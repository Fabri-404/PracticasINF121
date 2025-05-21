class Artista:
    def __init__(self, nombre, ci, añosExperiencia):
        self.nombre = nombre
        self.ci = ci
        self.añosExperiencia = añosExperiencia

    def __str__(self):
        return f"Artista: {self.nombre}, CI: {self.ci}, Años de Experiencia: {self.añosExperiencia}"