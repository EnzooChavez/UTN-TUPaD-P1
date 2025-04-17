#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad = int(input("A continuación, ingrese su edad: "))
print("Es mayor de edad") if edad >= 18 else print("No es mayor de edad")
print("***************separador*************************")
#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.
nota = int(input("Ingrese su nota: "))
print("Aprobado") if nota >= 6 else print("Desaprobado")
print("***************separador*************************")
#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.
numero = int(input("A continuación, ingrese un numero par: "))
print("Ha ingresado un número par") if (numero % 2 == 0) else print("Por favor, ingrese un número par")
print("***************separador*************************")
#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.
edad_usuario = int(input("Ingrese su edad para saber a que categoria pertenece: "))
if (edad_usuario < 12):
    print("Usted tiene la categoria de: Niño/a")
elif (edad_usuario >= 12 and edad_usuario < 18):
    print("Usted tiene la categoria de: Adolescente")
elif (edad_usuario >= 18 and edad_usuario < 30):
    print("Usted tiene la categoria de: Adulto/a joven")
elif (edad_usuario >= 30):
    print("Usted tiene la categoria de: Adulto/a")
print("***************separador*************************")
#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.
password = input("Por favor, ingrese una contraseña de entre 8 y 14 caracteres: ")
len_password = len(password)
if (len_password >= 8 and len_password <= 14):
    print("Ha ingresado una contraseña correcta")  
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
print("***************separador*************************")
#Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range (50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
if (media > mediana) and (mediana > moda):
    print("Tomando la lista de numeros aleatorios y calculando su media, mediana y moda, el programa calcula que hay: Sesgo positivo")
elif (media < mediana) and (mediana < moda):
    print("Tomando la lista de numeros aleatorios y calculando su media, mediana y moda, el programa calcula que hay: Sesgo negativo")
elif (media == mediana) and (mediana == moda):
    print("Tomando la lista de numeros aleatorios y calculando su media, mediana y moda, el programa calcula que no hay sesgo")
print("***************separador*************************")
#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
frase_o_palabra = input("Ingrese una frase o palabra: ")
if frase_o_palabra[-1] in ("a, A, e, E, i, I, o, O, u, U"):
    frase_o_palabra = frase_o_palabra + "!"
    print(frase_o_palabra)
else:
    print(frase_o_palabra)
print("***************separador*************************")
#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),#lower() y title() de Python para convertir entre mayúsculas y minúsculas.
nombre = input("Ingrese su nombre: ")
print("*Ingrese el número 1, 2 o 3 dependiendo de la opción que desee: ")
print("1.Si quiere su nombre en mayúsculas.")
print("2.Si quiere su nombre en minúsculas.")
print("3.Si quiere su nombre con la primera letra mayúscula.*")
opcion = int(input("Opción: "))
if (opcion == 1):
    mayus = nombre.upper()
    print(mayus)
elif (opcion == 2):
    minus = nombre.lower()
    print(minus)
elif (opcion == 3):
    letra_mayus = nombre.capitalize()
    print(letra_mayus)
else:
    print("Por favor, ingrese 1 o 2 o 3.")
print("***************separador*************************")
#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
magnitud = int(input("Ingrese la magnitud del terremoto para saber su categoria: "))
if magnitud < 3:
    print("Categoria: Muy leve, imperceptible.")
elif (magnitud >= 3) and (magnitud < 4):
    print("Categoria: Leve, ligeramente perceptible.")
elif (magnitud >= 4) and (magnitud < 5):
    print("Categoria: Moderado, sentido por personas, pero generalmente no causa daños.")
elif (magnitud >= 5) and (magnitud < 6):
    print("Categoria: Fuerte, puede causar daños en estructuras débiles.")
elif (magnitud >= 6) and (magnitud < 7):
    print("Categoria: Muy Fuerte, puede causar daños significativos.")
elif (magnitud >= 7) :
    print("Categoria: Extremo, puede causar graves daños a gran escala.")
print("***************separador*************************")
#10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.
hemisferio = input("Que hemisferio es? (N/S): ")
mes = int(input("Que mes del año es(del 1 al 12): "))
dia = int(input("Que dia del mes es(del 1 al 31): "))
if (hemisferio == "N"):
    if (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia < 21):
        print("Estación: Primavera")
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia < 21):
        print("Estación: Verano")
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia < 21):
        print("Estación: Otoño")
    else:
        print("Estación: Invierno")
elif hemisferio == 'S':
    if (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia < 21):
        print("Estación: Otoño")
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia < 21):
        print("Estación: Invierno")
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia < 21):
        print("Estación: Primavera")
    else:
        print("Estación: Verano")
else:
    print("Los datos ingresados son incorrectos.")




