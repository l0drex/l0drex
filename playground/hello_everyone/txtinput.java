package javatests;
import java.io.*;
import java.util.Scanner;

class txtinput {

    String bufferedReader() {
        String s = "";
        System.out.println("Bitte Text eingeben und mit Enter abschliessen:" + System.getProperty("line.separator"));

        try {
        BufferedReader ein = new BufferedReader(new InputStreamReader(System.in));
        s = ein.readLine();
        System.out.println("Du hast eingegeben:" + System.getProperty("line.separator") + s);
        } catch (IOException ioe) {
        ioe.printStackTrace();
        }
        
        return s;
    }

    String scanner() {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.next();
        scanner.close();
        return s;
    }
}