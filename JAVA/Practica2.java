import java.lang.Math;

class Punto {
    private double x;
    private double y;

    public Punto(double x, double y) {
        this.x = x;
        this.y = y;
    }

    public double[] coordCartesianas() {
        return new double[]{x, y};
    }

    public double[] coordPolares() {
        double radio = Math.sqrt(x * x + y * y);
        double angulo = Math.toDegrees(Math.atan2(y, x));
        return new double[]{radio, angulo};
    }

    @Override
    public String toString() {
        return String.format("(%.2f, %.2f)", x, y);
    }
}

class Circulo {
    private Punto centro;
    private double radio;

    public Circulo(Punto centro, double radio) {
        if (radio <= 0) {
            throw new IllegalArgumentException("El radio debe ser un valor positivo");
        }
        this.centro = centro;
        this.radio = radio;
    }

    @Override
    public String toString() {
        return String.format("Centro: %s, Radio: %.2f", centro, radio);
    }

    public void dibujaCirculo() {
        System.out.printf("Dibujando un círculo con centro en %s y radio %.2f%n", centro, radio);
    }

    public static void main(String[] args) {
        Punto puntoCentro = new Punto(2, 3);
        Circulo circulo = new Circulo(puntoCentro, 5);
        System.out.println(circulo);
        circulo.dibujaCirculo();
    }
}