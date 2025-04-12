print("Ejercicio 1")
print("Hola Mundo")

print("************************************************")

print("Ejercicio 2")

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}, bienvenido!")

print("************************************************")

print("Ejercicio 3")

print("A continuación, complete el siguiente formulario")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugarDeResidencia = input("Ingrese su lugar de residencia: ")

print(f"Según la información proporcionada usted es {nombre} {apellido}, su edad es {edad} y reside en {lugarDeResidencia}")
print("************************************************")

print("Ejercicio 4")

radio = input("Ingrese el radio de un circulo: ")
area = 3.14 * float(radio) ** 2
perimetro = 2 * 3.14 * float(radio)
print(f"El area del circulo es {area} y el perimetro es {perimetro}")
print("************************************************")

print("Ejercicio 5")

segundos = input("Ingrese la cantidad de segundos para saber a cuantas horas equivale: ")
horas = int(segundos) // 3600

print(f"{segundos} segundos son {int(horas)} horas")
print("************************************************")

print("Ejercicio 6")

numero = input("Ingrese un numero para saber su tabla de multiplicar: ")

print (f"La tabla de multiplicar de {numero} es: ")
print (f"{numero} x 1 = {int(numero) * 1}")
print (f"{numero} x 2 = {int(numero) * 2}")
print (f"{numero} x 3 = {int(numero) * 3}")
print (f"{numero} x 4 = {int(numero) * 4}")  
print (f"{numero} x 5 = {int(numero) * 5}")
print (f"{numero} x 6 = {int(numero) * 6}")  
print (f"{numero} x 7 = {int(numero) * 7}")
print (f"{numero} x 8 = {int(numero) * 8}")  
print (f"{numero} x 9 = {int(numero) * 9}")
print (f"{numero} x 10 = {int(numero) * 10}")
print("************************************************")

print("Ejercicio 7")
input("Este programa calcula la suma, multiplicación, división y resta de 2 numeros enteros dados")
num1 = input("Ingrese el primer numero: ")
num2 = input("Ingrese el segundo numero: ")

print(f"La suma de {num1} y {num2} es {int(num1) + int(num2)}")
print(f"La multiplicación de {num1} y {num2} es {int(num1) * int(num2)}")
print(f"La división de {num1} y {num2} es {int(num1) / int(num2)}")
print(f"La resta de {num1} y {num2} es {int(num1) - int(num2)}")
print("************************************************")

print("Ejercicio 8")

print("Este es un programa para saber su Indice de Masa Corporal")
altura = input("Ingrese su altura en metros: ")
peso = input("Ingrese su peso en kilos: ")
IMC = float(peso) / float(altura) ** 2

print(f"Segun la información proporcionada su Indice de Masa Corporal es {IMC}")
print("************************************************")

print("Ejercicio 9")

print("Este es un programa para convertir grados Celcius a Farenheit")
celcius =input("Ingrese la temperatura en Celcius: ")

farenheit = 9/5 * float(celcius) + 32

print(f"La temperatura en grados Farenheit es {farenheit}")
print("************************************************")

print("Ejercicio 10")

print("Este programa calcula el promedio de 3 numeros enteros ingresados")
num1 = input("Ingrese el primer numero: ")
num2 = input("Ingrese el segundo numero: ")
num3 = input("Ingrese el tercer numero: ")

promedio = (int(num1) + int(num2) + int(num3)) / 3

print(f"El promedio de los 3 numeros es {promedio}")
print("************************************************")
