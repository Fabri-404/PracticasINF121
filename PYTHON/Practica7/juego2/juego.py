from abc import ABC, abstractmethod

class Juego(ABC):
    def __init__(self, numeroVidas):
        self.numeroDeVidas = numeroVidas
        self.record = 0
    @abstractmethod
    def reiniciaPartida(self):
        pass
    @abstractmethod
    def actualizaRecord(self):
        pass
    @abstractmethod
    def quitaVida(self):
        pass