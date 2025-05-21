from obra import Obra

class Pintura(Obra):
    def __init__(self, titulo, material, artista, genero):
        super().__init__(titulo, material, artista)
        self.genero = genero
        self.anuncio = None

    def asignar_anuncio(self, anuncio):
        self.anuncio = anuncio
        anuncio.agregar_obra(self)

    def incrementar_precio(self, incremento):
        if self.anuncio:
            self.anuncio.precio += incremento

    def __str__(self):
        return f"Pintura: {self.titulo}, Género: {self.genero}, Material: {self.material}, {self.artista}"