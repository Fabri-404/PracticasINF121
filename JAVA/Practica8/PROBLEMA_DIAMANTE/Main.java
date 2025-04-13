package JAVA.Practica8.PROBLEMA_DIAMANTE;

import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Valor para x: ");
        int x = scanner.nextInt();
        System.out.print("Valor para y: ");
        int y = scanner.nextInt();
        System.out.print("Valor para z: ");
        int z = scanner.nextInt();
        D objeto = new D(x, y, z);
        System.out.println("--------------------------");
        objeto.x += 1;
        objeto.z += 1;
        System.out.println("IncrementaXZ:");
        System.out.println("x: " + objeto.x + ", y: " + objeto.y + ", z: " + objeto.z);
        System.out.println("--------------------------");
        objeto.y += 1;
        objeto.z += 1;
        System.out.println("\nIncrementaYZ:");
        System.out.println("x: " + objeto.x + ", y: " + objeto.y + ", z: " + objeto.z);
        System.out.println("--------------------------");
        System.out.println("IncrementaXYZ:");
        objeto.incrementaXYZ();
        System.out.println("x: " + objeto.x + ", y: " + objeto.y + ", z: " + objeto.z);
        scanner.close();
    }
}
