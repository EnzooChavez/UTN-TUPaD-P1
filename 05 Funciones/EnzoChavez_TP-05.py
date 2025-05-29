# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()


print("/////////////////////////////////////////////////")
# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre=input("Por favor, ingrese su nombre: ")
saludo = saludar_usuario(nombre)
print(saludo)


print("/////////////////////////////////////////////////")
# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}."


nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese donde reside: ")

frase = informacion_personal(nombre, apellido, edad, residencia)
print(frase)


print("/////////////////////////////////////////////////")
# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

def calcular_area_circulo(radio):
    area = 3.14 * (radio**2)
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.14 * radio
    return perimetro

radio = int(input("Ingrese el radio: "))
area_circulo = calcular_area_circulo(radio)
perimetro_circulo = calcular_perimetro_circulo(radio)
print(f"El area del circulo es {area_circulo} y el perimetro es {perimetro_circulo}")


print("/////////////////////////////////////////////////")
# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    horas = segundos /3600
    return f"{segundos} segundos son el equivalente a {horas} hora/s"

segundos = int(input("Ingrese una cantidad de segundos para saber cuantas horas son: "))
print(segundos_a_horas(segundos))


print("/////////////////////////////////////////////////")
# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range (1, 11):
        print(f"{numero} x {i} = {(numero) * i}")

numero = int(input("Ingrese un numero para saber su tabla de multiplicar: "))
tabla_multiplicar(numero)


print("/////////////////////////////////////////////////")
# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta= a - b
    multiplicacion = a * b
    division = a / b
    return (suma, resta, multiplicacion, division)

n1 = int(input("Ingrese el primero de dos numeros para conocer su suma, resta, multiplicacion y division: "))
n2 = int(input("Ingrese el segundo numero"))
resultados = operaciones_basicas(n1, n2)

print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicacion: {resultados[2]}")
print(f"Division: {resultados[3]}")


print("/////////////////////////////////////////////////")
# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    imc = (peso / (altura * altura))
    return imc

print("Este programa calcula su indice de masa corporal")
peso = int(input("Ingrese su peso: "))
altura = float(input("Ingerse su altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Su IMC es: {imc:.1f}")


print("/////////////////////////////////////////////////")
# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

def celcius_a_farenheit(celsius):
    en_farenheit = ((celcius * 9) / 5) + 32
    return en_farenheit

celcius = float(input("Ingrese una temperatura en grados celcius para conocer su equivalente en grados Farenheit: "))
farenheit = celcius_a_farenheit(celcius)
print(f"La temperatura en grados Farenheit es {farenheit}")


print("/////////////////////////////////////////////////")
# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

def calcular_promedio (a, b, c):
    promedio = (a + b + c) / 3
    return promedio

numero1 = int(input("Ingrese el primero de 3 numeros para conocer su promedio: "))
numero2 = int(input("Ingrese el segundo numero: " ))
numero3 = int(input("Ingrese el tercer numero: "))

promedio = int(calcular_promedio(numero1, numero2, numero3))
print(f"El promedio de los 3 numeros es {promedio}")