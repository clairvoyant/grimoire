
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {


    public static void main(String[] args) {

        String[] strings= { "1 uno", 
                      "2\t\tdos"
                      };

        // first do with the normal string. 
        for (String s: strings) {


            System.out.print("before [" + s);
            String s2 = s.replaceAll("(\\w+)\\s+(\\w+)", "$2,$1");
            System.out.println("] after  [" + s2 + "]");

        }

        // second do with a precompiled pattern.
        Pattern pattern = Pattern.compile( "(\\w+)\\s+(\\w+)");
        for (String s: strings) {
            Matcher matcher = pattern.matcher(s);
            System.out.print("before [" + s);
            String s2 = matcher.replaceAll("$2,$1");
            System.out.println("] after  [" + s2 + "]");


        }
    }
/*
TODO

string.matches
string.replaceAll
string.replaceFirst
*/




}
