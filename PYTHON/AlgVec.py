class AlgebraVectorial:
    def __init__(self, vector_a, vector_b):
        self._vector_a = vector_a  
        self._vector_b = vector_b 

    def _producto_punto(self, a, b):
        return sum(x * y for x, y in zip(a, b))

    def _magnitud(self, vector):
        return (sum(x**2 for x in vector)) ** 0.5

    def _obtener_vectores(self, args):
        if len(args) == 2:  
            return args  
        return self._vector_a, self._vector_b  

    def perpendicular_1(self, *args):
        vector_a, vector_b = self._obtener_vectores(args)
        suma = [vector_a[i] + vector_b[i] for i in range(len(vector_a))]
        resta = [vector_a[i] - vector_b[i] for i in range(len(vector_a))]
        return suma == resta

    def perpendicular_2(self, *args):
        vector_a, vector_b = self._obtener_vectores(args)
        resta_ab = [vector_a[i] - vector_b[i] for i in range(len(vector_a))]
        resta_ba = [vector_b[i] - vector_a[i] for i in range(len(vector_a))]
        return resta_ab == resta_ba

    def perpendicular_3(self, *args):
        vector_a, vector_b = self._obtener_vectores(args)
        return self._producto_punto(vector_a, vector_b) == 0

    def perpendicular_4(self, *args):
        vector_a, vector_b = self._obtener_vectores(args)
        suma = [vector_a[i] + vector_b[i] for i in range(len(vector_a))]
        magnitud_suma = self._magnitud(suma) ** 2
        magnitud_a = self._magnitud(vector_a) ** 2
        magnitud_b = self._magnitud(vector_b) ** 2
        return magnitud_suma == magnitud_a + magnitud_b

    def paralela_1(self, *args):
        vector_a, vector_b = self._obtener_vectores(args)
        if self._magnitud(vector_b) == 0:
            return False
        r = vector_a[0] / vector_b[0] if vector_b[0] != 0 else None
        for i in range(1, len(vector_a)):
            if vector_b[i] == 0:
                if vector_a[i] != 0:
                    return False
            else:
                if r is None or vector_a[i] / vector_b[i] != r:
                    return False
        return True

    def paralela_2(self, *args):
        vector_a, vector_b = self._obtener_vectores(args)
        if len(vector_a) == 2:
            cruzado = vector_a[0] * vector_b[1] - vector_a[1] * vector_b[0]
            return cruzado == 0
        return False  

    def proyeccion_de_a_sobre_b(self, *args):
        vector_a, vector_b = self._obtener_vectores(args)
        producto_punto = self._producto_punto(vector_a, vector_b)
        magnitud_b_cuadrado = self._magnitud(vector_b) ** 2
        if magnitud_b_cuadrado == 0: 
            return [0] * len(vector_a)
        factor = producto_punto / magnitud_b_cuadrado
        return [factor * x for x in vector_b]

    def componente_de_a_en_b(self, *args):
        vector_a, vector_b = self._obtener_vectores(args)
        producto_punto = self._producto_punto(vector_a, vector_b)
        magnitud_b = self._magnitud(vector_b)
        if magnitud_b == 0:  
            return 0
        return producto_punto / magnitud_b

if __name__ == "__main__":
    a = list(map(float, input("Ingrese los elementos del vector a separados por espacios: ").split()))
    b = list(map(float, input("Ingrese los elementos del vector a separados por espacios: ").split()))
    algebra = AlgebraVectorial(a, b)

    print(algebra.perpendicular_1())  
    print(algebra.perpendicular_2())  
    print(algebra.perpendicular_3())  
    print(algebra.perpendicular_4())  
    print(algebra.paralela_1())  
    print(algebra.paralela_2())  
    print(algebra.proyeccion_de_a_sobre_b())  
    print(algebra.componente_de_a_en_b())  
