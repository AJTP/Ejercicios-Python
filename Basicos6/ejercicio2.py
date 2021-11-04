class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir(self):
        print("Nombre: ", self.nombre, "Edad: ", self.edad)

        if self.edad>=18:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")

p1 =Persona("Paco",25)
p2 = Persona("Juan",15)
p1.imprimir()
p2.imprimir()