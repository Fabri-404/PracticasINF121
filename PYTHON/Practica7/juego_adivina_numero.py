import random
from juego import Juego

class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroVidas):
        super().__init__(numeroVidas)
        self.numeroAAdivinar = 0
    def reiniciaPartida(self):
        self.numeroDeVidas = super().__init__.__self__.numeroDeVidas
        self.numeroAAdivinar = random.randint(0, 9)
    def actualizaRecord(self):
        if self.numeroDeVidas > self.record:
            self.record = self.numeroDeVidas
    def quitaVida(self):
        self.numeroDeVidas -= 1
        return self.numeroDeVidas > 0
    def juega(self):
        self.reiniciaPartida()
        print(f"¡Adivina el numero entre 0 y 10! Tienes {self.numeroDeVidas} vidas.")

        while True:
            try:
                guess = int(input("Ingresa un número: "))
                if guess < 0 or guess > 10:
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
                print("Por favor, ingresa un numero entero válido.")