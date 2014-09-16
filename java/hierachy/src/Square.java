


public class Square extends Shape implements Operations
{
     int x;
     int y;
     int len;

     public Square(String name_, int x, int y, int len) {
        super(name_);
     
        System.out.println("Square: " + super.toString());
     
     }
     
     
     @Override // ensure there is an exact match.... 
     public void rotate(int angle) {
        System.out.println("Square rotate: " + super.toString());
     
     
     };

    public void crop(int len) { 
        System.out.println("Square crop: " + super.toString());
    }
}
