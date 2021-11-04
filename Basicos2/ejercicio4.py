# Escribir un algoritmo que, para un número decimal de 4 cifras, imprima su valor en
# base 2 (binario).
d = int(input("Introduce un número: "))
cadena = ""
while d > 1:
    cadena += str(int(d % 2))
    d = d / 2
print(cadena[::-1])
