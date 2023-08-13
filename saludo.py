import os
os.system("cls")
print()

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "No es posible dividir entre cero"

operacion = input("Ingrese la operación (+, -, *, /): ")

if operacion in ('+', '-', '*', '/'):
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if operacion == '+':
        resultado = suma(num1, num2)
    elif operacion == '-':
        resultado = resta(num1, num2)
    elif operacion == '*':
        resultado = multiplicacion(num1, num2)
    elif operacion == '/':
        resultado = division(num1, num2)

    print(f"El resultado de {num1} {operacion} {num2} es: {resultado}")
else:
    print("Operación no válida. Por favor, ingrese una operación válida.")

print()
os.system('pause')
os.system('cls')