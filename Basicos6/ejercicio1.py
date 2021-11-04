class Alumno:

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre: ", self.nombre, "Nota: ", self.nota)

        if self.nota>=5:
            print("Aprobado")
        else:
            print("Suspenso")

alumno1 =Alumno("Paco",6)
alumno2 = Alumno("Juan",3)
alumno1.imprimir()
alumno2.imprimir()
