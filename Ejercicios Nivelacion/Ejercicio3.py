def elementos_comunes(a, b):
    aux = []
    for valueA in a:
        for valueB in b:
            if (valueA == valueB):
                aux.append(valueA)
    return aux

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Forma 1 - Falla porque repite el 1
print(elementos_comunes(a, b))

# Forma 2
print(list(set(a)&set(b)))


