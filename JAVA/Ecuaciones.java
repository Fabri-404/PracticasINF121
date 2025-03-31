import java.util.Scanner;

public class Ecuaciones {

    public float getDiscriminante(float a, float b, float c) {
        return (b * b) - 4 * a * c;
    }

    public double getRaiz1(double a, double b, double c) {
        return ((-b)+ Math.sqrt(b * b - 4 * a * c)) / (2 * a);
    }

    public double getRaiz2(double a, double b, double c) {
        return ((-b) - Math.sqrt(b * b - 4 * a * c)) / (2 * a);
    }

    public float[] raices(float a, float b, float c){
        float raices[] = new float[2];
        float d = (b*b)-(4*a*c);
        if(d > 0 && a != 0){
            raices[0] = (-b + (float)Math.sqrt(d))/(2*a);
            raices[1] = (-b - (float)Math.sqrt(d))/(2*a);
        }

        return raices;
    }

    public  static void main(String[] args) {
        Ecuaciones x = new Ecuaciones();
        float a, b, c;
        try (Scanner sc = new Scanner(System.in)) {
            System.out.println("Ingrese a, b, c: ");
            a = Float.parseFloat(sc.nextLine());
            b = Float.parseFloat(sc.nextLine());
            c = Float.parseFloat(sc.nextLine());
            System.out.println("La ecuación tiene una raíz: " + x.getRaiz1(a, b, c));

            float raices[] = x.raices(a, b, c);
            System.out.println("La ecuación tiene dos raíces: " + raices[0] + " y " + raices[1]);
        }
        

        

        
    } 
     
}