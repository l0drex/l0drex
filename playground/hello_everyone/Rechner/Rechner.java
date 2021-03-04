import java.util.Scanner;

class Rechner {
  // Anfang Attribute
  static double ergebnis, a, b;
  static int fehlercode;
  static boolean fehler = false;
  // Ende Attribute

  // Anfang Methoden
  static double Addition (double a, double b){
    double c = a + b;
    return c;
  }
  
  static double Subtraktion (double a, double b){
    double c = a - b;
    return c;
  }            
  
  static double Multiplikation (double a, double b){
    double c = a * b;
    return c;
  }
  
  static double Division (double a, double b){
    double c = a / b;
    return c;
  }
  
  public static void main (String [] args){
    Scanner s = new Scanner(System.in);
    
    System.out.println("Zahl a:");
    double a = s.nextDouble();
    
    System.out.println("Zahl b:");
    double b = s.nextDouble();
    
    System.out.println("Rechenart ( + | - | * | / ): ");
    char rechenart = s.next().charAt(0);

    s.close();
    
    //    String rechnung = s.next();
    //    
    //    for (int i = 0; i<rechnung.word.length(); i++) {
    //      if (rechnung.charAt(i)) {
    //        
    //      } // end of if
    //      } // end of switch
    //      
    //    } // end of for
    
    System.out.println("------------");
    
    switch (rechenart) {
      case '+': 
        System.out.println(Addition(a, b));
        break;
        
      case '-': 
        System.out.println(Subtraktion(a, b));
        break;
        
      case '*':
        System.out.println(Multiplikation(a, b));
        break;
        
      case '/':
        System.out.println(Division(a, b));
        break;
        
      case ':' :
        fehler = true;
        fehlercode = 1;
        break;
        
      case '.' : 
        fehler = true;
        fehlercode = 2;
        break;
        
      default: 
        fehler = true;
        fehlercode = 0;
        
    } // end of switch
    
    if (fehler == true) {
      System.out.println("ERROR!");
      System.out.println("");
      
      boolean fbz = false;
      while (fbz == false) { 
        Scanner fb_s = new Scanner(System.in);  //Fehlerbestimmung
        System.out.println("N�here Fehlerbestimmung? (j/n)");
        char fb = fb_s.next().charAt(0);
        fb_s.close();
        System.out.println("");
        
        switch (fb) {
          case 'j' : 
            fbz=true;
            System.out.println("Fehlercode: " + fehlercode);
            switch (fehlercode) {
              case 0 :
                System.out.println("unzul�ssiges Zeichen");
                break;
                
              case 1 : 
                System.out.println("Bitte nutzen Sie '/' statt ':'");
                break;
                
              case 2: 
                System.out.println("Bitte nutzen Sie '*' statt '.'");
                break;
                
            } // end of switch
            break;
            
          case 'n' : 
            fbz = true;
            break;
            
          default: 
            fbz = false;
            
        } // end of switch
      } // end of while
    } // end of if
  }
    // Ende Methoden
}