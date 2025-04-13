package JAVA.Practica8.PROBLEMA_DIAMANTE;

public class A extends C {
    public int x;
    public A(int x, int z) {
        super(z);
        this.x = x;
    }
    public void incrementaXZ() {
        this.x += 1;
        this.z += 1;
    }
    public void incrementaZ() {
        this.z += 1;
    }
}
