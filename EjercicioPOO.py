# Con una clase por medio de una lista o un diccionario almacenar
# las caracteristicas de 10 personas (Nombre, apellio, edad, email)
# para luego en dos casas A y B meter las caracteristicas de las personas 
# de manera aleatorea.  

import os
import random
os.system("cls")
print()
#-------------------------------------------------

class Personas:

    def __init__(self, nombre, apellido, edad, email):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.email = email

personas10 = []# Lista vacia que almacena las carcteristicas de las 10 personas.

for i in range(10):
    nombre = input(f"Escriba el nombre de la {i + 1} persona: ")
    apellido = input(f"Escriba el apellido de la {i + 1} persona: ")
    edad = (input(f"Escriba la edad de la {i + 1} persona: "))
    email = input(f"Escriba el correo electrónico de la {i + 1} persona: " )
    print("..................................................................................................")
    persona = Personas(nombre, apellido, edad, email)
    personas10.append(persona)


Gryffindor = [] # Colocar las caracteristicas de las personas aleatoreamente en
Slytherin = [] # Colocar las caracteristicas de las personas aleatoreamente en

for persona in personas10:
    if random.choice([True, False]):
        Gryffindor.append(persona)
    else:
        Slytherin.append(persona)

# Mostrar las caracteristicas de las personas en Griff.. y en Slythe..
print("-------------------------------------------")
print("Personas en la casa Gryffindor: ")
for persona in Gryffindor:
    print(f"Nombre: {persona.nombre}, Apellido: {persona.apellido}, Edad: {persona.edad} años, Email: {persona.email}" )
print("-------------------------------------------")
print("Personas en la casa Slytherin: ")
for persona in Slytherin:
    print(f"Nombre: {persona.nombre}, Apellido: {persona.apellido}, Edad: {persona.edad} años, Email: {persona.email}" )

#-------------------------------------------------
print()
os.system("pause")
os.system("cls")