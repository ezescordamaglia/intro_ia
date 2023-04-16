from datetime import date

def calcular_anio_edad_100(age):
    return (date.today().year + 100 -age)

name = input("¿Cual es su nombre?: ")
age = int(input("¿Cuantos años tenes?: "))

anio = calcular_anio_edad_100(age)

print("Cumpliras 100 años en el año " + str(anio))
