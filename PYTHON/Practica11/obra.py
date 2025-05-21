class Obra:
    def __init__(self, titulo, material, artista):
        self.titulo = titulo
        self.material = material
        self.artista = artista

    def get_artista_nombre(self):
        return self.artista.nombre

    def get_años_experiencia(self):
        return self.artista.añosExperiencia

    def __str__(self):
        return f"Obra: {self.titulo}, Material: {self.material}, {self.artista}"