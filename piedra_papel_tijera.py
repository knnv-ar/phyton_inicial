# Piedra, papel o tijera

import random

def elegir_opciones():
    opciones = ["piedra", "papel", "tijera"]
    jugador_seleccion = input("Ingrese una opción (piedra, papel o tijera): ")
    computadora_seleccion = random.choice(opciones)
    elecciones = {"jugador": jugador_seleccion, "computadora": computadora_seleccion}

    return elecciones

#selecciones = seleccionar_opciones()
#print(elecciones)

def comprobar_ganador(jugador, computadora):
    print(f"Elegiste {jugador} y la computadora eligió {computadora}")
    if jugador == computadora:
        print("¡Es un empate!")

    elif jugador == "piedra":
        if computadora == "tijera":
            return "La piedra rompe la tijera. ¡Ganaste!"
        else:
            return "El papel envuelve a la piedra. ¡Perdiste!"

    elif jugador == "tijera":
        if computadora == "papel":
            return "La tijera corta el papel. ¡Ganaste!"
        else:
            return "La piedra rompe la tijera. ¡Perdiste!"

    elif jugador == "papel":
        if computadora == "piedra":
            return "El papel envuelve a la piedra. ¡Ganaste!"
        else:
            return "La tijera corta el papel. ¡Perdiste!"

elecciones = elegir_opciones()

resultado = comprobar_ganador(elecciones["jugador"], elecciones["computadora"])
print(resultado)


# Esta estructura de if y elif es
# el primer paso para resolver quién gana
# Luego vendrá la refactorización con
# if anidado
"""
elif jugador == "piedra" and computadora == "tijera":
    return "La piedra rompe la tijera. ¡Ganaste!"
elif jugador == "piedra" and computadora == "papel":
    return "El papel envuelve a la piedra. ¡Perdiste!"
"""