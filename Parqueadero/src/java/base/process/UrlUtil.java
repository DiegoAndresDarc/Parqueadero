/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package base.process;

import java.util.regex.Pattern;

/**
 *
 * @author Lord_Nightmare
 */
public class UrlUtil {

    public static String getClassName(String url, boolean type) {
        String[] parts = url.split(Pattern.quote("/"));
        if (parts.length > 1) {
            if (type) {
                return "business.logic." + ((!parts[2].contains("Controller"))?
                         parts[2] + "Controller":parts[2]);
            } else {
                return "business.entities." + parts[2];
            }
        }
        return null;
    }

    public static String getMethodName(String servletPath) {
        String[] parts = servletPath.split(Pattern.quote("/"));
        if (parts.length > 1) {
            String method = parts[3];
            return method;
        }
        return null;
    }
}
