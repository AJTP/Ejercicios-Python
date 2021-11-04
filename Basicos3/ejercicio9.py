# Escribir un programa que pida al usuario una palabra y muestre por pantalla el
# número de veces que contiene cada vocal.

x = input("Introduce una palabra: ")
vocales = ['a', 'e', 'i', 'o', 'u']

for vocal in vocales:
    print("Tiene ", x.count(vocal), " veces la ", vocal)