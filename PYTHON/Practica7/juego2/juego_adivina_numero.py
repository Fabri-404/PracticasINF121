import random
from juego import Juego

class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroVidas):
        super().__init__(numeroVidas)
        self.numeroAAdivinar = 0
        self._vidas_iniciales = numeroVidas

    def reiniciaPartida(self):
        self.numeroDeVidas = self._vidas_iniciales
        self.numeroAAdivinar = random.randint(0, 10)
        while not self.validaNumero(self.numeroAAdivinar):
            self.numeroAAdivinar = random.randint(0, 10)

    def actualizaRecord(self):
        if self.numeroDeVidas > self.record:
            self.record = self.numeroDeVidas
    def quitaVida(self):
        self.numeroDeVidas -= 1
        return self.numeroDeVidas > 0
    def validaNumero(self, numero):
        return 0 <= numero <= 10
    def juega(self):
        self.reiniciaPartida()
        print(f"¡Adivina el numero entre 0 y 10! Tienes {self.numeroDeVidas} vidas.")

        while True:
            try:
                guess = int(input("Ingresa un numero: "))
                if not self.validaNumero(guess):
                    print("Por favor, ingresa un numero entre 0 y 10.")
                    continue
                if guess == self.numeroAAdivinar:
                    print("Acertaste!!")
                    self.actualizaRecord()
                    break
                else:
                    tiene_vidas = self.quitaVida()
                    if tiene_vidas:
                        print(f"Numero incorrecto. Te quedan {self.numeroDeVidas} vidas.")
                    else:
                        print(f"Te quedaste sin vidas. El numero era {self.numeroAAdivinar}.")
                        break
            except ValueError:
                print("Por favor, ingresa un numero entero valido.")