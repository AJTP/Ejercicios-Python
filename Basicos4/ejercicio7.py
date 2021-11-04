# Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura
# y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva
# factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el
# número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el
# programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.

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