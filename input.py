edad = 18
if(edad >=18):
    print('Es mayor de edad')
else:
    print('No eres mayoe de edad')

#---------------------

edad = 20
if edad < 18 and edad > 0:
    print("niños")
elif edad >=18 and edad <=35:
    print('pos adolesente')
elif edad >35 and edad <=60:
    print('Adultos')
else:
    print('Adultos mayores')    

print("###########################################")

#--------------------

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
        return "##### Error #####. No se puede dividir entre cero."

while True:
    print("Calculadora sencilla")
    print("A continuacion digite los numeros que quiera")
    print("Usando las peraciones disponibles: suma -->(+), resta -->(-), multiplicar -->(*), dividir -->(/)")
    
    num1 = float(input("Ingrese el primer número: "))
    operacion = input("Ingrese el simbolo de la operación que desea realizar |+|,|-|,|*| o |/|): ")
    num2 = float(input("Ingrese el segundo número: "))
    
    if operacion == "+":
        resultado = suma(num1, num2)
    elif operacion == "-":
        resultado = resta(num1, num2)
    elif operacion == "*":
        resultado = multiplicacion(num1, num2)
    elif operacion == "/":
        resultado = division(num1, num2)
    else:
        print("Elija una opción correcta por favor")
        continue
    
    print("Resultado:", resultado)

os.system('pause')


