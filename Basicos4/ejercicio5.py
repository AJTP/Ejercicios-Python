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
