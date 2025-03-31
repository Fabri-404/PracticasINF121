import math

def promedio(numeros):
    return sum(numeros) / len(numeros)

def desviacion(numeros, prom):
    suma = sum((x - prom) ** 2 for x in numeros)
    return math.sqrt(suma / (len(numeros) - 1))

def main():
    numeros = list(map(float, input("Ingrese 10 numeros: ").split()))
    
    if len(numeros) != 10:
        print("Error")
        return
    
    prom = promedio(numeros)
    desv = desviacion(numeros, prom)

    print(f"El promedio es {prom:.2f}")
    print(f"La desviacion  es {desv:.6f}")

main()
