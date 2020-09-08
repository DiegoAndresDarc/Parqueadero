/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package logic.objects;

import base.dao.BasicDao;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

/**
 *
 * @author Brian Botina
 */
public class Usuario {

    private String id,tipo_doc, nombres, apellidos, usuario, password, email, tipo_usuario;
    private long telefono, celular, identificacion;
    private short sancionado, al_dia;
    private BasicDao basicDao;
    private HashMap<String, String> data;
    private ArrayList<Vehiculo> vehiculos;
    private ArrayList<Parqueadero> parqueaderos;

    public Usuario(HashMap<String, String> data) {
        this.data = data;
        fillData();
        basicDao = new BasicDao(tipo_usuario);
        vehiculos = new ArrayList<>();
        parqueaderos = new ArrayList<>();
    }

    private void fillData() {
        id = data.get("id");
        tipo_doc = data.get("tipo_identificacion");
        nombres = data.get("nombres");
        apellidos = data.get("apellidos");
        usuario = data.get("usuario");
        password = data.get("password");
        email = data.get("email");
        tipo_usuario = data.get("tipo_usuario");
        telefono = Long.parseLong(data.get("telefono"));
        celular = Long.parseLong(data.get("celular"));
        identificacion = Long.parseLong(data.get("identificacion"));
        sancionado = Short.parseShort(data.get("sancionado"));
        al_dia = Short.parseShort(data.get("al_dia"));
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getTipo_usuario() {
        return tipo_usuario;
    }

    public void setTipo_usuario(String tipo_usuario) {
        this.tipo_usuario = tipo_usuario;
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

    public long getTelefono() {
        return telefono;
    }

    public void setTelefono(int telefono) {
        this.telefono = telefono;
    }

    public long getCelular() {
        return celular;
    }

    public void setCelular(int celular) {
        this.celular = celular;
    }

    public long getIdentificacion() {
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
