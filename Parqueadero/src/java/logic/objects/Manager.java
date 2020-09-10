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
            usuario.setNombres("Administrador");
            usuario.setApellidos("del sistema");
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
        return userData;
    }

    public void deleteUser(String id) {
        usuarios.remove(id);
    }

    public boolean signUpUser(HashMap<String, String> data) {
        boolean result;
        basicDao = new BasicDao("r");
        result = basicDao.insert("usuario", data);
        basicDao.close();
        return result;
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
}
