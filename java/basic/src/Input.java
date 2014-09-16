
import java.util.Scanner;

import org.apache.log4j.Logger;
import org.apache.log4j.BasicConfigurator;


public class Input
{
   static Logger logger = Logger.getLogger(Input.class);
   
   public static void main(String[] args)
   {
      BasicConfigurator.configure(); // log4j needed. 

      Scanner input = new Scanner(System.in);

      double d1 = input.nextDouble();
      double d2 = input.nextDouble();


      String s = "value: " + d1 + " * " + d2 + " = " + d1 * d2;
      System.out.println(s);
      logger.info(s); //log4j usage

      


   }


};
