# Escribir un programa que pregunte al usuario los números ganadores de la lotería
# primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor
# a mayor.

Lista = []
for i in range(6):
    x = int(input("Introduce un numero: "))
    Lista.append(x)

Lista.sort()

for i in Lista:
    print(i)