# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un
# palíndromo.

x = list(input("Introduce una palabra: "))
lista = []

for letra in x:
    lista.append(letra)

lista.reverse()

if lista==x:
    print("Es un palindromo")
else:
    print ("No es un palindromo")