/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package logic.objects;

import base.dao.BasicDao;
import base.persistence.connection.DBConnection;
import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Properties;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author Prog7
 */
public class Manager {

    private static Manager manager;
    private HashMap<String, Usuario> usuarios;
    private BasicDao basicDao;
    private Properties databasProperties;

    private Manager() {
        usuarios = new HashMap();
        databasProperties = new Properties();
        setGeneralProperties();
    }

    public static Manager getManager() {
        if (manager == null) {
            manager = new Manager();
        }
        return manager;
    }

    public boolean loginUser(HashMap<String, String> data, String id) {
        boolean result = false;
        basicDao = new BasicDao("r");
        Usuario usuario = null;
        if (data.get("usuario").equals(databasProperties.get("mysql_r_user"))) {
            usuario = new Usuario();
            usuario.setTipo_usuario("R");
            usuario.setNombres("ADMINISTRADOR");
            usuario.setApellidos("DEL SISTEMA");
            usuario.setBasicDao("r");
            result = true;
        } else {
            Map<String, String> res = basicDao.search("usuario", data, null);
            if (res.size() > 0) {
                usuario = new Usuario();
                usuario.fillData((HashMap) res);
                result = true;
            }
        }
        usuarios.put(id, usuario);
        basicDao.close();
        return result;
    }

    public Map<String, String> getUserdata(String id) {
        Usuario usuario = usuarios.get(id);
        Map<String, String> userData = new HashMap();
        userData.put("nombres", usuario.getNombres());
        userData.put("apellidos", usuario.getApellidos());
        userData.put("usuario", usuario.getTipo_usuario());
        return userData;
    }

    public void deleteUser(String id) {
        Usuario usuario = usuarios.get(id);
        if (usuario != null) {
            usuario.getBasicDao().close();
            usuarios.remove(id);
        }
    }

    public boolean signUpUser(HashMap<String, String> data) {
        boolean result;
        basicDao = new BasicDao("r");
        result = basicDao.insert("usuario", data);
        basicDao.close();
        return result;
    }

    public boolean insert(HashMap<String, String> data, String id, String table) {
        Usuario usuario = usuarios.get(id);
        return usuario.getBasicDao().insert(table, data);
    }

    public Object getMenu(String id) {
        Usuario usuario = usuarios.get(id);
        Object object = null;
        if (usuario != null) {
            object = usuario.getMenu();
        }
        return object;
    }

    protected void setGeneralProperties() {
        try {
            ClassLoader classLoader = Thread.currentThread().getContextClassLoader();
            InputStream input = classLoader.getResourceAsStream("properties.properties");
            databasProperties.load(input);
        } catch (IOException ex) {
            Logger.getLogger(DBConnection.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    public Object update(String id, HashMap<String, String> data) {
        String table = (String) data.get("tabla");
        data.remove("tabla");
        Usuario usuario = usuarios.get(id);
        Object object = null;
        if (usuario != null) {
            ArrayList<String> tables = new ArrayList<>();
            tables.add(table);
            String keyName = "id";
            int keyValue = Integer.parseInt(data.get("id"));
            data.remove("id");
            object = usuario.getBasicDao().update(tables, data, keyName, keyValue);
        }
        return object;
    }

    public Object delete(String id, HashMap<String, String> data) {
        String table = (String) data.get("tabla");
        data.remove("tabla");
        Usuario usuario = usuarios.get(id);
        Object object = null;
        if (usuario != null) {
            String key = "", value = "";
            for (Map.Entry<String, String> entry : data.entrySet()) {
                key = entry.getKey();
                value = entry.getValue();
            }
            object = usuario.getBasicDao().delete(table, key, Integer.parseInt(value));
        }
        return object;
    }

    public Object getInformation(String id, HashMap<String, String> data) {
        Object object = null;
        ArrayList<String> tables = new ArrayList<>();
        HashMap<String, String> params = null;
        String table = data.get("tabla");
        data.remove("tabla");
        tables.add(table);
        if (data.containsKey("signup")) {
            basicDao = new BasicDao("r");
            object = basicDao.consult(tables, params, null);
            basicDao.close();
        } else {
            Usuario usuario = usuarios.get(id);
            if (usuario != null) {
                if (data.size() > 0) {
                    params = new HashMap();
                    for (Map.Entry<String, String> entry : data.entrySet()) {
                        String key = entry.getKey();
                        String value = entry.getValue();
                        params.put(key, value);
                    }
                }
                object = usuario.getBasicDao().consult(tables, params, null);
            }
        }
        return object;
    }

}
