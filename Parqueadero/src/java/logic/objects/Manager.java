/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package logic.objects;

/**
 *
 * @author Prog7
 */
public class Manager {
    private static Manager manager;
    private Usuario usuario;
    
    private Manager(){
        
    }
    
    public static Manager getManager(){
        if(manager == null){
            manager = new Manager();
        }
        return manager;
    }
}
