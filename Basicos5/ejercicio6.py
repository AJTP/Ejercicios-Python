# Escribir una función que pida una cadena de caracteres y que devuelva cuántos de
# ellos son mayúsculas.

def mayusculas(cadena):
    contador = 0
    for i in range(len(cadena)):
        if cadena[i].isupper():
            contador = contador + 1
    return contador


x = input("Introduce una palabra: ")

print("Contiene ", mayusculas(x), " mayusculas")
