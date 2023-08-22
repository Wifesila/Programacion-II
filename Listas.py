import os
os.system("cls")
print("--------------------------------------")

# varlista = ["Hector", True, 5.5, 9]

# print(varlista[0])
# print(varlista[1])
# print(varlista[2])
# print(varlista[3])

# for z in varlista:
#     print(z)

# W = len(varlista)
# q = 0

# while q < len (varlista):
#     print(varlista[q])
#     q +=1
#########################
# del varlista [0]
# varlista.insert(1, "cual?")
# varlista.append("USCO")
# varlista.append(input("Inserte ciudad: "))

# eliminar = input("Digite el valor a eliminar: ")
# contador = 0

# for z in varlista:
#     if eliminar == z:
#         del varlista[contador]
#     else:
#         contador *=1

# print(varlista)
#########################
datos = [["hector", "sanchez", 36], ["maria", "lugo", 28],["juan","silva", 17]]

# print(datos[1][2])

for w in datos:
    print(w)
print("________")
for z in datos:
    for u in z:
        print(u)
    print("........")

print("--------------------------------------")
os.system('pause')
os.system('cls')