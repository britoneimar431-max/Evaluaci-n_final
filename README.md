# Evaluaci-n_final

El impacto de las Nuevas Tecnologías en la Sociedad: Desarrollo y Proyección de Soluciones Informáticas

Nombre:
Neimar Brito

Objetivo del sistema: 
El objetivo es crear un juego de "Piedra, Papel o Tijeras" en la computadora donde una persona pueda jugar contra la máquina todas las veces que quiera. El programa debe ser inteligente: debe llevar el marcador de los puntos de cada uno, saber quién gana en cada ronda sin equivocarse y, si el jugador presiona un botón por error, el juego no debe trabarse ni cerrarse solo.

Explicación del Sistema y Descripción de Funcionalidades 
1.	Selección interactiva del jugador: Permite al usuario elegir su jugada (piedra, papel o tijeras) de forma cómoda ingresando los números 1, 2 o 3 desde el teclado.
2.	Rival inteligente: La computadora genera una jugada 100% aleatoria e impredecible en cada ronda utilizando la biblioteca random de Python. 
3.	Árbitro lógico automatizado: El sistema analiza las elecciones de ambos jugadores bajo las reglas reales del juego y determina instantáneamente si hubo un empate, si ganaste tú o si ganó la máquina.
4.	Marcador acumulativo: El programa lleva la cuenta de los puntos. Al terminar cada ronda, te muestra en pantalla el marcador actualizado con tus victorias y las de la computadora.
5.	Protección contra errores: Si el usuario ingresa una opción que no existe (como una letra o el número 5), el sistema detecta el error, muestra un mensaje de advertencia y reinicia la ronda limpiamente sin trabarse ni cerrarse.
6.	Modo de juego infinito: El juego no se apaga al terminar una ronda. Te pregunta explícitamente si deseas continuar jugando o si prefieres salir escribiendo palabras clave como "no" o "salir".

Fecha: 
28/06/2026

Introducción

Este proyecto consiste en el desarrollo de un simulador interactivo del juego clásico "Piedra, Papel o Tijeras", diseñado para ejecutarse en un entorno de consola utilizando el lenguaje de programación Python.
Descripción del problema 
El problema radica en la necesidad de automatizar un juego tradicional en caso de que no exista la posibilidad de un segundo jugador. Para solucionarlo el software debe ser capaz de:
1.	Simular un rival que elija al azar de forma justa
2.	Actuar como un árbitro para decidir quién gana la ronda
3.	Llevar la cuenta de los puntos del jugador y de sí mismo
4.	Mantener un flujo continúo permitiéndole al jugador decidir si participar en otra ronda o dar por finalizado el juego

Reflexión sobre el impacto de la tecnología

En el software desarrollado destacan tres puntos fundamentales a la hora de construir una solución digital a un problema real.
1.	Automatización de toma de decisiones
El programa es capaz de determinar el resultado de la ronda, simular un rival y llevar una cuenta de los puntos sin tener que anotarlos manualmente usando reglas lógicas como el if/else, eliminado el error humano y hace los procesos instantáneos. 
2.	Proactividad ante errores humanos
Comandos como el continue y el .lower() le permiten al programa proteger al usuario de sus propios errores, como aplastar otro botón o escribir todo en mayúsculas. Un software de calidad no se rompe cuando el usuario comete un error.
3.	Traducción de ideas abstractas a la realidad
Antes de codificar se realizó los respectivos diagramas que nos permitieron tener una idea visual de como sería el resultado final, esta experiencia demuestra que la tecnología es la herramienta que nos permite transformar ideas abstractas y lógica pura en soluciones interactivas reales.

Relación con los contenidos de la asignatura

En el programa se usó las variables y tipos de datos como cadenas de textos y números enteros, también las estructuras de datos como el diccionario (“1”: “piedra”).
La lógica condicional (if/else/elif) para determinar las reglas del juego y determinar un ganador.
Ciclos o bucles (While/True) permitiendo al programa la repetición del juego.

Planificación del Proyecto 

1.	Definir el alcance del sistema a desarrollar
Este proyecto se limita únicamente a crear un juego de piedra, papel o tijeras que se ejecuta en la terminal de Visual Studio Code.
2.	Identificar el Problema que se Desea Resolver
El problema radica en la necesidad de automatizar un juego tradicional en caso de que no exista la posibilidad de un segundo jugador. Para solucionarlo el software debe ser capaz de:
1.	Simular un rival que elija al azar de forma justa
2.	Actuar como un árbitro para decidir quién gana la ronda
3.	Llevar la cuenta de los puntos del jugador y de sí mismo
4.	Mantener un flujo continúo permitiéndole al jugador decidir si participar en otra ronda o dar por finalizado el juego

Elaborar un cronograma de actividades desde la semana 1 hasta la 8, considerando los temas de la asignatura

Semana 1: Pensé en la idea del juego y definí qué problemas iba a resolver (la falta de un segundo jugador).

Semana 2: Dibujé el Diagrama de Flujo en papel para planificar los caminos del juego y entender la lógica antes de escribir código.

Semana 3: Instalé y configuré Visual Studio Code en mi computadora para dejar listo el entorno de programación.

Semana 4: Creé la base del código, puse las variables para los puntos y armé el ciclo repetitivo principal (while True) para que el juego fuera infinito.

Semana 5: Programé la lógica para que la computadora elija al azar usando random y armé la lista de opciones (piedra, papel, tijeras) con un diccionario.

Semana 6: Escribí las reglas del juego usando los condicionales (if, elif, else) para comparar las jugadas y saber quién gana o si hay empate.

Semana 7: Mejoré el programa agregando el (continue) por si el usuario escribe un número que no es, y configuré las palabras para salir del juego de forma segura (break).

Semana 8: Agregué los comentarios explicativos dentro de mi código, ordené los archivos y subí todo el proyecto final a mi repositorio de GitHub.

