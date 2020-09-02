/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package base.persistence.connection;

import java.io.IOException;
import java.io.InputStream;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.Properties;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author Brian Botina
 */
public class DBConnection {

    static int nconn = 0;
    static Properties databasProperties = new Properties();

    protected void setGeneralProperties() {
        try {
            ClassLoader classLoader = Thread.currentThread().getContextClassLoader();
            InputStream input = classLoader.getResourceAsStream("properties.properties");
            databasProperties.load(input);
        } catch (IOException ex) {
            Logger.getLogger(DBConnection.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    public static Connection connect(String user_type) {
        DBConnection cn = new DBConnection();
        Connection cnn = null;
        cn.setGeneralProperties();
        String user = databasProperties.getProperty("mysql_" + user_type + "_user");
        String password = databasProperties.getProperty("mysql_" + user_type + "_password");
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            cnn = DriverManager.getConnection(
                    databasProperties.getProperty("mysql_url"), user, password);
            cnn.setAutoCommit(false);
//            System.out.println(String.valueOf(++nconn) + " abriendo  conexion");

        } catch (ClassNotFoundException | SQLException ex) {
            ex.printStackTrace(System.err);
        }
        return cnn;
    }

    public static void closeConnection(Connection cnn) {
        closeConnection(cnn, null);
    }

    public static void closePreparedStatement(PreparedStatement ps) {
        closeConnection(null, ps);
    }

    private static void closeConnection(Connection cnn, PreparedStatement ps) {
        try {
            if (ps != null) {
                ps.close();
            }
            if (cnn != null) {
                cnn.close();
//                System.out.println(String.valueOf(nconn--) + " cerrando  conexion");

            }
        } catch (SQLException e) {
            e.printStackTrace(System.err);
        }
    }

    public static void rollBack(Connection cnn) {
        try {
            cnn.rollback();
        } catch (SQLException e) {
            e.printStackTrace(System.err);
        }
    }

    public static boolean checkConnection(Connection cnn) {
        boolean connection = false;
        try {
            if (cnn != null) {
                connection = cnn.isClosed();
            }
        } catch (SQLException ex) {
            Logger.getLogger(DBConnection.class.getName()).log(Level.SEVERE, null, ex);
        }
        return connection;
    }

    public static boolean checkPreparedStatement(PreparedStatement ps) {
        boolean connection = false;
        try {
            if (ps != null) {
                connection = ps.isClosed();
            }

        } catch (SQLException ex) {
            Logger.getLogger(DBConnection.class.getName()).log(Level.SEVERE, null, ex);
        }
        return connection;
    }
}
