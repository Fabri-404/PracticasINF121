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
    print("Pintura sin anuncio:")
    print(pintura2.crear_pintura_sin_anuncio())

    anuncio = Anuncio(1, 500)
    anuncio.agregar_obra(pintura1)
    print("\nPintura con anuncio:")
    print(anuncio)

    #B)
    print("\nArtista y experiencia de pintura con anuncio:")
    print(f"Nombre: {pintura1.get_artista_nombre()}, Años de Experiencia: {pintura1.get_años_experiencia()}")
    print("Artista y experiencia de pintura sin anuncio:")
    print(f"Nombre: {pintura2.get_artista_nombre()}, Años de Experiencia: {pintura2.get_años_experiencia()}")

    #C)
    print("\nMonto total de venta del anuncio:")
    print(f"Monto: {anuncio.calcular_monto_venta()}")

if __name__ == "__main__":
    main()