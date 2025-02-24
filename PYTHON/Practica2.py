import math
#Importamos la libreria math para poder hacer operaciones matematicas y poder agregar graficos
#Esta clase es la clase punto
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coord_cartesianas(self):
        return self.x, self.y

    def coord_polares(self):
        radio = math.sqrt(self.x * self.x + self.y * self.y)
        angulo = math.atan(self.y / self.x)
        angulo = math.degrees(angulo)
        return radio, angulo

    def __str__(self):
        return "({:.2f},{:.2f})".format(self.x, self.y)
#Esta es la clase circulo 
class Circulo:
    def __init__(self, centro, radio):
        if not isinstance(centro, Punto):
            raise TypeError("El centro debe ser un objeto de la clase Punto")
        if radio <= 0:
            raise ValueError("El radio debe ser un valor positivo")
            
        self.centro = centro
        self.radio = radio

    def __str__(self):
        return "Centro: {}, Radio: {:.2f}".format(self.centro, self.radio)

    def dibujaCirculo(self):
        print(f"Dibujando un círculo con centro en {self.centro} y radio {self.radio}")

# Ejemplo de uso para la clase Punto:
p1 = Punto(0, 3)
print(p1)
x, y = p1.coord_cartesianas()
print(f"x: {x}, y: {y}")
r, a = p1.coord_polares()
print(f"r: {r}, a: {a}")
# Ejemplo de uso para la clase Circulo:

punto_centro = Punto(2, 3)
circulo = Circulo(punto_centro, 5)
print(circulo)
circulo.dibujaCirculo()