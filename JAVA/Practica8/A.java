package JAVA.Practica8;
public class A {
    public int x;
    public int z;

    public A(int x, int z) {
        this.x = x;
        this.z = z;
    }
    public void incrementaXZ() {
        this.x += 1;
        this.z += 1;
    }

    public void incrementaZ() {
        this.z += 1;
    }
}