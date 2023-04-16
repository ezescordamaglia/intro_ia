
def quien_gana(j1, j2):
    if (j1 == j2):
        return 0
    elif ((j1 == "PI") & (j2 == "TI")) | ((j1 == "PA") & (j2 == "PI")) | ((j1 == "TI") & (j2 == "PA")):
        return 1
    else:
        return 2

dict={0:"Empate", 1:"Gana 1", 2:"Gana 2"}

gana = 0

while gana==0:
    jugada1 = input("Juega 1 (PI/PA/TI):")
    jugada2 = input("Juega 2 (PI/PA/TI):")
    gana = quien_gana(jugada1, jugada2)
    print(dict[gana])

print("Fin del juego")

