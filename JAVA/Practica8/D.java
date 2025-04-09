package JAVA.Practica8;
public class D extends A {
    private B b;
    public D(int x, int y, int z) {
        super(x);
        this.b = new B(y);
        this.z = z;
        this.b.z = z;
    }
    public int getY() {
        return b.y;
    }
    public int getZFromB() {
        return b.z;
    }
    public void incrementaYZ() {
        b.incrementaYZ();
    }
    public void incrementaXYZ() {
        x++;
        b.y++;
        z++;
        b.z++;
    }
    @Override
    public String toString() {
        return "x: " + x + ", y: " + b.y + ", z (from A): " + z + ", z (from B): " + b.z;
    }
}
