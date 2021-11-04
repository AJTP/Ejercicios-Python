# Escribir una función que determine si una letra dada es consonante.

def consonante(letra):
    consonantes = {'a','e','i','o','u'}
    if letra not in consonantes:
        return True
    else:
        return False


x = input("Introduce una letra: ")

if consonante(x[0]):
    print("Es una consonante")
else:
    print("Es una vocal")