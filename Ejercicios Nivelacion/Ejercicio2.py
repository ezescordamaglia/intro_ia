


def valores_debajo_umbral(lista, umbral):
    aux = []
    for value in lista:
        if (value <= umbral):
            aux.append(value)
    return aux

umbral = 6
lista = [52, 10, 2, 3, 6, 7, -1, 5, 8]

# Forma manual
print(valores_debajo_umbral(lista, umbral))

# Forma automatica
print(list(filter(lambda x: x <= umbral, lista)))

# Otra forma automatica
print([elemento for elemento in lista if elemento <= umbral])

