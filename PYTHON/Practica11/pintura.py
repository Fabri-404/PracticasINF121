from obra import Obra

class Pintura(Obra):
    def __init__(self, titulo, material, artista, genero):
        super().__init__(titulo, material, artista)
        self.genero = genero

    def crear_pintura_sin_anuncio(self):
        return f"Pintura creada: {self.titulo}, Género: {self.genero}, sin anuncio"

    def __str__(self):
        return f"Pintura: {self.titulo}, Género: {self.genero}, Material: {self.material}, {self.artista}"