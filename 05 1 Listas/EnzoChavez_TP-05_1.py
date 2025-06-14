# Práctico 5: Listas
# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

lista_multiplos = list(range(4, 101, 4))
print(lista_multiplos)

# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo.

cosas_escritorio = ["notebook", "mate", "lentes", "auriculares", "celular"]
print(cosas_escritorio[3])

# 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.

lista_vacia =[]
lista_vacia.append("yerba")
lista_vacia.append("yuyo")
lista_vacia.append("bombilla")

print(lista_vacia)

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. Imprimir la lista resultante por pantalla. 

animales = ["perro", "gato", "conejo", "pez"]
print(animales)
animales[1] = "loro"
animales[-1]= "oso"
print(animales)

# # 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

# """
# Lo que hace este programa es que de la lista de numeros dada, busca el numero mas alto con "max()" y luego lo saca de la lista con ".remove()" para terminar mostrando
# por pantalla la lista de numeros sin el mayor de ellos.
# """

# 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

numeros_lista = list(range(10, 31, 5))
print(numeros_lista[0:2])

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.

autos = ["sedan", "polo", "suran", "gol"]
print(autos)
autos[1]= "pato"
autos[2]= "pata"
print(autos)

# 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.

lista_dobles = []
lista_dobles.append(5*2)
lista_dobles.append(10*2)
lista_dobles.append(15*2)

print(lista_dobles)

# 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" a la lista del tercer cliente usando append.
compras[2].append("jugo")
print(compras[2])
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
compras[1][1] = "tallarines"
print(compras[1])
# c) Eliminar "pan" de la lista del primer cliente.
compras[0].remove("pan")
print(compras[0])
# d) Imprimir la lista resultante por pantalla
print(compras)

# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)

