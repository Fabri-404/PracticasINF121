import math

class Estadistica:
    def __init__(self, numeros):
        self.numeros = numeros

    def promedio(self):
        return sum(self.numeros) / len(self.numeros)

    def desviacion(self):
        prom = self.promedio()
        suma = sum((x - prom) ** 2 for x in self.numeros)
        return math.sqrt(suma / (len(self.numeros) - 1))

def main():
    numeros = list(map(float, input("Ingrese 10 numeros: ").split()))
    
    if len(numeros) != 10:
        print("Error")
        return

    stats = Estadistica(numeros)
    print(f"El promedio es {stats.promedio():.2f}")
    print(f"La desviacion  es {stats.desviacion():.6f}")

main()
