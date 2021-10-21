facturas={}
cobrado=0
while True:
    print("\n1. Añadir factura")
    print("2. Pagar factura")
    print("0. Terminar")
    opcion = int(input("Introduce una opcion: "))

    if opcion==1:
        num = input("Introduce el numero de factura: ")
        coste = int(input("Introduce el coste: "))
        facturas[num] = coste
    if opcion ==2:
        num = input("Introduce el numero de factura a eliminar: ")
        cobrado = cobrado+facturas[num]
        del facturas[num]

    pendiente=0
    for i,j in facturas.items():
        pendiente = pendiente+j

    print("Cobrado: ", cobrado, "Pendiente: ", pendiente)

    if opcion == 0:
        break