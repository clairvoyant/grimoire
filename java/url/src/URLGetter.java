
import java.util.Scanner;

import org.apache.log4j.Logger;
import org.apache.log4j.BasicConfigurator;


import java.io.*;
import java.net.*;

public class URLGetter {

    public String getHTML(String urlToRead) {
        URL url;
        HttpURLConnection conn;
        BufferedReader rd;
        String line;
        String result = "";
        try {
            url = new URL(urlToRead);
            conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");
            rd = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            while ((line = rd.readLine()) != null) {
                result += line;
            }
            rd.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return result;
    }

    public static void main(String args[])
    {
        URLGetter  getter = new URLGetter();
        System.out.println(getter.getHTML(args[0]));
    }
}
