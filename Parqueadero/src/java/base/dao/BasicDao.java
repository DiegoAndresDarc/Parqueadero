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
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author Brian Botina
 */
public class BasicDao {

    public Connection cnn;
    private ResultSet rs;
    private PreparedStatement ps;
    private StringBuilder sb;
    static int nconn = 0;

    //------------Métodos para manipular conexión y metadata--------------------//
    public BasicDao(String user_type) {
        nconn++;
        this.cnn = DBConnection.connect(user_type);
        this.sb = new StringBuilder();
        //System.out.println("Conexiones abiertas:" + nconn);

    }

    public void close() {
        if (DBConnection.checkConnection(cnn)) {
            DBConnection.closeConnection(cnn);
            //System.out.println("Conexiones cerradas :" + nconn);
        }
        nconn--;
        if (nconn < 0) {
            System.out.println("Inconsistencia en conexiones cerradas :" + nconn);
        }
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
            Logger.getLogger(BasicDao.class.getName()).log(Level.SEVERE, null, ex);
        } finally {
            DBConnection.closePreparedStatement(ps);
        }
        return rowCount;
    }

    public boolean insert(String table, Map<String, String> values) {
        Boolean result = false;
        try {
            StringBuilder sb = new StringBuilder();
            sb.append("INSERT INTO ").append(table).append(" (");
            for (Map.Entry<String, String> entry : values.entrySet()) {
                Object key = entry.getKey();
                Object val = entry.getValue();
                sb.append(key);
                sb.append(",");

            }
            sb.deleteCharAt(sb.lastIndexOf(","));
            sb.append(") VALUES (");
            for (int i = 0; i < values.size(); i++) {
                sb.append("?,");
            }
            sb.deleteCharAt(sb.lastIndexOf(","));
            sb.append(")");

            //execute insert
            ps = cnn.prepareStatement(sb.toString());
            int psParams = 1;
            for (String value : values.keySet()) {
                ps.setString(psParams++, values.get(value));
            }

            result = ps.executeUpdate() > 0;
            cnn.commit();

        } catch (SQLException ex) {
            Logger.getLogger(BasicDao.class.getName()).log(Level.SEVERE, null, ex);
            try {
                cnn.rollback();
            } catch (SQLException ex1) {
                Logger.getLogger(BasicDao.class.getName()).log(Level.SEVERE, null, ex1);
            }
        } finally {
            DBConnection.closePreparedStatement(ps);
        }
        return result;
    }

    public boolean update(List<String> tables, Map<String, String> fields) {
        Boolean result = false;
        try {

            for (String table : tables) {
                ArrayList<String> values = new ArrayList<>();
                sb = new StringBuilder();
                sb.append("UPDATE ").append(table).append(" SET ");
                for (String field : fields.keySet()) {
                    sb.append(field).append(" = ?,");
                    values.add(fields.get(field));

                }
                sb.deleteCharAt(sb.lastIndexOf(","));
                //sb.append(" WHERE ").append(keyName).append(" = ?");
                //execute insert
                ps = cnn.prepareStatement(sb.toString());
                int psParams = 1;
                for (int i = 1; i <= values.size(); i++) {
                    ps.setString(i, values.get(i - 1));
                }
            }
            result = ps.executeUpdate() > 0;

            cnn.commit();

        } catch (SQLException ex) {
            Logger.getLogger(BasicDao.class.getName()).log(Level.SEVERE, null, ex);
        } finally {
            DBConnection.closePreparedStatement(ps);
        }
        return result;
    }

    public Map<String, String> search(String table, Map<String, String> params, ArrayList<String> fields) {

        Map<String, String> result = new HashMap();
        try {
            ArrayList<String> values = new ArrayList();
            StringBuilder sbWhere = new StringBuilder();
            StringBuilder sb = new StringBuilder();
            sb.append("SELECT ");
            StringBuilder sbFields = new StringBuilder();
            if (fields != null) {
                for (String field : fields) {
                    if (sbFields.length() > 0) {
                        sbWhere.append(" , ");
                    }
                    sbFields.append(field);
                }
                sbFields.deleteCharAt(sbFields.lastIndexOf(","));
            } else {
                sbFields.append("* ");
            }
            sb.append(sbFields);
            sb.append(" FROM ").append(table);
            for (String field : params.keySet()) {
                if (sbWhere.length() > 0) {
                    sbWhere.append(" AND ");
                }
                sbWhere.append(field).append('=').append("?");
                String value = params.get(field);
                values.add(value);
            }

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
        } catch (SQLException ex) {
            Logger.getLogger(BasicDao.class.getName()).log(Level.SEVERE, null, ex);
        } finally {
            DBConnection.closePreparedStatement(ps);
        }
        return result;
    }

    public List<Map<String, String>> consult(ArrayList<String> table, Map<String, String> params, ArrayList<String> fields) {
        ArrayList result = new ArrayList();

        ArrayList<String> values = new ArrayList();
        int regMulCount = 0;
        try {
            StringBuilder sbWhere = new StringBuilder();
            StringBuilder sb = new StringBuilder();
            sb.append("SELECT ");
            StringBuilder sbFields = new StringBuilder();
            if (fields != null) {
                for (String field : fields) {
                    sbFields.append(field).append(",");
                }
                sbFields.deleteCharAt(sbFields.lastIndexOf(","));
            } else {
                sbFields.append("* ");
            }
            sb.append(sbFields);
            sb.append(" FROM ");
            for (int i = 0; i < table.size(); i++) {
                sb.append(table.get(i));
            }
            if (params != null) {
                for (String field : params.keySet()) {
                    if (sbWhere.length() > 0) {
                        sbWhere.append(" AND ");
                    }
                    sbWhere.append(field).append('=').append("?");
                    String value = params.get(field);
                    values.add(value);
                }
            }
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
                for (int col = 1; col <= colsCount; col++) {
                    map.put(rs.getMetaData().getColumnName(col),
                            rs.getString(col));
                }
                result.add(map);
            }
        } catch (SQLException ex) {
            Logger.getLogger(BasicDao.class.getName()).log(Level.SEVERE, null, ex);
        } finally {
            DBConnection.closePreparedStatement(ps);
        }
        return result;
    }

    public boolean delete(String tableName, String idName, int idValue) {
        ps = null;
        boolean execute = false;
        try {
            String sql;
            sql = "DELETE FROM ".concat(tableName).concat(" WHERE ").concat(idName).concat(" = ?");
            ps = cnn.prepareStatement(sql);
            ps.setString(1, String.valueOf(idValue));
            execute = ps.executeUpdate() != 0;
            cnn.commit();

        } catch (SQLException ex) {
            Logger.getLogger(BasicDao.class.getName()).log(Level.SEVERE, null, ex);
        } finally {
            DBConnection.closePreparedStatement(ps);
        }
        return execute;
    }

    public List<List<String>> consultWithQuery(String query, List<String> values) {
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

    public boolean inserWithQuery(String query, List<String> values) {
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

            } catch (SQLException ex1) {
                Logger.getLogger(BasicDao.class
                        .getName()).log(Level.SEVERE, null, ex1);

            }

        } finally {
            DBConnection.closePreparedStatement(ps);
        }
        return result;
    }

    public boolean updateWithQuery(String query, List<String> values) {
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
            Logger.getLogger(BasicDao.class
                    .getName()).log(Level.SEVERE, null, ex);
        }
        return result;
    }

}
