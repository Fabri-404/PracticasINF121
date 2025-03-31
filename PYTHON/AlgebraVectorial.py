class AlgebraVectorial:
    def __init__(self, vector_a, vector_b):
        self._vector_a = vector_a  
        self._vector_b = vector_b 
    # Método auxiliar
    def _producto_punto(self, a, b):
        return sum(x * y for x, y in zip(a, b))
    # Método auxiliar
    def _magnitud(self, vector):
        return (sum(x**2 for x in vector)) ** 0.5
    # a)
    def perpendicular_1(self):
        suma = [self._vector_a[i] + self._vector_b[i] for i in range(len(self._vector_a))]
        resta = [self._vector_a[i] - self._vector_b[i] for i in range(len(self._vector_a))]
        return suma == resta
    # b) 
    def perpendicular_2(self):
        resta_ab = [self._vector_a[i] - self._vector_b[i] for i in range(len(self._vector_a))]
        resta_ba = [self._vector_b[i] - self._vector_a[i] for i in range(len(self._vector_a))]
        return resta_ab == resta_ba
    # c)
    def perpendicular_3(self):
        return self._producto_punto(self._vector_a, self._vector_b) == 0
    # d)
    def perpendicular_4(self):
        suma = [self._vector_a[i] + self._vector_b[i] for i in range(len(self._vector_a))]
        magnitud_suma = self._magnitud(suma) ** 2
        magnitud_a = self._magnitud(self._vector_a) ** 2
        magnitud_b = self._magnitud(self._vector_b) ** 2
        return magnitud_suma == magnitud_a + magnitud_b
    # e)
    def paralela_1(self):
        if self._magnitud(self._vector_b) == 0:  
            return False
        # Verificar si los vectores son proporcionales
        r = self._vector_a[0] / self._vector_b[0] if self._vector_b[0] != 0 else None
        for i in range(1, len(self._vector_a)):
            if self._vector_b[i] == 0:
                if self._vector_a[i] != 0:
                    return False
            else:
                if r is None or self._vector_a[i] / self._vector_b[i] != r:
                    return False
        return True
    # f) 
    def paralela_2(self):
        if len(self._vector_a) == 2: 
            cruzado = self._vector_a[0] * self._vector_b[1] - self._vector_a[1] * self._vector_b[0]
            return cruzado == 0
        return False  
    # g)
    def proyeccion_de_a_sobre_b(self):
        producto_punto = self._producto_punto(self._vector_a, self._vector_b)
        magnitud_b_cuadrado = self._magnitud(self._vector_b) ** 2
        if magnitud_b_cuadrado == 0: 
            return [0] * len(self._vector_a)
        factor = producto_punto / magnitud_b_cuadrado
        return [factor * x for x in self._vector_b]
    # h)
    def componente_de_a_en_b(self):
        producto_punto = self._producto_punto(self._vector_a, self._vector_b)
        magnitud_b = self._magnitud(self._vector_b)
        if magnitud_b == 0:  
            return 0
        return producto_punto / magnitud_b

if __name__ == "__main__":
    #a = [1, 2] 
    #b = [2, 4]  
    a = list(map(float, input("Ingrese los elementos del vector a separados por espacios: ").split()))
    b = list(map(float, input("Ingrese los elementos del vector b separados por espacios: ").split()))
    algebra = AlgebraVectorial(a, b)
 
    print("a) Perpendicular", algebra.perpendicular_1())
    print("b) Perpendicular", algebra.perpendicular_2())
    print("c) Perpendicular", algebra.perpendicular_3())
    print("d) Perpendicular", algebra.perpendicular_4())
    print("e) Paralela", algebra.paralela_1())
    print("f) Paralela", algebra.paralela_2())
    print("g) Proyección de a sobre b:", algebra.proyeccion_de_a_sobre_b())
    print("h) Componente de a en la dirección de b:", algebra.componente_de_a_en_b())