from artista import Artista
from obra import Obra
from pintura import Pintura
from anuncio import Anuncio


def main():
    artista1 = Artista("Leonardo", "12345", 20)
    artista2 = Artista("Miguel", "67890", 15)

    #A)
    pintura1 = Pintura("Mona Lisa", "Óleo", artista1, "Retrato")
    pintura2 = Pintura("Guernica", "Óleo", artista2, "Histórico")
    anuncio1 = Anuncio(1, 500)
    anuncio2 = Anuncio(2, 300)
    pintura1.asignar_anuncio(anuncio1)
    pintura2.asignar_anuncio(anuncio2)
    print("Pinturas creadas con anuncios:")
    print(pintura1)
    print(pintura2)
    print(anuncio1)
    print(anuncio2)

    #B)
    promedio_exp = (anuncio1.calcular_promedio_experiencia() + anuncio2.calcular_promedio_experiencia()) / 2
    print("\nPromedio de años de experiencia de los artistas:")
    print(f"Promedio: {promedio_exp}")

    #C)
    incremento = 100
    for pintura in [pintura1, pintura2]:
        if pintura.artista.nombre == "Miguel":
            pintura.incrementar_precio(incremento)
            print(f"\nPrecio incrementado en {incremento} para {pintura.titulo}")
            print(f"Nuevo precio del anuncio: {pintura.anuncio.precio}")

if __name__ == "__main__":
    main()