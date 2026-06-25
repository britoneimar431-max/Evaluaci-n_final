#Configuracion del juego aleatorio de la computadora
import random
#Inicializacion de puntos fuera del bucle para que no se reinicien cada vez que se vuelve a jugar
puntos_jugador = 0
puntos_computadora = 0
#Bucle del juego
while True:
    #Se solicia al juegador que eliga entre piedra, papel o tijeras usando saltos de liena para mejorar la legibilidad
    eleccion_jugador = input("Elige piedra, papel o tijeras:\n1 = piedra\n2 = papel\n3 = tijeras\nOpcion: ")
    #Nos aseguramos de que el jugador ingrese una opción válida, si no es así, se le pide que vuelva a intentarlo
    if eleccion_jugador not in ["1", "2", "3"]:
        print("Opción no válida. Por favor, elige 1, 2 o 3.")
        #Si la opción no es válida, se vuelve al inicio del bucle para solicitar al jugador que ingrese una opción válida
        continue
    #Se utiliza un diccionario para mapear los números y establecer su valor correspondiente
    opciones = {"1":"piedra", "2": "papel", "3": "tijeras"}
    #Se usa el random.randint para generar un número aleatorio dentro del rango de 1 a 3, el cual representa la elección de la computadora
    numero_computadora = random.randint(1,3)
    eleccion_final_jugador = opciones[eleccion_jugador]
    #Se usa el str para convertir el núemero elegido por la computadora a texto  
    eleccion_final_computadora = opciones[str(numero_computadora)]
    #Se usa el format para evitar concatenar texto con variables repetidamente 
    print(f"\nTú elegiste: {eleccion_final_jugador}")
    print(f"La computadora eligió: {eleccion_final_computadora}")
    #Se empieza a codificar la lógica del juego, siguiendo las reglas tradicionales de piedra, papel o tiejeras
    if eleccion_final_jugador == eleccion_final_computadora:
        print("!Empate!")
    #Se usa el elif para evitar usar multiples if anidados
    elif (eleccion_final_jugador == "piedra" and eleccion_final_computadora == "tijeras") or \
        (eleccion_final_jugador == "papel" and eleccion_final_computadora == "piedra") or \
        (eleccion_final_jugador == "tijeras" and eleccion_final_computadora == "papel"):
        print("¡Ganaste!")
    #El += se usa para incrementar el valor de puntos_jugador en 1 cada vez que este gana, en lugar de puntos_jugador = puntos_jugador +1
        puntos_jugador += 1
    else:
        print("¡Perdiste!")
        puntos_computadora += 1
    print(f"\nPuntos del jugador: {puntos_jugador}")
    print(f"Puntos de la computadora: {puntos_computadora}")
    #Después de mostrar el resultado se le pregunta al jugador si desea jugar otra vez, usando el new line para mejorar la legibilidad
    jugar_otra_vez = input("\n¿Quieres jugar otra vez? (s/n): ")
    #Se verifica si la respuesta del jugador es negativa, usando el lower para convertir la respuesta a minúscula y así aceptar diferentes formas de decir no
    if jugar_otra_vez.lower() in ["n", "no", "salir", "nope", "nah", "nada", "nouuuu"]:
    #Si decide salir del juego, se muestra un mensaje de despedida y se rompe el bucle
        print("¡Gracias por jugar! ¡Hasta la próxima!")
        break