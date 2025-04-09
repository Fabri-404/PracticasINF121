from juego_adivina_numero import JuegoAdivinaNumero

class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        return super().validaNumero(numero) and numero % 2 != 0

    def juega(self):
        self.reiniciaPartida()
        print(f"¡Adivina un numero IMPAR entre 0 y 10! Tienes {self.numeroDeVidas} vidas.")
        
        while True:
            try:
                guess = int(input("Ingresa un numero: "))
                if not self.validaNumero(guess):
                    print("Por favor, ingresa un numero IMPAR entre 0 y 10.")
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