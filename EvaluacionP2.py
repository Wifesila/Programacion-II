import os
os.system("cls")
print()
#-------------------------------------------
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

class Perro(Animal):
    def __init__(self, nombre, raza, contextura):
        super().__init__(nombre)
        self.raza = raza
        self.contextura = contextura

    def ladrar(self):
        print(f"{self.nombre} está ladrando")

    def hacer_sonido(self):
        print(f"{self.nombre} está haciendo un sonido de perro")

mi_perro = Perro("Max", "Labrador", "Delgada")

mi_perro.hacer_sonido()

mi_perro.ladrar()

#-------------------------------------------
print()
os.system('pause')
os.system('cls')
