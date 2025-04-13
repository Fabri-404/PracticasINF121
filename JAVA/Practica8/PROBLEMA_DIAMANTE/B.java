package JAVA.Practica8.PROBLEMA_DIAMANTE;

public class B extends C {
    public int y;
    public B(int y, int z) {
        super(z);
        this.y = y;
    }
    public void incrementaYZ() {
        this.y += 1;
        this.z += 1;
    }
    public void incrementaZ() {
        this.z += 1;
    }
}