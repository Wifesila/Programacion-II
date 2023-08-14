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
        raise ValueError("No se puede dividir entre cero.")

while True:
    try:
        operacion = input("Ingrese la operación ( +, -, *, / ) o la letra 's' para salir: ")

        if operacion == 's':
            break

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

            print()
            print(f"El resultado de {num1} {operacion} {num2} es igual a: {resultado}")
            print()
        else:
            print("||||               !!! Operación inválida ¡¡¡               ||||")
            print("Por favor, digite una operación indicada.")
            print()

    except ValueError as e:
        print("                    ##### Error #####                    ")
        print("Digite solo lo que se pide e intente de nuevo por favor.")
        print()

print()
os.system('pause')
os.system('cls')