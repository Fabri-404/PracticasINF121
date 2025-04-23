

import java.awt.Color;

public class Carro implements Coloreado {
    private Color color;

    public Carro(Color color) {
        this.color = color;
    }

    public Color getColor() {
        return this.color;
    }

    public static void main(String[] args) {
        Carro carro = new Carro(Color.GRAY);
        System.out.println("El carro es: " + carro.getColor());
    }
}