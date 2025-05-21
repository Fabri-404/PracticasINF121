class Anuncio:
    def __init__(self, numero, precio):
        self.numero = numero
        self.precio = precio
        self.obras = []
    def agregar_obra(self, obra):
        self.obras.append(obra)

    def calcular_promedio_experiencia(self):
        if not self.obras:
            return 0
        total_experiencia = sum(obra.get_años_experiencia() for obra in self.obras)
        return total_experiencia / len(self.obras)

    def __str__(self):
        obras_str = ", ".join([obra.titulo for obra in self.obras])
        return f"Anuncio {self.numero}, Precio: {self.precio}, Obras: [{obras_str}]"