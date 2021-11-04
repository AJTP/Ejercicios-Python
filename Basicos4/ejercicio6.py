# Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa
# debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida
# terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total

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