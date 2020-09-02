/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package logic.objects;

import base.dao.BasicDao;
import java.util.HashMap;

/**
 *
 * @author Brian Botina
 */
public class Usuario {

    private String tipo_doc, nombres, apellidos, usuario, password, email,tipo_usuario;
    private int telefono, celular, identificacion;
    private BasicDao basicDao;
    private HashMap<String,String> data;
    
    public Usuario(HashMap<String,String> data){
        this.data = data;
        fillData();
        basicDao = new BasicDao(tipo_usuario);
    }
    
    public void fillData(){
        
    }
    
    public String getTipo_doc() {
        return tipo_doc;
    }

    public void setTipo_doc(String tipo_doc) {
        this.tipo_doc = tipo_doc;
    }

    public String getNombres() {
        return nombres;
    }

    public void setNombres(String nombres) {
        this.nombres = nombres;
    }

    public String getApellidos() {
        return apellidos;
    }

    public void setApellidos(String apellidos) {
        this.apellidos = apellidos;
    }

    public String getUsuario() {
        return usuario;
    }

    public void setUsuario(String usuario) {
        this.usuario = usuario;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public int getTelefono() {
        return telefono;
    }

    public void setTelefono(int telefono) {
        this.telefono = telefono;
    }

    public int getCelular() {
        return celular;
    }

    public void setCelular(int celular) {
        this.celular = celular;
    }

    public int getIdentificacion() {
        return identificacion;
    }

    public void setIdentificacion(int identificacion) {
        this.identificacion = identificacion;
    }

    public BasicDao getBasicDao() {
        return basicDao;
    }

    public void setBasicDao(BasicDao basicDao) {
        this.basicDao = basicDao;
    }
    
}
