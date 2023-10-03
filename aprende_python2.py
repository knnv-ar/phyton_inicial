# video
# Python for Beginners – Full Course [Programming Tutorial]
# https://youtu.be/eWRfhZUzrAc
# por Beau Carnes

# clase 1: piedra, papel o tijera
# clase 2: fundamentos: "Setup Python Locally" > "Control Statements"
# clase 3: fundamentos: "Lists" > "Break and Continue"
# clase 4: fundamentos: "Classes" > "Operator Overloading"


# VARIABLE: # así creo una variable y le asigno un valor
texto = "Este es un texto."

# FUNCION: Así ejecuto una función
print(texto)


# FUNCION: Así defino una función (se usa obligatoriamente un tab para determinar los contenidos de la misma)
def saludo():
    return "Hola!"


print(saludo())

# DICTIONARIES
# DICCIONARIO: almacena datos en pares clave-valor
persona = {"nombre": "Ana", "profesion": "artista"}
n_persona = persona["nombre"]
print(n_persona)  # imprimirá: Ana

# LIBRARIES, LISTS, METHODS
# Librerías, listas y métodos

# LIBRERÍA: importamos la librería random
import random

# LISTA (almacena múltiples elementos en una variable. Una lista es un tipo de secuencia)
food = ["pizza", "milanga", "sushi"]


# Argumentos de funciones
def jugador_futbol(apellido, nro_camiseta):
    return [apellido, nro_camiseta]


# Estructura condicional if
if a > b:
    print("a es mayor que b")

# Cadenas de texto concatenadas
print("You chose " + jugador + ", computer chose " + computadora)

# F-strings
edad = 5
print(f"Lisandro tiene {edad} años.")

# Estructuras condicionales else / elseif
edad = 20
if edad >= 18:
    print("Es una persona adulta.")
else:
    print("Es una persona menor de edad.")

edad = 25
if edad >= 18:
    print("Es una persona adulta.")
elif edad > 12:
    print("Es una persona adolescente.")
elif edad > 1:
    print("Es una persona infante.")
else:
    print("Es una persona bebé.")

# Refactorización e if anidado


# =================================
# =================================
# Fundamentos de Python

"""
Variables

Sólo se pueden usar constructos que no sean palabras clave de Python y que comience con letras
o guión bajo y luego letras, números o guiones bajos. Todos los demás caracteres están prohibidos.
"""

nombre = "Juan"
edad = 25

nombre1
ALTURA
mi_nombre
_nombre


# Expresiones e instrucciones
"""
- Una expresión es un fragmento de código que evalúa un valor

1
1+1
"Pedro"

- Una instrucción es un frangmento de código que realiza una acción sobre un valor:

nombre = "Pedro"
print(nombre)

- Un programa se realiza con un conjunto de instrucciones

En dos líneas: 

nombre = "Pedro"
print(nombre)

En una linea: 

nombre = "Pedro"; print(nombre)
"""

# Comentarios
"""
# Comentario en una linea

tres guiones rectos para iniciar y los mismos para cerrar
"""

# Sangría (indentation)
"""
Es muy importante para definir los bloques de código 
"""

# Tipos de dato (data types)
"""
string = str
integer= int
float = float
nñumeros complejos = complex
booleanos = bool
listas = lists
tuples = tuple
ranges = range
diccionarios = dict
conjuntos = sets

La creación del tipo de dato es dinámica. Pero podemos determinarla de forma manual con:
edad = float(2)
print(isinstance(edad, float))
"""

nombre = "Laura"
print(type(nombre))

# Operadores aritméticos
"""
=   operador de asignación 
+   operador de adición
-   operador de sustracción
*   operador de multiplicación
/   operador de división
%   resto
**  exponentes
//  floor division

*=  operadores combinados
"""

# Operadores de comparación
"""
==
!=  
>   
<   

Devuelven True o False
"""

# Operadores booleanos
"""
not
and
or

condicion1 = True
condicion2 = False

not condicion1 #False
condicion1 and condicion2 #False
condicion1 or condicion2 #True

# or

print(0 or 1) ## 1
print(False or "che") ## "che"
print("hola" or "che") ## "hola"
print([] or False) ## "False"
print(False or []) ## "[]"

# and
print(0 and 1) ## 0
print(1 and 0) ## 0
print(False and "che") ## False
print("hola" and "che") ## "che"
print([] and False) ## "[]"
print(False and []) ## "False"
"""

# Operadores bit a bit (bitwise operators)
"""
& ejecuta AND binario
| ejecuta OR binario
^ ejecuta una operación XOR binaria
~ ejecuta una operación NOT binaria
<< operación de desplazamiento a la izquierda
>> operación de desplazamiento a la derecha
"""

# Operadores is e in (is & in operators)
"""
is  es el operador de identidad (identity operator) usado para comparar dos objetos que devuelve True si ambos son el mismo objeto.
in  es el operador de membresía (membership operator) usado para verificar si un valor está contenido en una lista o en otra secuencia.
"""

# Operador ternario (ternary operator)
"""
Es usado para definir un condicional de manera rápida:

def es_adulto(edad):
    if edad > 18:
        return True
    else:
        return False

pasa a:

def es_adulto(edad)
    return True if edad > 18 else False
"""

# Cadenas de texto
"""
"Ana"
'Ana'

nombre = "Beatriz"
frase = nombre + "es artista" # concatenación de textos con operador de adición

o bién

frase += "es artista"

Por otro lado, se puede hacer una cadena de texto multilínea:
""" ""
print(
    """Este
es
un texto
multilínea
"""
)

# Métodos de cadenas de textos
"""
print("Eva".upper()) # EVA
print("EVA".lower()) # eva
print("eVa y lisandro".title()) # Eva Y Lisandro
print("eVa y lisandro".islower()) # False

Siempre devuelven una nueva cadena de texto, no altera la original:
isalpha() evalua si la cadena contiene sólo caracteres alfabéticos y no esté vacía
isalnum() evalua si la cadena contiene caracteres alfabéticos o numéricos y no esté vacía
isdecimal() evalua si la cadena contiene sólo caracteres numéricos y no esté vacía
lower() convierte el textp a caracteres en minúsculass
islower() evalua si la cadena tiene todos sus caracteres en minúsculas
upper() convierte el textp a caracteres en mayúsculas
isupper() evalua si la cadena tiene todos sus caracteres en mayúsculas
title() convierte el texto en versión capitalizada
startswith() evalua si la cadena comienza con una subcadena específica
endwith() evalua si la cadena termina con una subcadena específica
replace() para reemplazar una parte de la cadena
split() para dividir una cadena en un caracter separador específico
strip() para recortar el espacio en blanco de una cadena
join() para añadir nuevos caracteres a una cadena
find() para encontrar la posición de una subcadena

Funciones globales:
len()   deveulve la cantidad de elementos

nombre = "Eva"
print(len(nombre)) ## 3
print("va" in nombre) ## True
"""

# Caracteres de escape (para agregar caracteres especial a una cadena)
"""
print("E\"va") ## E"va
print("E\\va") ## E\va
print("E\nva") ## \n imprime en una nueva línea
## E
## va
"""

# Caracteres de cadena y corte (String characters and slicing)

"""
nombre = "Eva"
print(nombre[0]) # E
print(nombre[-1]) # a
print(nombre[1:2]) # v
print(nombre[1:3]) # va
print(nombre[:2]) # Ev ## desde el comienzo hasta 2
print(nombre[1:]) # va ## desde 1 hasta el final
"""

# Booleanas

"""
True y False

- Todos los números se evalúan como True (incluso los negativos) salvo el cero.
- Todas las cadenas se evalúan como True salvo cuando están vacías
- Listas, tuplas conjuntos y diccionarios se evalúan como True salvo cuando están vacías

Función global any() muy util para usar con booleanas.
Regresa True si alguno de los valores de un iterable (por ejemplo una lista)
es True.

libro_1_leido = True
libro_2_leido = False

algun_libro_leido = any([libro_1_leido, libro_2_leido]) # True

Función global all() muy util para usar con booleanas.
Regresa True si todos los valores de un iterable (por ejemplo una lista)
es True.

libro_1_leido = True
libro_2_leido = False

algun_libro_leido = all([libro_1_leido, libro_2_leido]) # False
"""

# Tipos de datos numéricos

"""
Los números complejos son una extensión del sistema de números reales
donde todos los numeros son expresados como una suma de una parte real
y una parte imaginaria (5 + 2i)

Los números imaginarios son múltiplos reales de la unidad imaginaria
(que es la raíz cuadrada de -1, es decir: i = math.sqrt(-1))
Python soporta la escritura de números complejos con la notación j.

Se puede escribir así:
numero_complejo1 = 2+3j

O bien así:
numero_complejo2 = complex(2,3)
print(numero_complejo2.real, numero_complejo2. imag) ## 2.0 3.0
"""

# Funciones globales utiles para los números
"""
abs()   devuelve el valor absoluto del numero
round() redondea al entero más cercano
"""

# Enums (usado para crear constantes)
"""
Los enums son nombres legibles unidos a un valor constante

from enum import Enum
class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

print(State.ACTIVE.value) ## 1
print(State.INACTIVE.value) ## 0
print(list(State)) ## [<State.INACTIVE: 0>,<State.ACTIVE: 1>]
print(len(State)) ## 2
"""

# USER INPUT
"""
edad = input("Cuál es tu edad? ")
print("Tu edad es " + edad)
"""

# LISTAS
"""
Las listas son una estructura de datos esencial en python.

pokemones = ["Pikachu", "Charmander", "Squirtle"]
print("Mylau" in pokemones) ## False

Las listas pueden contener distintos tipos de datos:
cosas = ["Darth Vader", 4, 2.1532, True]

Podemos usar el método de índice para acceder a los elementos de la lista:
print(4 in cosas) ## True
print(cosas[0]) ## "Darth Vader"

cosas[2] = 8
print(cosas) ## "Darth Vader", 8, 2.1532, True
print(cosas[-2]) ## 2.1532

print(cosas[1:2]) ## 8, 2.1532
print(cosas[2:]) ## 2.1532, True
print(cosas[:2]) ## "Darth Vader", 8, 2.1532
print(len(cosas)) ## 4

Agregamos elementos a la lista con .append(), siempre al final de la lista:
cosas.append("Copa del mundo")

También agregamos elementos a la lista con .extend(), siempre al final
de la lista pero podemos incorporarlo como lista:
cosas.extend(["Copa del mundo 2022"])
cosas.extend(["Copa del mundo 2022", "Copa Finalissima 2022", "Copa América 2021", 3])

Otra forma de agregar elementos a una lista es con el operador de adición:
cosas += ["Copa del mundo 2022", "Copa Finalissima 2022", "Copa América 2021", 3]

Es importante no olvidar de usar los corchetes ya que si se lo hace va a
incorporar cada caracter como un elemento nuevo en la lista:
cosas += "Copa del mundo 2022" ## No es un método recomendado

Ahora, es posible remover elementos con el método .remove():
cosas.remove("Darth Vader")
print(cosas) ## 8, 2.1532, True

Otro método muy usado en las listas es .pop(), el cual se encarga
de remover y regresar el último elemento:
print(cosas.pop()) ## True
print(cosas) ## 8, 2.1532

Bien, ahora para insertar un elemento en algún lugar
de la lista usamos .insert():
lista_colores = ["rojo", "verde", "azul"]
lista_colores.insert(1, "amarillo")
print(lista_colores) ## "rojo", "amarillo", "verde", "azul"

Si queremos insertar varios elementos en algún lugar
de la lista usamos el caracter ":":
lista_colores = ["rojo", "verde", "azul"]
lista_colores[1:1] = ["naranja", "amarillo"]
print(lista_colores) ## "rojo", "naranja", "amarillo", "verde", "azul"

Para la ordenación de listas usamos .sort().
colores = ["rojo", "naranja", "amarillo", "verde", "azul"]
colores.sort()
print(colores) ## "amarillo", "azul", "naranja", "rojo", "verde"

Las mayúsculas tienen un ordende nivel prevalecente a las minúsculas,
por lo tanto si las queremos ordenar en el mismo nivel tenemos que usar:
colores = ["rojo", "naranja", "amarillo", "verde", "Azul"]
print(colores) ## "Azul", "amarillo", "naranja", "rojo", "verde"
colores.sort(key=str.lower)
print(colores) ## "amarillo", "Azul", "naranja", "rojo", "verde"

La ordenación de elementos mediante .sort() modifica el contenido origical de la lista.
Para evitar esto podemos copiar la lista en otra lista:
colores = ["rojo", "naranja", "amarillo", "verde", "Azul"]
colores_copia = colores[:]
colores_copia.sort(key=str.lower)
print(colores) ## "rojo", "naranja", "amarillo", "verde", "Azul"
print(colores_copia) ## "amarillo", "Azul", "naranja", "rojo", "verde"

Por último, para ordenar los contenidos de un lista sin modificar la lista original:
colores = ["rojo", "naranja", "amarillo", "verde", "Azul"]
print(sorted(colores, key=str.lower)) ## "amarillo", "Azul", "naranja", "rojo", "verde"
print(colores) ## "rojo", "naranja", "amarillo", "verde", "Azul"

colores_copia.sort(key=str.lower)
print(colores_copia) ## "amarillo", "Azul", "naranja", "rojo", "verde"


"""

# Creating a tuple
my_tuple = (1, "apple", 3.14)

# Accessing elements by index
print(my_tuple[0])  # Output: 1
print(my_tuple[1])  # Output: 'apple'

# Tuple unpacking
x, y, z = my_tuple
print(x)  # Output: 1
print(y)  # Output: 'apple'
print(z)  # Output: 3.14

# =================================
# =================================

# Python IDLE ???
# Python Standard REPL (read-eval-print-loop) ???
# https://replit.com/@BeauCarnes/rps-python#main.py

"""
Learn Python by Building Five Games - Full Course
(Pong, Snake, Connect four, Tetris, Mutiplayer [Rock, Scissors, Paper])
https://youtu.be/XGf2GcyHPhc

20 Beginner Python Projects
https://youtu.be/pdy3nh1tn6I
(0:00:00) Introduction  
(0:00:41) Email Sender    
(0:12:15) Word Replacement Program    
(0:14:35) Basic Calculator
(0:28:21) Email Slicer
(0:35:20) Binary Search Algorithm
(0:53:48) Quiz Program
(1:07:04) QR Code Generator
(1:13:58) Interest Payment Calculator
(1:21:51) Random Password Generator
(1:31:41) Dice Rolling Simulator
(1:38:47) Site Connectivity Checker
(1:47:29) Currency Converter
(1:51:53) Leap Year Checker
(1:55:53) Word Dictionary
(2:07:41) Rock, Paper, Scissors
(2:19:39) Python Face Detection
(2:27:14) Python Automation
(2:39:02) Web Scraper
(2:47:28) Image Resizer
(2:57:34) Graph Plotter

12 Beginner Python Projects - Coding Course
https://youtu.be/8ext9G7xspg
(1:40) 1. Madlibs 
(6:54) 2. Guess the Number (computer) 
(13:17) 3. Guess the Number (user)
(21:14) 4. Rock Paper Scissors
(24:25) 5. Hangman
(35:53) 6. Tic-Tac-Toe
(59:59) 7. Tic-Tac-Toe AI
(1:15:53) 8. Binary Search 
(1:27:16) 9. Minesweeper 
(1:51:55) 10. Sudoku Solver 
(2:05:34) 11. Photo Manipulation in Python 
(2:31:49) 12. Markov Chain Text Composer 

Pygame Tutorial for Beginners - Python Game Development Course (una especie de space invaders trucheli)
https://youtu.be/FfWpgLFMI7w
"""
