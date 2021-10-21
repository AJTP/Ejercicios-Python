productos={}
while True:
    producto = input("Introduce el nombre del producto: ")
    precio = int(input("Introduce el precio del producto: "))
    productos[producto]=precio
    continuar = int(input("¿Continuar? (1->Si,0->No)"))
    if continuar==0:
        break
print("Lista de la compra")
suma=0
for i,j in productos.items():
    print(i, "\t\t", j)
    suma=suma+j
print("Total\t", suma)