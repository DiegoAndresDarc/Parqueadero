/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package base.dao;

import base.persistence.connection.DBConnection;
import java.sql.Connection;
import java.sql.DatabaseMetaData;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author prog14
 */
public class BasicDao {

    public Connection cnn;
    private ResultSet rs;
    private PreparedStatement ps;
    private StringBuilder sb;
    static int nconn = 0;
/*
    //------------Métodos para manipular conexión y metadata--------------------//
    public BasicDao(){
        nconn++;
        try {
            this.cnn = DBConnection.connect();
            this.sb = new StringBuilder();
            //System.out.println("Conexiones abiertas:" + nconn);
        } catch (SystemException ex) {
            Logger.getLogger(BasicDao.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    public void close() throws JException {
        if (DBConnection.checkConnection(cnn)) {
            DBConnection.closeConnection(cnn);
            //System.out.println("Conexiones cerradas :" + nconn);
        }
        nconn--;
        if(nconn<0)
        {
            System.out.println("Inconsistencia en conexiones cerradas :" + nconn);
        }
    }

    public Map<String, List<String>> loadMetada() throws JException {
        Map<String, List<String>> tableColumns = new HashMap<>();
        try {
            List<String> tableNames = new ArrayList<>();
            if (cnn == null || !cnn.isValid(5)) {
                cnn = DBConnection.connect();
            }
            DatabaseMetaData meta = cnn.getMetaData();
            rs = meta.getTables(null, null, null, new String[]{"TABLE"});
            while (rs.next()) {
                tableNames.add(rs.getString("TABLE_NAME"));
            }
            for (String name : tableNames) {
                ps = cnn.prepareStatement("SELECT * FROM ".concat(name));
                rs = ps.executeQuery();
                ResultSetMetaData rsmd = rs.getMetaData();
                int columnCount = rsmd.getColumnCount();
                List<String> columns = new ArrayList<>();
                for (int i = 1; i <= columnCount; i++) {
                    columns.add(rsmd.getColumnName(i));
                }
                tableColumns.put(name, columns);
            }
        } catch (SQLException | SystemException ex) {
            Logger.getLogger(BasicDao.class.getName()).log(Level.SEVERE, null, ex);
            JError error = new JError();
            error.setUserError("Error al cargar datos de la BD");
            error.setErrorCode(JError.ERR_DB_LOAD_METADATA);
            error.setDebugError(ps.toString());
        } finally {
            if (DBConnection.checkPreparedStatement(ps)) {
                DBConnection.closePreparedStatement(ps);
            }
            if (DBConnection.checkConnection(cnn)) {
                DBConnection.closeConnection(cnn);
            }
        }
        return tableColumns;
    }

    public int count(String tableName, WebFormat reportFormat, WebFormat parametersFormat, Map<String, String> params) throws SQLException {
        int regCount = 0;
        StringBuilder sb = new StringBuilder();
        StringBuilder sbWhere = new StringBuilder();
        sb.append("SELECT COUNT(");
        sb.append(tableName).append(".jccn)");
        sb.append(" FROM ").append(tableName);
        //llena los joind de la tabla
        fillJoins(reportFormat, sb);
        sb.append(" WHERE ");
        List<String> values = new ArrayList<>();
        if (parametersFormat != null) {
            for (WebFormatDetail detail : parametersFormat.getDetails()) {
                sbWhere.append(detail.getField().getFieldName());
                sbWhere.append(getOperator(detail.getRangeType()));
                sbWhere.append("?");
                sbWhere.append(" AND ");
                if (params.get(detail.getFieldName()) != null) {
                    values.add((String) params.get(detail.getFieldName()));
                } else {
                    values.add((String) params.get(detail.getField().getFieldName()));
                }
            }
            sbWhere.setLength(sbWhere.length() - 5);
        }
        if (sbWhere.length() > 0) {
            sb.append(sbWhere);
        }
        ps = cnn.prepareStatement(sb.toString());
        for (int i = 1; i <= values.size(); i++) {
            ps.setString(i, values.get(i - 1));
        }
        rs = ps.executeQuery();
        if (rs.next()) {
            regCount = rs.getInt(1);
        }
        return regCount;
    }

    private ArrayList<WebFormatDetail> getForeignFields(WebFormat reportFormat) {
        ArrayList<WebFormatDetail> foreignFields = new ArrayList();
        ArrayList<String> aliasList = new ArrayList();
        for (WebFormatDetail detail : reportFormat.getDetails()) {
            boolean inJoins = false;
            if (detail.getTable() != reportFormat.getTable()) {
                //Si la tabla del ca,po es distinta  a la del formato se registra
                //el campo para buscar las relaciones posteriormente
                for (String alias : aliasList) {
                    if (alias.equals(detail.getTableAlias())) {
                        inJoins = true;
                        break;
                    }
                }
                if (!inJoins) {
                    aliasList.add(detail.getTableAlias());
                    foreignFields.add(detail);
                }
            }
        }
        return foreignFields;
    }

    private void fillJoins(WebFormat reportFormat, StringBuilder sb1) {
        int index = 0;
        //Llena el arreglo con los detalles de campos foráneos
        ArrayList<WebFormatDetail> foreignFields = getForeignFields(reportFormat);
        Map relationsMap = new HashMap();
        for (WebFormatDetail detail : foreignFields) {
            //Trae las relaciones posibles entre la tabla del formato y la foránea
            List<FieldRelation> relations = reportFormat.getTable().getRelations(detail.getTable());
            //Si se especifica el campo a través del cual se hace la  relación
            if (detail.getKeyFieldIndex() != 0) {
                Field keyField = reportFormat.getTable().getFields().get(detail.getKeyFieldIndex());
                for (FieldRelation relation : relations) {
                    //Verificar que no se haya hecho el inner join con el mismo campo
                    if (relationsMap.get(relation) == null) {
                        List<Field> fields = relation.getSourceFields();
                        for (Field field : fields) {
                            if (keyField == field) {
                                Table relationTable = detail.getTable();
                                fillInnerJoin(sb1, relationTable, relation,
                                        reportFormat.getTable().getName(), detail.getTableAlias());
                                relationsMap.put(relation, relation);
                                break;
                            }
                        }
                    }
                }
            } else {
                //cuando hay dos o mas relaciones en este for siempre el alias de la tabla va a ser el mismo 
                //porque estamos usando el mismo campo                
                for (FieldRelation relation : relations) {
                    if (relationsMap.get(relation) == null) {
                        Table relationTable = detail.getTable();
                        fillInnerJoin(sb1, relationTable, relation, reportFormat.getTable().getName(), detail.getTableAlias());
                        relationsMap.put(relation, relation);
                        break;
                    }
                }

            }
        }
    }

    public void fillInnerJoin(StringBuilder sb, Table relationTable, FieldRelation relation, String tableName, String tableAlias) {
        sb.append(" INNER JOIN ");
        sb.append(relationTable.getName());
        if (tableAlias != null) {
            sb.append(" AS ");
            sb.append(tableAlias);
        } else {
            tableAlias = tableName;
        }
        sb.append(" ON ");
        for (int fieldIndex = 0; fieldIndex < relation.getSourceFields().size(); fieldIndex++) {
            sb.append(tableName);
            sb.append(".");
            sb.append(relation.getSourceFields().get(fieldIndex).getFieldName());
            sb.append("=");
            sb.append(tableAlias);
            sb.append(".");
            sb.append(relation.getForeignFields().get(fieldIndex).getFieldName());
            sb.append(" AND ");
        }
        sb.setLength(sb.length() - 5);
    }

    private int countItems(String tableName, Map<String, String> params) {
        int rowCount = 0;
        int nParam = 0;
        try {
            StringBuilder sb = new StringBuilder();
            sb.append("SELECT MAX(jccn)");
            if (params != null && params.size() > 0) {
                for (String key : params.keySet()) {
                    sb.append(",");
                    sb.append(params.get(key)).append(" AS ").append(key);
                }
            }
            sb.append(" FROM ").append(tableName);
            if (params != null && params.size() > 0) {
                sb.append(" WHERE ");
                for (String key : params.keySet()) {
                    if (nParam > 0) {
                        sb.append(" AND ");
                    }
                    sb.append(key).append("=").append(params.get(key));
                }
            }
            ps = cnn.prepareStatement(sb.toString());
            rs = ps.executeQuery();
            if (rs.next()) {
                for (String key : params.keySet()) {
                    params.put(key, rs.getString(key));
                }
                rowCount = rs.getInt(1);
            } else {
                rowCount = 0;

            }
        } catch (SQLException ex) {
            Logger.getLogger(BasicDao.class
                    .getName()).log(Level.SEVERE, null, ex);
            JError error = new JError();
            error.setUserError("error al contar los elementos");
            error.setErrorCode(JError.ERR_DB_COUNT);
            error.setDebugError(ex.toString());
        }
        return rowCount;
    }

    //----------------------Obtener fieldType tabla y params adicionales-------------//
    public Map getTableTypeFields(Table table, Integer user) {
        Map<String, String> values = new HashMap<>();
        //Obtener campos
        if (table.getAgency() > 1) {
            values.put("jagencia", "0");
        }
        switch ((int) table.getType()) {
            case 1:
                values.put("jmesc", "MONTH(NOW())");
                values.put("janoc", "YEAR(NOW())");
                break;
            case 2:
                values.put("janoc", "YEAR(NOW())");
                break;
            case 18:
                values.put("jusr", String.valueOf(user));
                break;
        }
        //Crear mapa de campos
        values.put("jccn", String.valueOf(countItems(table.getName(), values) + 1));
        return values;

    }

    public boolean insert(List<WebFormat> formats, Map<String, String> values, Integer user) throws JException {
        Boolean result = false;
        try {
            Map<String, String> insertValues = new HashMap();
            Map<String, String> keyMap = null;
            String keyName = null;
            for (WebFormat format : formats) {
                if (FormatType.DATA.getInt() == format.getType()) {
                    StringBuilder sb;
                    sb = new StringBuilder();
                    String fto = format.getTable().getName();
                    sb.append("INSERT INTO ").append(fto).append(" (");
                    if (format.getTable().getType() == 0) {
                        for (Field fld : format.getTable().getFields()) {
                            if (fld != null && fld.isPrimary()) {
                                keyName = fld.getFieldName();
                                break;
                            }
                        }
                    } else {
                        keyMap = getTableTypeFields(format.getTable(), user);
                    }

                    for (WebFormatDetail detail : format.getDetails()) {
                        if (detail.getField().getFieldName().equals(keyName)
                                && format.getTable().getType() == 0) {
                            //Quita valores autoincrementales
                            values.remove(detail.getField().getFieldName());
                        } else {
                            sb.append(detail.getField().getFieldName()).append(",");
                            //(P) Validacion de datos
                            insertValues.put(detail.getField().getFieldName(), values.get(detail.getField().getFieldName()));
                        }
                    }
                    if (keyMap != null) {
                        for (String key : keyMap.keySet()) {
                            insertValues.put(key, keyMap.get(key));
                        }
                    }
                    sb.deleteCharAt(sb.lastIndexOf(","));
                    sb.append(") VALUES (");
                    for (int i = 0; i < insertValues.size(); i++) {
                        sb.append("?,");
                    }
                    sb.deleteCharAt(sb.lastIndexOf(","));
                    sb.append(")");

                    //execute insert
                    ps = cnn.prepareStatement(sb.toString(), PreparedStatement.RETURN_GENERATED_KEYS);
                    int psParams = 1;
                    for (WebFormatDetail detail : format.getDetails()) {
                        if (detail.getField().getFieldName().equals(keyName)) {
                        } else {
                            ps.setString(psParams++, insertValues.get(detail.getField().getFieldName()));
                        }
                    }
                    result = ps.executeUpdate() > 0;
                }
            }
            cnn.commit();
            if (keyName != null) {
                ResultSet rsKeys = ps.getGeneratedKeys();
                rsKeys.first();
                values.put(keyName, rsKeys.getString(1));
            } else if (keyMap != null) {
                //Indices compuestos
                for (String key : keyMap.keySet()) {
                    values.put(key, keyMap.get(key));
                }
            }
        } catch (SQLException ex) {
            result = false;
            DBConnection.rollBack(cnn);
            Logger
                    .getLogger(BasicDao.class
                            .getName()).log(Level.SEVERE, null, ex);
            JError error = new JError();
            error.setUserError("error al insertar los elementos");
            error.setErrorCode(JError.ERR_DB_COUNT);
            error.setDebugError(ps.toString());
        } finally {
            DBConnection.closePreparedStatement(ps);
        }
        return result;
    }

    public boolean update(List<WebFormat> formats, Map<String, String> values) throws JException {
        Boolean result = false;
        String keyName = null;
        try {
            for (WebFormat format : formats) {
                if (FormatType.DATA.getInt() == format.getType()) {

                    //Obtener los valores de esa tabla
                    Table formatTable = format.getTable();
                    for (Field fld : format.getTable().getFields()) {
                        if (fld != null && fld.isPrimary()) {
                            keyName = fld.getFieldName();
                            break;
                        }
                    }

                    sb = new StringBuilder();
                    sb.append("UPDATE ").append(formatTable.getName()).append(" SET ");
                    for (WebFormatDetail detail : format.getDetails()) {
                        if (detail.getTable() == formatTable) {
                            sb.append(detail.getField().getFieldName()).append(" = ?,");
                        }
                    }
                    sb.deleteCharAt(sb.lastIndexOf(","));
                    sb.append(" WHERE ").append(keyName).append(" = ?");
                    //execute insert
                    ps = cnn.prepareStatement(sb.toString());
                    int psParams = 1;
                    for (WebFormatDetail detail : format.getDetails()) {
                        if (detail.getTable() == formatTable) {
                            ps.setString(psParams, values.get(detail.getField().getFieldName()));
                            psParams++;
                        }
                    }
                    ps.setString(psParams, values.get(keyName));
                    result = ps.executeUpdate() > 0;
                }
            }
            cnn.commit();
        } catch (SQLException ex) {
            result = false;
            DBConnection.rollBack(cnn);
            Logger
                    .getLogger(BasicDao.class
                            .getName()).log(Level.SEVERE, null, ex);

            Logger
                    .getLogger(BasicDao.class
                            .getName()).log(Level.SEVERE, null, ex);
            JError error = new JError();
            error.setUserError("error al actualizar los elementos");
            error.setErrorCode(JError.ERR_DB_UPDATE);
            error.setDebugError(sb.toString());
        } finally {
            DBConnection.closePreparedStatement(ps);
        }
        return result;
    }

    public List<Map<String, String>> consult(WebFormat parametersFormat,
            WebFormat reportFormat, Map<String, ? extends Object> params, boolean orderBy) throws JException {
        ArrayList result = new ArrayList();

        List<String> values = new ArrayList<>();
        int regMulCount = 0;
        final short REGMUL_TYPE = 74;
        boolean expandCodes = reportFormat.getSubType() == 41 || reportFormat.getSubType() == 44 || reportFormat.getSubType() == 42;
        try {
            StringBuilder sbWhere = new StringBuilder();
            StringBuilder sb = new StringBuilder();
            if (parametersFormat != null) {
                for (WebFormatDetail detail : parametersFormat.getDetails()) {
                    if (detail.getField().getFieldName().equals("control")
                            && params.get("control") == null) {
                        {
                            for (Field keyField : parametersFormat.getTable().getDataStructs().get(0).getPrimaryKeys()) {
                                if (params.get(keyField.getFieldName()) != null) {
                                    if (sbWhere.length() > 0) {
                                        sbWhere.append(" AND ");
                                    }
                                    sbWhere.append(detail.getTable().getName()).append('.').append(keyField.getFieldName());
                                    sbWhere.append(" = ?");
                                    values.add((String) params.get(keyField.getFieldName()));
                                }
                            }
                        }
                    } else {
                        if (sbWhere.length() > 0) {
                            sbWhere.append(" AND ");
                        }
                        if (detail.getField().getType() == REGMUL_TYPE) {
                            String regMulTableName = detail.getField().getFieldName() + "_" + detail.getTable().getName();
                            sbWhere.append(regMulTableName).append(".codigo");
                            regMulCount++;
                        } else {
                            sbWhere.append(detail.getTable().getName()).append('.').append(detail.getField().getFieldName());
                        }
                        Object value = params.get(detail.getFieldName());
                        if (value != null) {
                            if (RangeType.getRangeType(detail.getRangeType()) == RangeType.KEYWORD) {
                                sbWhere.append(" LIKE (?)");
                                values.add((String) value + "%");
                            } else {
                                Class valueClass = value.getClass();

                                if (detail.getField().getType() == REGMUL_TYPE)//reg,mul
                                {
                                    if (valueClass == String.class) {
                                        value = ((String) value).split(",");

                                    }
                                }
                                if (value.getClass() == String.class) {
                                    sbWhere.append(getOperator(detail.getRangeType()));
                                    sbWhere.append("?");
                                    values.add((String) value);

                                } else if (value.getClass() == String[].class) {
                                    sbWhere.append(" IN (");
                                    for (String str : (String[]) value) {
                                        sbWhere.append("?,");
                                        values.add(str);
                                    }
                                    sbWhere.deleteCharAt(sbWhere.length() - 1);
                                    sbWhere.append(")");
                                }
                            }
                        }
                    }
                }
            }
            //Se deja la tabla de formato en primera posicioón
            int nCode = 0;
            for (WebFormatDetail detail : reportFormat.getDetails()) {
                String select;
                if (detail.getField().getCodeList() != null && expandCodes) {
                    select = "codigos_definidos" + nCode + ".namedefcod";
                    nCode++;
                } else {
                    if (detail.getTable() != reportFormat.getTable()) {
                        select = detail.getTableAlias().concat(".").concat(detail.getField().getFieldName());
                    } else {
                        select = detail.getTable().getName().concat(".").concat(detail.getField().getFieldName());
                    }
                }
                if (sb.lastIndexOf(select) < 0) {
                    sb.append(select).append(",");
                }
            }

            sb.deleteCharAt(sb.length() - 1);
            sb.append(" FROM ");
            sb.append(reportFormat.getTable().getName());
            fillJoins(reportFormat, sb);

            if (nCode > 0 && expandCodes) {
                int codeIndex = 0;
                for (WebFormatDetail detail : reportFormat.getDetails()) {
                    if (detail.getField().getCodeList() != null && expandCodes) {
                        String alias = "codigos_definidos" + codeIndex;
                        sb.append(" INNER JOIN ");
                        sb.append("codigos_definidos AS ").append(alias);
                        sb.append(" ON ");
                        sb.append(detail.getTable().getName()).append(".");
                        sb.append(detail.getField().getFieldName());
                        sb.append(" = ");
                        sb.append(alias).append(".ndefcod");
                        sb.append(" AND ");
                        sb.append(alias).append(".codigo_grupo");
                        sb.append(" = ").append(detail.getField().getListCode());
                        codeIndex++;
                    }
                }
            }
            if (regMulCount > 0) {
                for (WebFormatDetail detail : parametersFormat.getDetails()) {
                    if (detail.getField().getType() == REGMUL_TYPE) {
                        sb.append(" INNER JOIN ");
                        String regMulTableName = detail.getField().getFieldName() + "_" + detail.getTable().getName();
                        sb.append(regMulTableName).append(" ON ");
                        sb.append(regMulTableName).append(".ccn_maestro");
                        sb.append(" = ").append(detail.getTable().getName());
                        sb.append(".").append("jccn");
                    }
                }
            }

            if (sb.length() > 0) {
                sb.insert(0, "SELECT ");
                if (sbWhere.length() > 0) {
                    sb.append(" WHERE ");
                    sb.append(sbWhere);
                }
                if (orderBy) {
                    sb.append(" ORDER BY jccn");
                }
                ps = cnn.prepareStatement(sb.toString());
                for (int i = 1; i <= values.size(); i++) {
                    ps.setString(i, values.get(i - 1));
                }
                rs = ps.executeQuery();
                int colsCount = ps.getMetaData().getColumnCount();
                while (rs.next()) {
                    Map map = new HashMap();
                    result.add(map);
                    for (int col = 1; col <= colsCount; col++) {
                        String fieldName = reportFormat.getDetails().get(col - 1).getFieldName();
                        if (reportFormat.getDetails().get(col - 1).getAlias() != null) {
                            fieldName = reportFormat.getDetails().get(col - 1).getAlias();
                        }
                        /*
                        if (map.get(fieldName) != null) {                            
                            fieldName += String.valueOf(col);
                        } rs.getMetaData().getColumnName(col)
                         

                        map.put(fieldName, rs.getString(col));
                    }
                }
            }
        } catch (SQLException ex) {
            Logger.getLogger(BasicDao.class
                    .getName()).log(Level.SEVERE, null, ex);
            Logger
                    .getLogger(BasicDao.class
                            .getName()).log(Level.SEVERE, null, ex);
            JError error = new JError();
            error.setUserError("error al contar los elementos");
            error.setErrorCode(JError.ERR_DB_COUNT);
            error.setDebugError(ex.toString());
        } finally {
            DBConnection.closePreparedStatement(ps);
        }
        return result;
    }

    public List<Map<String, String>> read(WebFormat reportFormat, Map<String, ? extends Object> params) throws JException {

        ArrayList result = new ArrayList();
        ArrayList tables = new ArrayList();
        List<String> values = new ArrayList<>();
        try {
            StringBuilder sbWhere = new StringBuilder();
            StringBuilder sb = new StringBuilder();
            if (params != null) {
                for (String key : params.keySet()) {
                    Object value = params.get(key);
                    if (value != null) {
                        if (sbWhere.length() > 0) {
                            sbWhere.append(" AND ");
                        }
                        sbWhere.append(key);

                        if (value.getClass() == String.class) {
                            sbWhere.append(" =");
                            sbWhere.append("?");
                            values.add((String) value);

                        } else if (value.getClass() == String[].class) {
                            sbWhere.append(" IN (");
                            for (String str : (String[]) value) {
                                sbWhere.append("?,");
                                values.add(str);
                            }
                            sbWhere.deleteCharAt(sbWhere.length() - 1);
                            sbWhere.append(")");
                        }
                    }
                }
            }
            reportFormat.getDetails().forEach((detail) -> {
                String select = reportFormat.getTable().getName().concat(".").concat(detail.getField().getFieldName());
                if (sb.lastIndexOf(select) < 0) {
                    sb.append(select).append(",");
                    boolean inTables = tables.stream().noneMatch(t -> t.equals(reportFormat.getTable().getName()));
                    if (tables.isEmpty() || inTables) {
                        tables.add(reportFormat.getTable().getName());
                    }
                }
            });

            sb.deleteCharAt(sb.length() - 1);
            sb.append(" FROM ");
            tables.forEach(t -> {
                sb.append(t);
                sb.append(",");
            });
            sb.deleteCharAt(sb.length() - 1);
            if (sb.length() > 0) {
                sb.insert(0, "SELECT ");
                if (sbWhere.length() > 0) {
                    sb.append(" WHERE ");
                    sb.append(sbWhere);
                }
                ps = cnn.prepareStatement(sb.toString());
                for (int i = 1; i <= values.size(); i++) {
                    ps.setString(i, values.get(i - 1));
                }
                rs = ps.executeQuery();
                int colsCount = ps.getMetaData().getColumnCount();
                while (rs.next()) {
                    Map map = new HashMap();
                    result.add(map);
                    for (int col = 1; col <= colsCount; col++) {
                        map.put(rs.getMetaData().getColumnName(col),
                                rs.getString(col));

                    }
                }
            }
        } catch (Exception ex) {
            Logger.getLogger(BasicDao.class
                    .getName()).log(Level.SEVERE, null, ex);
            Logger
                    .getLogger(BasicDao.class
                            .getName()).log(Level.SEVERE, null, ex);
            JError error = new JError();
            error.setUserError("error al leer registros");
            error.setErrorCode(JError.ERR_DB_READ);
            error.setDebugError(sb.toString());
        } finally {
            DBConnection.closePreparedStatement(ps);
        }
        return result;
    }

    public Map<String, String> search(List<WebFormat> formats, Map<String, String> params) throws JException {

        Map<String, String> result = new HashMap();
        ArrayList tables = new ArrayList();
        List<String> values = new ArrayList<>();
        try {
            StringBuilder sbWhere = new StringBuilder();
            StringBuilder sb = new StringBuilder();
            for (String field : params.keySet()) {
                if (sbWhere.length() > 0) {
                    sbWhere.append(" AND ");
                }
                sbWhere.append(field).append('=').append("?");
                String value = params.get(field);
                values.add(value);
            }

            for (int index = 0;
                    index < formats.size();
                    index++) {
                WebFormat format = formats.get(index);
                if (format.getType() == FormatType.DATA.getInt()) {
                    format.getDetails().forEach((detail) -> {
                        String select = format.getTable().getName().concat(".").concat(detail.getField().getFieldName());
                        if (sb.lastIndexOf(select) < 0) {
                            sb.append(select).append(",");
                            boolean inTables = tables.stream().noneMatch(t -> t.equals(format.getTable().getName()));
                            if (tables.isEmpty() || inTables) {
                                tables.add(format.getTable().getName());
                            }
                        }
                    });
                }
            }

            sb.deleteCharAt(sb.length() - 1);
            sb.append(
                    " FROM ");
            tables.forEach(t
                    -> {
                sb.append(t);
                sb.append(",");
            }
            );
            sb.deleteCharAt(sb.length() - 1);
            if (sb.length()
                    > 0) {
                sb.insert(0, "SELECT ");
                if (sbWhere.length() > 0) {
                    sb.append(" WHERE ");
                    sb.append(sbWhere);
                }
                ps = cnn.prepareStatement(sb.toString());
                for (int i = 1; i <= values.size(); i++) {
                    ps.setString(i, values.get(i - 1));
                }
                rs = ps.executeQuery();
                int colsCount = ps.getMetaData().getColumnCount();
                while (rs.next()) {

                    for (int col = 1; col <= colsCount; col++) {
                        result.put(rs.getMetaData().getColumnName(col),
                                rs.getString(col));

                    }
                }
            }

        } catch (Exception ex) {
            Logger.getLogger(BasicDao.class
                    .getName()).log(Level.SEVERE, null, ex);
            Logger
                    .getLogger(BasicDao.class
                            .getName()).log(Level.SEVERE, null, ex);
            JError error = new JError();
            error.setUserError("error al contar los elementos");
            error.setErrorCode(JError.ERR_DB_COUNT);
            error.setDebugError(ex.toString());
        } finally {
            DBConnection.closePreparedStatement(ps);
        }
        return result;
    }

    public boolean delete(String tableName, String idName, int idValue) throws JException {
        ps = null;
        try {
            String sql;
            boolean execute;
            sql = "DELETE FROM ".concat(tableName).concat(" WHERE ").concat(idName).concat(" = ?");
            ps = cnn.prepareStatement(sql);
            ps.setString(1, String.valueOf(idValue));
            execute = ps.executeUpdate() != 0;
            cnn.commit();
            return execute;

        } catch (SQLException ex) {
            Logger.getLogger(BasicDao.class
                    .getName()).log(Level.SEVERE, null, ex);
            JError error = new JError();
            error.setUserError("Error al eliminar ");
            error.setErrorCode(JError.ERR_DB_DELETE);
            error.setDebugError(ex.toString());
            throw new JException(error);
        } finally {
            DBConnection.closePreparedStatement(ps);
        }
    }

    public List<String> getLastRow(String tableName) throws JException {
        List<String> row = null;
        int colsCount, index;
        ps = null;
        try {
            String sql = "SELECT * FROM " + tableName
                    + " ORDER BY codigo DESC "
                    + "LIMIT 1";
            ps = cnn.prepareStatement(sql);
            rs = ps.executeQuery();
            cnn.commit();
            colsCount = rs.getMetaData().getColumnCount();
            while (rs.next()) {
                row = new ArrayList<>();
                for (index = 1; index <= colsCount; index++) {
                    row.add(rs.getString(index));
                }
                return row;
            }
        } catch (SQLException ex) {
            JError error = new JError();
            error.setUserError("No se pudo obtener la ultima columna");
            error.setErrorCode(JError.ERR_GET_LAST_ROW);
            error.setDebugError(ex.toString());
            throw new JException(error);
        } finally {
            DBConnection.closePreparedStatement(ps);
        }
        return row;
    }

    public List<List<String>> consultWithQuery(String query, List<String> values) throws JException {
        List<List<String>> rowList = new ArrayList<>();
        List<String> row;
        int colsCount, index;
        ps = null;
        try {
            ps = cnn.prepareStatement(query);
            if (values != null && values.size() > 0) {
                index = 1;
                for (String value : values) {
                    ps.setString(index++, value);
                }
            }
            rs = ps.executeQuery();
            cnn.commit();
            colsCount = rs.getMetaData().getColumnCount();
            while (rs.next()) {
                row = new ArrayList<>();
                rowList.add(row);
                for (index = 1; index <= colsCount; index++) {
                    row.add(rs.getString(index));
                }
            }
            rs.close();

        } catch (SQLException ex) {
            Logger.getLogger(BasicDao.class
                    .getName()).log(Level.SEVERE, null, ex);
            JError error = new JError();
            error.setUserError("Error al consultar la base de datos ");
            error.setErrorCode(JError.ERR_DB_CONSULT_QUERY);
            error.setDebugError(ex.toString());
            throw new JException(error);
        } finally {
            DBConnection.closePreparedStatement(ps);
        }
        return rowList;
    }

    private String getOperator(int tiporango) {
        switch (tiporango) {
            case 2:
                return ">=";
            case 3:
                return "<=";
            default:
                return "=";
        }
    }

    public boolean inserWithQuery(String query, List<String> values) throws JException {
        boolean result = false;
        try {
            ps = cnn.prepareStatement(query);
            int psParams = 1;
            if (values != null) {
                for (String value : values) {
                    ps.setString(psParams, value);
                    psParams++;
                }
            }
            result = ps.executeUpdate() > 0;
            cnn.commit();
        } catch (SQLException ex) {
            try {
                cnn.rollback();
                JError error = new JError();
                error.setUserError("error al insertar el dato");
                error.setErrorCode(JError.ERR_DB_INSERT_QUERY_1);
                error.setDebugError(ps.toString());
                throw new JException(error);

            } catch (SQLException ex1) {
                Logger.getLogger(BasicDao.class
                        .getName()).log(Level.SEVERE, null, ex1);
                JError error = new JError();
                error.setUserError("error al inserrtar el dato");
                error.setErrorCode(JError.ERR_DB_INSERT_QUERY_2);
                error.setDebugError(ps.toString());
                throw new JException(error);

            }

        } finally {
            DBConnection.closePreparedStatement(ps);
        }
        return result;
    }

    public List getFieldList(FieldRelation fr, String[] fieldList, Map<String, String> params, String searchQuery) throws JException {
        Table foreignTable;
        List<List<String>> resultList = null;
        List<String> values = new ArrayList<>();
        List result = new ArrayList();

        if (fr != null) {
            foreignTable = fr.getForeignTable();
            String stringFields = "concat(";
            if (fieldList == null) {
                fieldList = new String[1];
                fieldList[0] = fr.getForeignFields().get(0).getFieldName();
            }
            StringBuilder query = new StringBuilder();
            query.append("select ");

            for (String fieldName : fieldList) {
                stringFields += fieldName + ",' ',";
            }
            for (Field foreignKey : fr.getForeignFields()) {
                query.append(foreignKey.getFieldName()).append(",");
                stringFields += foreignKey.getFieldName() + ",' ',";
            }
            stringFields = stringFields.substring(0, stringFields.length() - 5);
            stringFields += ")";
            query.append(stringFields)
                    .append(" from ").append(foreignTable.getName());
            values = new ArrayList<>();
            if (params != null || searchQuery != null) {
                query.append(" where ");
                if (params != null) {
                    for (String key : params.keySet()) {
                        Object obj = params.get(key);

                        if (obj.getClass() == String.class) {
                            query.append(key).append("=? ");
                            values.add((String) params.get(key));

                        } else if (obj.getClass() == String[].class) {
                            query.append(key).append(" IN ( ");
                            for (String str : (String[]) obj) {
                                query.append("?,");
                                values.add(str);
                            }
                            query.setLength(query.length() - 1);
                            query.append(") ");
                        }
                        query.append(" and ");
                    }
                }
                if (searchQuery != null) {
                    query.append(stringFields).append(" LIKE ?");
                    values.add("%" + searchQuery + "%");
                } else {
                    query.setLength(query.length() - 6);
                }
            }
            resultList = consultWithQuery(query.toString(), values);
            resultList.forEach(res -> {
                ItemCode item = new ItemCode();
                item.code = res.get(0);
                item.name = res.get(1);
                result.add(item);
            });
        }
        return result;
    }

    public static String getCodeDescription(WebFormatDetail detail, String value) throws JException {
        String result = null;
        BasicDao dao = new BasicDao();
        List<String> values = new ArrayList<>();
        values.add(String.valueOf(detail.getField().getListCode()));
        values.add(String.valueOf(value));
        List<List<String>> list = dao.consultWithQuery("SELECT "
                + "namedefcod FROM codigos_definidos "
                + "WHERE "
                + "codigo_grupo= ? AND ndefcod = ? ORDER BY ndefcod", values);
        if (list != null && list.size() > 0) {
            result = list.get(0).get(0);
        }
        dao.close();
        return result;
    }

    public static List getCodeList(long listCode) throws JException {
        if (listCode == 0) {
            return null;
        }
        List result = new ArrayList();
        BasicDao dao = new BasicDao();
        List<String> values = new ArrayList<>();
        values.add(String.valueOf(listCode));
        List<List<String>> codes = dao.consultWithQuery("SELECT ndefcod,namedefcod FROM codigos_definidos where codigo_grupo= ? ORDER BY ndefcod", values);
        for (List<String> code : codes) {
            ItemCode item = new ItemCode();

            item.code = code.get(0);

            item.name = code.get(1);
            result.add(item);
        }
        dao.close();
        return result;
    }

    public Connection getConnection() {
        return cnn;
    }

    public String getInnerJoin(WebFormatDetail webFormatDetail) {
        /*
        INNER JOIN usuarios
ON jtracktime.nit_empleado = usuarios.nit AND jtracktime.tipo_documento = usuarios.tipo_doc
INNER JOIN jcompany
on jcompany.nit = jtracktime.nit_empresa
         
//ArrayList fieldRelationsArrayList = (ArrayList) format.getTable().getFieldRelations();
        String strInnerJoin = "";

        if (webFormatDetail.getTable() == null) {
            return "";
        }

        for (int i = 0; i < webFormatDetail.getTable().getFieldRelations().size(); i++) {
            strInnerJoin += " INNER JOIN ";
            strInnerJoin += webFormatDetail.getTable().getName();
            strInnerJoin += " ON ";
            /*
            for (int j = 0; j < webFormat.getTable().getFieldRelations().size(); j++) {
                strInnerJoin += webFormat.getTable().getFieldRelations().get(i).getForeignTable().getName();
                strInnerJoin += ".";
                strInnerJoin += webFormat.getTable().getName();
                strInnerJoin += " = ";
                strInnerJoin += webFormat.getTable().getRelations(i).getForeignFields().getFieldName();

                webFormat.getTable().getRelations(i).getForeignFields().getFieldName();
                strInnerJoin += " AND ";
            }
            strInnerJoin.substring(0, strInnerJoin.length() - 3);
        }
        }
        return strInnerJoin;
    }

    public boolean updateWithQuery(String query, List<String> values) throws JException, SQLException {
        boolean result = false;
        try {
            ps = cnn.prepareStatement(query);
            int psParams = 1;
            if (values != null) {
                for (String value : values) {
                    ps.setString(psParams, value);
                    psParams++;
                }
            }
            result = ps.executeUpdate() > 0;
            cnn.commit();
        } finally {

        }
        return result;
    }
*/
}
