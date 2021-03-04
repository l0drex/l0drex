package javatests;

class math{

    int fakultät(int a) {
        if (a > 1) {
            a *= fakultät(a-1);
        } else {
            return 1;
        }
        return a;
    }

    int quersumme(int inpQuer){
        int sum = 0;
        while (inpQuer>0) {
            sum+= inpQuer % 10;
            inpQuer/=10;
        }
        return sum;
    }

    //geometry

    static double b, l, h;
    double A, V, e;
  
    static double Volume(){
        return b*l*h;
    }

    static double surfaceArea(){
        return 2 * (b *l + l * h + b * h);
    }

    static double diagonal(){
        return Math.sqrt(Math.pow(b,2)+Math.pow(l, 2)+Math.pow(h,2));
    }

    void calculate(double b, double l, double h){
    
        V = Volume();
        A = surfaceArea();
        e = diagonal();
    }

    void view(){
        System.out.println("Volume: " + "V/n" + "Surface: " + "A/n" + "Diagonal: " + "e");
    }

    //folgen

    String calculateFibonacciRow(int length) {
        int[] fib = new int[length]; //Array der Länge 30 -> 30 Zahlen werden berechne
        String fibStr = ""; //String zur Ausgabe

        fib[0] = 0;
        fib[1] = 1; //Deklaration der Anfangszahlen

        for (int i = 2; i<fib.length; i++){
            fib[i]=fib[i-1]+fib[i-2];
        }

        for (int fibEl: fib) {
            fibStr += Integer.toString(fibEl) + "\n";
        }

        return fibStr;
    }

    void FizzBuzz(int max){
        for (int i = 1; i <= max; i++) {
            if ((i % 3) == 0) {
                System.out.println("fizz");
            } else {
                if ((i % 5) == 0) {
                    System.out.println("buzz");
                } else {
                    if ((i % 3) == 0 && (i % 5) == 0) {
                    System.out.println("fizzbuzz");
                    } else {
                        System.out.println(i);
                    }
                }
            }
        }
    }
}