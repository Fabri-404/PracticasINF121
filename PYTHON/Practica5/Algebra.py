import math
class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def obtenerDiscriminante(self):
        """Calcula el discriminante b^2 - 4ac"""
        return self.b ** 2 - 4 * self.a * self.c

    def obtenerRaiz1(self):
        """Aqui Calcula la primera raiz de la ecuacion"""
        discriminante = self.obtenerDiscriminante()
        if discriminante >= 0:
            return (-self.b + math.sqrt(discriminante)) / (2 * self.a)
        else:
            return None  

    def obtenerRaiz2(self):
        """Aqui Calcula la segunda raiz de la ecuacion"""
        discriminante = self.obtenerDiscriminante()
        if discriminante >= 0:
            return (-self.b - math.sqrt(discriminante)) / (2 * self.a)
        else:
            return None 

if __name__ == "__main__":
    # Solicita datos
    a = float(input("Ingrese a: "))
    b = float(input("Ingrese b: "))
    c = float(input("Ingrese c: "))
    
    ecuacion = EcuacionCuadratica(a, b, c)
    discriminante = ecuacion.obtenerDiscriminante()
    
    if discriminante > 0:
        raiz1 = ecuacion.obtenerRaiz1()
        raiz2 = ecuacion.obtenerRaiz2()
        print(f"La ecuacion tiene dos raices: {raiz1} y {raiz2}")
    elif discriminante == 0:
        raiz = ecuacion.obtenerRaiz1()
        print(f"La ecuacion tiene una raiz: {raiz}")
    else:
        print("La ecuacion no tiene raices reales.")


        