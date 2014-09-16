
public class VarArgs 
{
 
    public static void main(String[] args)
    {
        int n1 = 1;
        int n2 = 2;
        int n3 = 3;

        System.out.println(max(n1, n2, n3));
    }

    public static int max(int ... values) 
    {
       int result =     Integer.MIN_VALUE ;

       for (int n: values) {
          if (n>result) {
             result = n;
          }

      }

      return result;

    }


}
