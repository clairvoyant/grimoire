


import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.Files;
import java.nio.charset.Charset;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Map;
import java.util.HashMap;

public class Main {

    public static void usage(String log) {

          if (log.length()>0) {
              System.out.println(log);
          }
          System.out.println("usage:\n program FILENAME");

          System.exit(-1);


    }

    public static void main(String[] args) {

        Path file = Paths.get(args[0]);

        if (Files.isReadable(file)) {

            try {
                Charset charset = Charset.defaultCharset();
                BufferedReader reader = Files.newBufferedReader(file, charset);
                String line = null;
                Map<String, String[]> rows = new HashMap<String, String[]>();

                // read the file as a CSV file. 
                // and split each file to index using the first column.
                while ((line = reader.readLine()) != null) {
                    String[] fields = line.split(",");
                    if (fields.length >= 2) {
                       rows.put(fields[0], fields);
                    }
                }
                // read the file as a CSV file. 
                // and split each file to index using the first column.
                for (Map.Entry<String, String[]> e : rows.entrySet()) {
                    System.out.println(e.getKey() + ": " + e.getValue());
                    for (String field: e.getValue()) { 
                        System.out.println("\t" + field); 
                    }  
                }
            } catch (IOException x) {
                System.err.format("IOException: %s%n", x);
            }

        } else {
           usage("error: file not found.");
        }
    }

}
