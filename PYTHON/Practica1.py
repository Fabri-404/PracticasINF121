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

# Ejemplo de uso:
p1 = Punto(0, 3)
print(p1)
x, y = p1.coord_cartesianas()
print(f"x: {x}, y: {y}")
r, a = p1.coord_polares()
print(f"r: {r}, a: {a}")
