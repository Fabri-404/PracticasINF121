import math
class area:

        
    def circulo(self,radio):
        return math.pi * radio * radio

    def rectangulo(self, base, altura):
        return base * altura

    def triàngulo_rect(self, base, altura):
        return (base * altura)/2

    def trapecio(self, a, base, altura):
        return ((a + base)/2) * altura

    def pentagono(self, perimetro, apotema):
        return 3 * perimetro * apotema


f1 = area()
f2 = area()
f3 = area()
f4 = area()
f5 = area()

print("circulo: ",f1.circulo(5))
print("rectangulo: ",f2.rectangulo(4.0,6.0))
print("triàngulo rect: ",f3.triàngulo_rect(5.3,3.1))
print("trapecio: ",f4.trapecio(8,8,4))
print("hexagono: ",f5.pentagono(6.6,9.9))