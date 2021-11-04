# Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los
# clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor
# será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente),
# donde preferente tendrá el valor True si se trata de un cliente preferente. El programa debe
# preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente,
# (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En
# función de la opción elegida el programa tendrá que hacer lo siguiente:
# 1. Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de
# datos.
# 2. Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
# 3. Preguntar por el NIF del cliente y mostrar sus datos.
# 4. Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
# 5. Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
# 6. Terminar el programa.
clientes={}

while True:
    print("\n1. Añadir cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Listar todos los clientes")
    print("5. Listar clientes preferentes")
    print("6. Terminar")
    opcion = int(input("Introduce una opcion: "))

    if opcion==1:
        dni = input("Introduce el DNI: ")
        nombre = input("Introduce el nombre: ")
        direccion = input("Introduce la dirección: ")
        telefono = input("Introduce el telefono: ")
        correo = input("Introduce el correo: ")
        x = int(input("¿Es preferente?(1->Si,0->No): "))
        if x > 0:
            preferente = True
        else:
            preferente = False

        datos = {'nombre': nombre, 'direccion': direccion, 'telefono': telefono, 'correo': correo,
                 'preferente': preferente}
        clientes[dni] = datos
    if opcion ==2:
        dni = input("Introduce el DNI a eliminar: ")
        del clientes[dni]
    if opcion == 3:
        dni = input("Introduce el DNI  a consultar: ")
        datos = clientes[dni]
        for i, j in datos.items():
            print(i, "\t", j)
    if opcion == 4:
        for i, j in clientes.items():
            print(i, "\t", j['nombre'])
    if opcion == 5:
        for i, j in clientes.items():
            if j['preferente'] == True:
                print(i, "\t", j['nombre'])
    if opcion == 6:
        break
