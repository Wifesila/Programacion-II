#1. Escriba un programa que almacene la cadena de caracteres contraseña en una 
# variable, para luego preguntarle al usuario por la contraseña. 
# Luego, imprima en la consola si la contraseña que el usuario ingreso coincide con 
# la guardada en variable.

#2. Realice un programa que le pida al usuario dos números por teclado y muestre por 
# consola su división. Si el divisor es cero el programa debe mostrar un error y solicitar
#nuevamente el numero.

#3. Escriba un programa que le pida al usuario por teclado un numero entero y 
# muestre en consola si es par o impar.

#4. Escriba que mediante un vector  de 5 item, lea cada item y evalué el ingreso a menores de 
# edad, si la persona tiene menos de 19 años el programa le debe mostrar 
#en pantalla que ¡No puede ingresar!, de caso contrario que le diga ¡Bienvenido!
import os
os.system("cls")
print("--------------------------------------")

print("PRIMER EJERCICIO")
sistContraseña = '2023'
ingrContraseña2 = input("Escriba la contraseña del sistema: ")

if ingrContraseña2 == sistContraseña:
    print("Acceso concedido. ")
else:
    print("X acceso denegado X")


print("SEGUNDO EJERCICIO")
def main():
    while True:
        try:
            dividendo = float(input("Ingrese el dividendo: "))
            divisor = float(input("Ingrese el divisor: "))
            
            if divisor == 0:
                print("Error: No se puede dividir por cero. Intente nuevamente.")
            else:
                division = dividendo / divisor
                print(f"La división de {dividendo} entre {divisor} es: {division}")
                break
        except ValueError:
            print("Error: Ingrese números válidos.")

if __name__ == "__main__":
    main()



print("TERCER EJERCICIO")
def main():
    try:
        numero = int(input("Ingrese un número entero: "))
        
        if numero % 2 == 0:
            print(f"El número {numero} es par.")
        else:
            print(f"El número {numero} es impar.")
    except ValueError:
        print("Error: Ingrese un número entero válido.")

if __name__ == "__main__":
    main()

print("CUARTO EJERCICIO")

def main():
    vector_edades = []  # Creamos un vector para almacenar las edades

    for i in range(5):
        try:
            edad = int(input(f"Ingrese la edad de la persona {i + 1}: "))
            vector_edades.append(edad)
        except ValueError:
            print("Error: Ingrese una edad válida.")

    for i, edad in enumerate(vector_edades):
        if edad < 19:
            print(f"Persona {i + 1}: No puede ingresar.")
        else:
            print(f"Persona {i + 1}: ¡Bienvenido!")

if __name__ == "__main__":
    main()







print("--------------------------------------")
os.system('pause')
os.system('cls')
