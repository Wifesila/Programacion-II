import os
os.system("cls")
print()
#-------------------------------------------
class libro:
    def __init__(self, titulo, autor, paginas, disonible):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponible = disonible

    def prestar(self, pedido):
        self.pedido = pedido
        if(self.pedido):
            return "El libro no esta disponible para el préstamo."
        else:
            return "El libro si esta disponible para el préstamo."
        
    def devolver(self, regresar):
        self.regresar = regresar
        if(self.regresar):
            return "el libro ya estaba disponible."
        else:
            return "el libro ya no esta disponible."
        
    def informacion(self, info):
        self.info = info
        if(self.info):
            return "El libro: Quijote, Autor: Cervantes, Paginas: 5000, Estado: disponible."
        else:
            return "No hay info de ese libro."
        
    def __str__(self):
        return 'El libro {} del autor {} tiene un total de {} paginas y esta {}'.format(self.titulo, self.autor, self.paginas, self.disponible, objUltimo.pedido(True))

objUltimo = libro('Quijote', "Cervantes", 45000, 'Rojo')
print(str(objUltimo.))

#-------------------------------------------
print()
os.system('pause')
os.system('cls')