/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package logic.objects;

import base.dao.BasicDao;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 *
 * @author Prog7
 */
public class Manager {
    private static Manager manager;
    private HashMap<String,Usuario> usuarios;
    private BasicDao basicDao;
    
    private Manager(){
        usuarios = new HashMap();
    }
    
    public static Manager getManager(){
        if(manager == null){
            manager = new Manager();
        }
        return manager;
    }
    
    public boolean loginUser(HashMap<String,String> data){
        basicDao = new BasicDao("r");
        return true;
    }
    public boolean signUpUser(HashMap<String,String> data){
        boolean result;
        basicDao = new BasicDao("r");
        result = basicDao.insert("usuario", data);
        basicDao.close();
        return result;
    }
}
