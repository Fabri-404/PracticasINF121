package JAVA.Practica8.PROBLEMA_DIAMANTE;

public class D extends A {
    public int y;
    public D(int x, int y, int z) {
        super(x, z);
        this.y = y;
    }
    public void incrementaXYZ() {
        this.x += 1;
        this.y += 1;
        this.z += 1;
    }
}
