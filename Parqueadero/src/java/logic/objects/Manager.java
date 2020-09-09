/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package logic.objects;

import base.dao.BasicDao;
import java.util.HashMap;
import java.util.Map;

/**
 *
 * @author Prog7
 */
public class Manager {

    private static Manager manager;
    private HashMap<String, Usuario> usuarios;
    private BasicDao basicDao;

    private Manager() {
        usuarios = new HashMap();
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
        if (data.get("usuario").equalsIgnoreCase("root")) {
            usuario = new Usuario();
            usuario.setTipo_usuario("R");
            usuario.setNombres("Administrador");
            usuario.setApellidos("del sistema");
            usuario.setBasicDao("R");
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
        return usuarios.get(id).getMenu();
    }
}
