class Schoolstory {
  public static void main (String[] args) {

    int note = 4, erfolg=5, erforderliche_lerntage=3; 
    int tag;
    double durchschn;
    String e = "";
    
    erforderliche_lerntage++;
    for (tag=1; tag<erforderliche_lerntage ; tag++) {
      System.out.println("--Tag " + tag + "--");
      System.out.println("Kind: Ich sollte langsam wirklich lernen, wir schreiben morgen eine Arbeit.");
      System.out.println("");
    } // end of for
    System.out.println("--Tag " + tag + "--");
    
    System.out.println("Kind: Mama, wir haben heute eine Arbeit geschrieben.");
    System.out.println("Mutter: Und, was sagt dein Gef�hl?");
    if (tag < 2 && erfolg ==0) {
      System.out.println("Kind: Naja, geht so.");
      } // end of if-else
      else {
        System.out.println("Kind: Joa, ganz gut.");}
    tag++;
    System.out.println("");
    System.out.println("--Tag " + tag + "--");
    switch (note) {
      case 1: e = "Aha."; break;
      case 2: e = "Schoen!"; break;
      case 3: e = "Immerhin."; break;
      case 4: e = "Naja."; break;
      case 5: e = "WAS?!"; break;
      case 6: e = "OH GOTT!"; break;
      default: e= "Das versteh ich nicht.";
    }
    System.out.println("Kind: Mama, ich habe heute eine " + note + " bekommen.");
    System.out.println("Mutter: " + e);
    if (note < 3 && erfolg < 5) {
      System.out.println("Gl�ck gehabt :)");
    } // end of if
    if (note > 4 || note == 4) {
      System.out.println("Daran m�ssen wir was aendern!");
      do {
        note--;
      } while (note>1); // end of do-while
      System.out.println("Lehrer: Sehr schoen. 100 Euro, damit hast du dir die " + note + " wirklich verdient!");    
      System.out.println("");
      tag++;
      System.out.println("--Tag " + tag + "--");
      System.out.println("Kind: Mama, der Lehrer hat die Note ge�ndert!");
      System.out.println("Mutter: Echt? Zeig mal.");
      switch (note) {
        case 1 : 
          e = "sehr schoen!";
          break;
        case 2 : 
          e = "das hoert sich doch schonmal besser an.";
          break;
        default: 
          e = "das verstehe ich jetzt nicht.";
      } // end of switch
      
      System.out.println("Oh! Eine " + note + ", " + e);
      durchschn=(note+1+1+1+3+2)/6;
      System.out.println("Kind: Mein Durchschnitt ist jetzt " + durchschn + ".");
    } // end of if
    System.out.println("________________________________________________________");
  }
}
