/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package servlet;

import base.dao.BasicDao;
import base.process.UrlUtil;
import com.google.gson.Gson;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

/**
 *
 * @author Brian Botina
 */
@WebServlet(name = "MainServlet", urlPatterns = {"/MainServlet/*"})
public class MainServlet extends HttpServlet {

    /**
     * Processes requests for both HTTP <code>GET</code> and <code>POST</code>
     * methods.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.addHeader("Access-Control-Allow-Origin", "*");
        response.setCharacterEncoding("UTF-8");
        response.setContentType("application/json");
        PrintWriter out = response.getWriter();
        String body, action;
        Gson gson = new Gson();
        action = UrlUtil.getMethodName(request.getRequestURI());
        Object object = null;
        body = request.getReader().lines().reduce("", (accumulator, actual) -> accumulator + actual);
        switch (action) {
            case "login":
                //devolver menu y tipo de usuario
                object = true;
                break;
            case "logout":
                request.getSession().invalidate();
                object = true;
                break;
            case "checkSession":
                if (this.checkSession(request.getSession())) {
                    object = true;
                } else {
                    object = false;
                }
                break;
            case "signup":
                String table = (String) request.getSession().getAttribute("tabla");
                HashMap<String, String> data = new HashMap();
                if(table.equals("usuario")){
                data.put("nombres", (String) request.getSession().getAttribute("nombres"));
                data.put("apellidos", (String) request.getSession().getAttribute("apellidos"));
                data.put("usuario", (String) request.getSession().getAttribute("usuario"));
                data.put("password", (String) request.getSession().getAttribute("password"));
                data.put("email", (String) request.getSession().getAttribute("email"));
                data.put("telefono", (String) request.getSession().getAttribute("telefono"));
                data.put("celular", (String) request.getSession().getAttribute("celular"));
                data.put("identificacion", (String) request.getSession().getAttribute("identificacion"));
                data.put("tipo_identificacion", (String) request.getSession().getAttribute("tipo_identificacion"));
                }else if(table.equals("parqueadero")){
                    
                }
                this.insert(table,data);
                break;
            case "recoverPassword":
                break;
            case "getMenu":
                break;
            case "update":
                break;
            case "select":
                break;
            default:
                break;
        }
        out.print(new Gson().toJson(object));
    }
    
    private void insert(String table, HashMap<String,String> data){
        BasicDao basicDao = new BasicDao("r");
        List<String> tables = new ArrayList();
        tables.add(table);
        basicDao.insert(tables, data);
        
    }
    
    private boolean checkSession(HttpSession session) {
//        System.out.println(session.getAttribute("name"));
        return session.getAttribute("names") != null;
    }

    // <editor-fold defaultstate="collapsed" desc="HttpServlet methods. Click on the + sign on the left to edit the code.">
    /**
     * Handles the HTTP <code>GET</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Handles the HTTP <code>POST</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Returns a short description of the servlet.
     *
     * @return a String containing servlet description
     */
    @Override
    public String getServletInfo() {
        return "Short description";
    }// </editor-fold>

}
