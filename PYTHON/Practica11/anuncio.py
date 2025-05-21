class Anuncio:
    def __init__(self, numero, precio):
        self.numero = numero
        self.precio = precio
        self.obras = []

    def agregar_obra(self, obra):
        self.obras.append(obra)

    def calcular_monto_venta(self):
        return len(self.obras) * self.precio

    def __str__(self):
        obras_str = ", ".join([obra.titulo for obra in self.obras])
        return f"Anuncio {self.numero}, Precio: {self.precio}, Obras: [{obras_str}]"