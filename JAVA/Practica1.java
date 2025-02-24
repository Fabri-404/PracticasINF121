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

    public static void main(String[] args) {
        Punto p1 = new Punto(0, 3);
        System.out.println(p1);
        double[] cartesianas = p1.coordCartesianas();
        System.out.printf("x: %.2f, y: %.2f%n", cartesianas[0], cartesianas[1]);
        double[] polares = p1.coordPolares();
        System.out.printf("r: %.2f, a: %.2f%n", polares[0], polares[1]);
    }
}