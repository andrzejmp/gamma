using System;
class Triangle {
  
  static bool checkTriangle(double a, double b, double c)    
  {
      if((a<b+c) && (b<a+c) && (c<a+b))
      {
          return true;
      }
      else
      {
          return false;
      }
  }
  
    
  static void Main() {
      double a = 3;
      double b = 4;
      double c = 5;
      if(checkTriangle(a,b,c))
      {
          Console.WriteLine("You can build a triangle with sides {0}, {1}, {2}.", a,b,c);
          if ((a*a == b*b + c*c) || (b*b == a*a + c*c) || (c*c == b*b + a*a))
          {
              Console.WriteLine("It is a rectangular triangle.");
          }
      }
      else
      {
          Console.WriteLine("You can not build a triangle with sides {0}, {1}, {2}.", a,b,c);
      }
    
  }
}