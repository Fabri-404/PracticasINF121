public class FiguraGeometrica {
    //circulo
    double areaCirculo(double radio) {
        return Math.PI * radio * radio;
    }
    //rectagulo
    double areaRectangulo(double base, double altura) {
        return base * altura;
    }
    //triangulo
    double areaTriangulo(double base, double altura) {
        return (base * altura) / 2;
    }
    //trapecio
    double areaTrapecio(double baseMayor, double baseMenor, double altura) {
        return ((baseMayor + baseMenor) * altura) / 2;
    }
    //hexagono
    double areaHexagono(double lado) {
        return (3 * Math.sqrt(3) * lado * lado) / 2;
    }

    public static void main(String[] args) {
        FiguraGeometrica f1 = new FiguraGeometrica(); 
        FiguraGeometrica f2 = new FiguraGeometrica(); 
        FiguraGeometrica f3 = new FiguraGeometrica(); 
        FiguraGeometrica f4 = new FiguraGeometrica(); 
        FiguraGeometrica f5 = new FiguraGeometrica(); 

        System.out.println("Círculo: " + f1.areaCirculo(5));
        System.out.println("Rectángulo: " + f2.areaRectangulo(4, 6));
        System.out.println("Triangulo: " + f3.areaTriangulo(5, 3));
        System.out.println("Trapecio: " + f4.areaTrapecio(8, 5, 4));
        System.out.println("Hexagono: " + f5.areaHexagono(6));
    }
}
// Univ. Fabricio Oliver Echeverria Poma 
