# TRABAJO PRACTICO: RECURSIVIDAD

# Ejercicios
# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

num = int(input("Introduzca un numero para saber su factorial: "))

print(factorial(num))

print("/////////////////////////////////////////////")
# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique

def funcion_fibonacci(pos):
    if pos == 0 or pos == 1:
        return pos
    else:
        return funcion_fibonacci(pos-1) + funcion_fibonacci(pos-2)

posicion = int(input("Ingrese una posicion en la secuencia de fibonacci para saber su valor: "))
print(funcion_fibonacci(posicion))

print("/////////////////////////////////////////////")
# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛 𝑚 = 𝑛 ∗ 𝑛 (𝑚−1) . Prueba esta función en un algoritmo general.

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
    
print("/////////////////////////////////////////////")
# 4) Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(num_decimal):
    if num_decimal == 0:
        return ""
    else:
        return decimal_a_binario(num_decimal // 2) + str(num_decimal % 2)

num_decimal = int(input("Ingrese un numero positivo en base numeral: "))
if num_decimal == 0:
    print("0")
else:
    print(decimal_a_binario(num_decimal))

print("/////////////////////////////////////////////")
# Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

palabra = str(input("Ingrese una palabra para ver si es palindromo: "))
print(es_palindromo(palabra)) 

print("/////////////////////////////////////////////")
# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.

def suma_digitos(numero_a_sumar):
    if numero_a_sumar < 10:
        return numero_a_sumar
    return (numero_a_sumar % 10) + suma_digitos(numero_a_sumar // 10)

numero_a_sumar = int(input("Ingrese un numero entero positivo para ver la suma de todos su digitos: "))
print(suma_digitos(numero_a_sumar))

print("/////////////////////////////////////////////")
# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque. Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
# nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.

def contar_bloques(num_bloques):
    if num_bloques == 1:
        return 1
    return num_bloques + contar_bloques(num_bloques - 1)

num_bloques = int(input("Ingrese la cantidad base de bloques de la piramide: "))
print(contar_bloques(num_bloques))

print("/////////////////////////////////////////////")
# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    ultimo = numero % 10
    resto = numero // 10
    
    if ultimo == digito:
        return 1 + contar_digito(resto, digito)
    else:
        return contar_digito(resto, digito)
    
numero = int(input("Ingrese un numero entero positivo: "))
digito = int(input("Ingrese un digito del 0 al 9: "))
print(contar_digito(numero, digito))