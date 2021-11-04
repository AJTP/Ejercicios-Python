# Realizar una clase que administre una agenda. Se debe almacenar para cada contacto
# el nombre, el teléfono y el email. Además, deberá mostrar un menú con las siguientes
# opciones
# • Añadir contacto
# • Lista de contactos
# • Buscar contacto
# • Editar contacto
# • Cerrar agenda

class Contacto:
    nombre = ""
    telefono = ""
    email = ""

    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email


class Agenda:
    contactos = []

    def add(self, contacto):
        self.contactos.append(contacto)

    def listar(self):
        for i in self.contactos:
            print("Nombre: ", i.nombre, " Telefono: ", i.telefono, " Email: ", i.email)

    def buscar(self, nombre):
        for i in self.contactos:
            if i.nombre == nombre:
                print("Nombre: ", i.nombre, " Telefono: ", i.telefono, " Email: ", i.email)

    def editar(self,nombre):
        for i in self.contactos:
            if i.nombre == nombre:
                while True:
                    print("1. Nombre")
                    print("2. Telefono")
                    print("3. Email")
                    x = int(input("¿Que deseas modificar?: "))

                    if x == 1:
                       i.nombre=input("Introduce el nuevo nombre: ")
                    elif x == 2:
                        i.telefono = input("Introduce el nuevo telefono: ")
                    elif x == 3:
                        i.email = input("Introduce el nuevo email: ")
                    else:
                        break
                break

agenda = Agenda()
while True:
    print("1. Añadir contacto")
    print("2. Listar contactos")
    print("3. Buscar contacto")
    print("4. Editar contacto")
    print("5. Cerrar agenda")
    x = int(input("¿Que deseas hacer?: "))

    if x == 1:
        c = Contacto(input("Introduce el nombre: "),input("Introduce el telefono: "),input("Introduce el email: "))
        agenda.add(c)
    elif x == 2:
        agenda.listar()
    elif x == 3:
        s = input("Introduce el nombre: ")
        agenda.buscar(s)
    elif x==4:
        s = input("Introduce el nombre: ")
        agenda.editar(s)
    else:
        break
