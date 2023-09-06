import os
os.system("cls")
print()
#-------------------------------------------

# 1. Escriba un programa que almacene (Input) en una Lista las materias que has cursado con sus respectivas notas
# . Luego muestre la lista por consola mediante un ciclo.

# notasdelasmaterias = []

# numerodematerias = int(input("Escriba el numero de cursos que has visto: "))

# for i in range(numerodematerias):
#     curso = input(f"Escriba el nombre del curso {i + 1} por favor: ")
#     nota = float(input(f"Escriba la nota del curso {i + 1} por favor: "))
#     notasdelasmaterias.append((curso, nota))

# print("Notas definitivas: ")
# for curso, nota in notasdelasmaterias:
#     print(f"Del curso: {curso}, su nota es: {nota}")
#-------------------------------------------------
# 2. Escriba un programa que almacene personas (input), luego que le muestre 
# por pantalla el mensaje de ‘Su nombre es ‘nombre’

# comosellama = input("Escriba su nombre por favor: ")
# print(f"Usted se llama {comosellama}")
#-------------------------------------------------
# 3. Escribir un programa que guarde en una variable un diccionario con los siguientes valores 
# {'Euro':'€', 'Dollar':'$', 'Yen':'¥'} Luego pregunte al usuario por una divisa y el valor en pesos a convertir. Luego muestre en consola el 
# símbolo con el valor que corresponde a la divisa o un mensaje de advertencia si esa divisa no se encuentra en el diccionario.

# Divisas = {"Euro": "€", "Dollar": "$", "Yen": "¥"}

# Divisa = input("Escriba una divisa: ")
# Valorenpesos = float(input("Escriba el valor en pesos a convertir por favor: "))

# if Divisa in Divisas:
#     Simbolo = Divisas[Divisa]
#     print(f"{Simbolo}{Valorenpesos}")
# else:
#     print("Esa divisa no se encuentra en el diccionario.") 
#-------------------------------------------------
# 4. En una tupla coloque o ingrese (input) los siguientes valores: números enteros, 
# decimales, String, colecciones. Luego muestre en consola que tipo de datos o variable son los valores digitados.

# ingrasardatos = input("Escriba valores separdos por comas: ")

# valores = ingrasardatos.split(",")

# for valor in valores:
#     valor = valor.strip()

#     if valor.isdigit():
#         print(f"{valor} ---> es un numero entero")
#     elif valor.replace(".","", 1).isdigit():
#         print(f"{valor} ---> es un numero decimal.")
#     else:
#         print(f"{valor} ---> es una cadena de texto.")
#-------------------------------------------
print()
os.system('pause')
os.system('cls')