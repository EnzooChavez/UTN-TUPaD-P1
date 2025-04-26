# Actividades

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for lista_numeros in range(0, 101):
    print (lista_numeros)
print("//////////////////////////////////////")

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad dedígitos que contiene.

numero = str(input("A continuación, ingrese un número para saber cuantos digitos tiene: "))
digitos = int(len(numero))
print(f"El número ingresado tiene: {digitos} digitos")
print("//////////////////////////////////////")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

numero_uno = int(input("A continuación ingrese el primero de dos numeros para sumar todos los numeros que se situen en medio de ambos: "))
numero_dos = int(input("Ahora el segundo numero: "))
suma_total = 0
for numeros_enmedio in range (numero_uno+1, numero_dos):
    suma_total = suma_total + numeros_enmedio
print(f"La suma total de los numeros es: {suma_total}")
print("//////////////////////////////////////")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
numeros_enteros = int(input("Este programa va a sumar todos los numeros enteros que ingrese. Ingrese el primero de ellos: "))
suma_numeros = 0
while numeros_enteros > 0:
    suma_numeros = suma_numeros + numeros_enteros
    numeros_enteros = int(input("Puede detener la suma ingresando [0], o puede ingresar otro sumero: "))
print(f"La suma de los numeros ingresados es: {suma_numeros}")
print("//////////////////////////////////////")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
objetivo = random.randint(0, 9)
contador_intentos = 0
print("* Bievenido a este juego para adivinar! *")
while True:
    intento = int(input("Ingrese un número entre 0 y 9 hasta adivinar el correcto: "))
    contador_intentos += 1
    if intento == objetivo:
        print(f"¡Lo lograste! Ganaste el juego en {contador_intentos} intentos.")
        break
    else:
        print("Vuelve a intentarlo.")
print("//////////////////////////////////////")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

print("Este programa muestra todos los numeros pares entre 0 y 100: ")
for lista_decreciente in range(100, -1, -2):
    print(lista_decreciente)
print("//////////////////////////////////////")

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

numero_limite = int(input("Este programa muestra la suma de todos los numeros comprendidos entre 0 y el numero entero positivo que ingrese a continuación: "))
total_suma = 0
for lista_desdecero in range (0, numero_limite+1):
    total_suma = total_suma + lista_desdecero
print(f"La suma de todos los numeros comprendidos entre 0 y {numero_limite} es: {total_suma}")
print("//////////////////////////////////////")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, 
# cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

num_par = 0
num_impar = 0
num_pos = 0
num_neg = 0
contador = 0
print("Ingrese hasta 100 numeros para conocer cuantos de ellos fueron pares e impares!")
while contador < 100:
    numeros_dados = int(input("Ingrese un numero: "))
    if numeros_dados % 2 == 0:
        num_par = num_par + 1
    elif numeros_dados % 2 != 0:
        num_impar = num_impar + 1
    if numeros_dados > 0:
        num_pos = num_pos + 1
    elif numeros_dados < 0:
        num_neg = num_neg + 1
    contador = contador + 1
print("* Resultados:  *")
print(f"Números pares:{num_par}")
print(f"Números impares:{num_impar}")
print(f"Números positivos:{num_pos}")
print(f"Números negativos:{num_neg}")
print("//////////////////////////////////////")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debepoder procesar 100 números cambiando solo un valor).

print("Ingrese hasta 100 numeros para calcular su media")
numeros_suma = 0
contador = 0
while contador < 100:
    numeros_media = int(input("Ingrese un numero: "))
    numeros_suma = numeros_suma + numeros_media
    contador = contador + 1
    media = numeros_suma / contador
print(f"La media de los valores ingresados es: {media}")
print("//////////////////////////////////////")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

print("Este es un programa para invertir numeros")
numero = int(input("Ingrese un número: "))
numero_invertido = 0
while numero > 0:
    ultimo_digito = numero % 10
    numero_invertido = (numero_invertido * 10) + ultimo_digito
    numero = numero // 10
print(f"El número invertido es: {numero_invertido}")