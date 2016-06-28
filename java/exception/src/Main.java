
import java.util.InputMismatchException;
import java.util.Scanner;



public class Main {

    public static int compare(int n1, int n2) throws ArgumentNotValidException 
    {
        if ( (n1<0) || (n2 <0)) {
           throw new ArgumentNotValidException();
        }

        return n1 - n2;
    }

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);


        try {

            int n1 = scanner.nextInt();
            int n2 = scanner.nextInt();

            System.out.println("Comparing: " + compare(n1, n2));
        } catch (InputMismatchException e) {
            System.err.printf("Error: in scan: " + e);
            // get stack tracke
            StackTraceElement[] strace = e.getStackTrace(); 
            for (StackTraceElement element: strace) {
               System.out.printf("%s\t", element.getClassName());
               System.out.printf("%s\t", element.getFileName());
               System.out.printf("%s\t", element.getLineNumber());
               System.out.printf("%s\n", element.getMethodName());
            
            }
        } catch (ArgumentNotValidException e) {
            System.err.printf("Error: in operation:  "+ e);
        } finally {
            System.out.printf("finally: ... the end...");
        }

    }
}
