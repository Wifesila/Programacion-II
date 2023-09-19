import os
os.system("cls")
print("--------------------------------------------------------------------")
########################################################

MiLista = ["León", "Perro", "Gato", "Zebra"] # ||| Lista original||| #

print(f"{MiLista} <--- LA ORIGINAL")

MiLista_1 = MiLista.copy() # Copia de la original
MiLista_2 = MiLista # Copia sin metodo

MiLista.insert(-1,"Hipopótamo") # Añade en cualaquier lugar especifico
#--------------[^]---------------#
#       ---> Posición <---       #
print(MiLista)
print(f'{MiLista[-1]} <--- La posición "3" de la lista en ese momento')
 
MiLista.append("Jirafa") # Añade solo al final

MiLista[2] = "Leopardo" # Remplazo Gato ---> Leopardo
print(MiLista)

MiLista.pop(1) # Elimina solo a el de la posición indicada 
print(MiLista)

MiLista.append("Coco")
print(MiLista)

MiLista.remove("Coco") # Borra al elemento especificado de manera escrita 
print(MiLista)

MiLista.clear() # Borra todo el contenido
print(f"{MiLista} <---- Se ha quedado vacia la original editada")

print(f"MiLista_1.0: {MiLista_1} <-- ClonDelaOriginal")
print(f"MiLista_2.0: {MiLista_2} <-- ClonDelaOriginalEditada")

MiLista_2.append("Manzana")
MiLista_2.append("Pera")
MiLista_2.append("Manzana")
MiLista_2.append("Uva")
print(f"MiLista_2.0 con nuevos elemetos {MiLista_2}")

print(MiLista_2.count("Manzana")) # cuenta cuantas veces esta el elemento

MiLista_2.reverse() # Colocar al revez la pocisión de los elementos
print(f"{MiLista_2} Al revez")

MiLista_2.sort() # Ordena alfabeticamente y/o de < a >
print(MiLista_2)

ListaNueva = [4, 8, 23, 2]

ListaNueva.sort(reverse=True) # Ordena alfabeticamente de Z a A y/o de > a <
print(ListaNueva)

ListaNueva.extend(MiLista_2)
print(ListaNueva) 

ListaNueva.extend("123") # tomar cada elemento de Str como elemento
print(ListaNueva) 

print(f'De ListaNueva el numero menor es "{ListaNueva[-3]}" y el más grande es el "{ListaNueva[0]}".')
print(f'Imprimiendo desde ListaNueva la pocición 2, de pera: "{ListaNueva[6][2]}".')

print(f'Uva esta en la posición {ListaNueva.index("Uva")}.') # Indica la posición de lo buscado 

ListaColores = ["rojo", "azul", "verde", "amarillo"]
print(ListaColores)
ListaColores.insert(0, "gris")
ListaColores.insert(3, "naranja")
ListaColores.append("rosa")
print(ListaColores)

########################################################
print("--------------------------------------------------------------------")
os.system('pause')
os.system('cls')