package JAVA.Practica8;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Valor para x: ");
        int x = input.nextInt();
        System.out.print("Valor para y: ");
        int y = input.nextInt();
        System.out.print("Valor para z: ");
        int z = input.nextInt();
        D objeto = new D(x, y, z);
        System.out.println("----------------------------");
        objeto.x += 1;
        objeto.z += 1;
        System.out.println("IncrementaXZ:");
        System.out.println("x: " + objeto.x + ", y: " + objeto.y + ", z: " + objeto.z);
        System.out.println("----------------------------");
        objeto.y += 1;
        objeto.z += 1;
        System.out.println("IncrementaYZ:");
        System.out.println("x: " + objeto.x + ", y: " + objeto.y + ", z: " + objeto.z);
        objeto.incrementaXYZ();
        System.out.println("----------------------------");
        System.out.println("IncrementaXYZ:");
        System.out.println("x: " + objeto.x + ", y: " + objeto.y + ", z: " + objeto.z);
    }
}
