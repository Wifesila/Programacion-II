import os
os.system("cls")
print("-------------------------------------------")
print()
################################################
# 1. Escriba una función que muestre por consola un 
# saludo personalizado. Por ejemplo ‘¡Hola mundo!’

def saludo(nombre): # Definicion de una funcion que toma el parametro nombre
    mensaje = f"¡Hola {nombre}!" # Dentro de la funcion se coloca una variable con una cadena formateada (f-string), donde {} es una marcador de posicion
    print(mensaje) # Imprime el valor de la variable

saludopersonalizado = "compay como vas" # Variable que se le coloca el valor "compay..."
saludo(saludopersonalizado) # llamado a la funcion que toma como argumento "saludopersonalizado"

################################################
# 2. Escriba una función que reciba un nombre por parámetro
# y que luego muestre en pantalla ¡Hola <nombre>!

# def saluda(nombre): # Definicion de una funcion que toma el parametro nombre
#     Loquevaadecir = f"¡Hola {nombre}!" # Dentro de la funcion se coloca una variable con una cadena formateada (f-string), donde {} es un marcador de posicion
#     print(Loquevaadecir) # Imprime el valor de la variable

# Elnombre = "Rodrigo Pepito" # Variable que se le coloca el valor "Rodri..."
# saluda(Elnombre) # llamado a la funcion que toma como argumento "Elnombre" 

################################################
# 3. Cree una función que le pida al usuario su nombre y 
# su edad, luego muestre en pantalla los resultados.

# def nombre_y_edad(): # Se define una funcion llamada "nombre_y_edad"
#     Nombre = str(input("Por favor escriba su nombre o nombres: ")) # Se le dice al usuario que ingrese usando la funcion str() por si escribe algo que no sea cadena, para que luego lo almacene en la variable
#     Edad = input("Por favor escriba cuantos años tiene: ") # Se le dice al usuario que ingrese, para que luego lo almacene en la variable
#     print()
#     print(f"Su nombre es: {Nombre}") # Muestra los resusltados usando cadenas formateadas, donde {} es un marcador de posicion
#     print(f"Su edad es: {Edad} Años") # Muestra los resusltados usando cadenas formateadas, donde {} es un marcador de posicion

# nombre_y_edad() # Llamado a la funcion para obtener los datos del usuario

################################################
# 4. Definir una función que reciba n cantidad de números 
# por parámetros y que luego los sume, reste, mutiplique y divida.

# def operaciones(*args): # Definicion de funcion que acepta un numero variable de argumentos (*args) o argumentos posicionales arbitrarios 
#     sumar = 0 # variable que se le asigna un valor para alamacenar resultados en las operaciones
#     restar = 0
#     multiplicar = 1
#     dividir = 1
#     for num in args: # Iteracion atravez de todos los numeros como argumentos
#         sumar += num # realizacion de operaciones en cada numero para luego actualizar en las variables correspondientes  
#         restar -= num
#         multiplicar *= num

#         if num != 0: # Verificacion que el numero no sea 0 para evitar una divicion
#             dividir /= num
#     print(f"La suma es = {sumar} ") # Muestra de resultados con cadena formateada
#     print(f"La resta es = {restar} ")
#     print(f"La multiplicación es = {multiplicar} ")
#     print(f"La división es = {dividir} ")

# operaciones(10,5,3) # llamado a la funcion "operaciones" con los numeros a operar como argumentos

################################################
print()
print("-------------------------------------------")
os.system('pause')
os.system('cls')