
def reemplazar_letras(palabraAdivinada, palabra, letra):
    for index, l in enumerate(palabra):
        if (l == letra):
            palabraAdivinada = palabraAdivinada[:index] + letra + palabraAdivinada[index + 1:]
    return palabraAdivinada


palabra = input("Ingrese una palabra de entre 5 y 8 letras:")

intentos = 5
acertado = False
palabraAdivinada = "_" * len(palabra)


while (intentos>0) & (not acertado):
    print("\nPalabra:")
    print(palabraAdivinada)

    letra = input("Ingrese una letra:")
    if (letra in palabra):
        palabraAdivinada = reemplazar_letras(palabraAdivinada, palabra, letra)
        if palabraAdivinada == palabra:
            acertado = True
    else:
        intentos = intentos - 1
        print("Perdiste un intento. Te quedan " + str(intentos))

if palabraAdivinada == palabra:
    print("¡¡¡¡¡GANASTE!!!!")
else:
    print("¡PERDISTE!")

print("Fin del juego")

