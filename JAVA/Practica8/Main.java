package JAVA.Practica8;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Valor para x:");
        int x = scanner.nextInt();
        System.out.println("Valor para y:");
        int y = scanner.nextInt();
        System.out.println("Valor para z:");
        int z = scanner.nextInt();

        D objeto = new D(x, y, z);

        System.out.println("Valores iniciales:");
        System.out.println(objeto);
        System.out.println("\nIncrementaXZ:");
        objeto.incrementaXZ();
        System.out.println(objeto);
        System.out.println("\nIncrementaYZ:");
        objeto.incrementaYZ();
        System.out.println(objeto);
        System.out.println("\nIncrementaXYZ:");
        objeto.incrementaXYZ();
        System.out.println(objeto);

        scanner.close();
    }
}