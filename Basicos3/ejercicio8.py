# Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22,
# 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

Lista = [50, 75, 46, 22, 80, 65, 8]

Lista.sort()

print("Menor: ",Lista[0])
print("Mayor: ",Lista[len(Lista)-1])