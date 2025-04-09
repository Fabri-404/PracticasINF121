from juego_adivina_numero import JuegoAdivinaNumero
from juego_adivina_par import JuegoAdivinaPar
from juego_adivina_impar import JuegoAdivinaImpar

if __name__ == "__main__":
    print("- - - Juego Adivina Numero - - -")
    juego_normal = JuegoAdivinaNumero(3)
    juego_normal.juega()

    print("\n- - - Juego Adivina Par - - - ")
    juego_par = JuegoAdivinaPar(3)
    juego_par.juega()

    print("\n- - - Juego Adivina Impar - - - ")
    juego_impar = JuegoAdivinaImpar(3)
    juego_impar.juega()