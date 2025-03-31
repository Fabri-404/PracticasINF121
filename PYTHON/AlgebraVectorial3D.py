import math

class AlgebraVectorial3D:
    def __init__(self, vector_a, vector_b):
        self._vector_a = vector_a  
        self._vector_b = vector_b 

    def __add__(self, other):
        if not isinstance(other, AlgebraVectorial3D):
            raise ValueError("El operando debe ser un objeto de AlgebraVectorial3D")
        return [self._vector_a[i] + other._vector_b[i] for i in range(3)]
    
    def __mul__(self, r):
        if not isinstance(r, (int, float)):
            raise ValueError("El operando debe ser un número (escalar)")
        return [r * x for x in self._vector_a]

    def __abs__(self):
        return math.sqrt(sum(x**2 for x in self._vector_a))

    def normal(self):
        magnitud = abs(self) 
        if magnitud == 0: 
            return [0, 0, 0]
        return [x / magnitud for x in self._vector_a]

    def producto_escalar(self):
        return sum(self._vector_a[i] * self._vector_b[i] for i in range(3))

    def producto_vectorial(self):
        a1, a2, a3 = self._vector_a
        b1, b2, b3 = self._vector_b
        return [
            a2 * b3 - a3 * b2, a3 * b1 - a1 * b3, a1 * b2 - a2 * b1 
        ]
    def son_perpendiculares(self):
        diagonal1 = [self._vector_a[i] + self._vector_b[i] for i in range(3)]
        diagonal2 = [self._vector_a[i] - self._vector_b[i] for i in range(3)]
        longitud_diag1 = math.sqrt(sum(x**2 for x in diagonal1))
        longitud_diag2 = math.sqrt(sum(x**2 for x in diagonal2))
        return abs(longitud_diag1 - longitud_diag2) < 1e-10
    def obt_vector_a(self):
        return self._vector_a

    def obt_vector_b(self):
        return self._vector_b

def ingresar_vector(nombre):
    print(f"Ingrese las 3 componentes del vector {nombre} (separadas por espacios, ej: 1 2 3):")
    try:
        componentes = list(map(float, input().split()))
        if len(componentes) != 3:
            raise ValueError("El vector debe tener exactamente 3 componentes.")
        return componentes
    except ValueError as e:
        print(f"Error: {e}. Intente de nuevo.")
        return ingresar_vector(nombre)

if __name__ == "__main__":
    a = ingresar_vector("a")
    b = ingresar_vector("b")

    algebra1 = AlgebraVectorial3D(a, [0, 0, 0])  
    algebra2 = AlgebraVectorial3D([0, 0, 0], b)  
    algebra = AlgebraVectorial3D(a, b)  

    print("a) Suma de a y b:", algebra1 + algebra2)
    print("b) Multiplicación de a por un escalar (r=2):", algebra1 * 2)
    print("c) Longitud de a:", abs(algebra1))
    print("d) Normal de a:", algebra1.normal())
    print("e) Producto escalar de a y b:", algebra.producto_escalar())
    print("f) Producto vectorial de a y b:", algebra.producto_vectorial())
    print("Es perpendicular", (algebra.son_perpendiculares()))



    