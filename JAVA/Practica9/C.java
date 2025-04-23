public class C implements I {
    public void m1() {
        System.out.println("Primera implementacion en C");
    }

    public void m2() {
        System.out.println("Segunda implementacion en C");
    }

    public static void main(String[] args) {
        C objeto = new C();
        objeto.m1();
        objeto.m2();
    }
}