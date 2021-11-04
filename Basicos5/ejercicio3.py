# Escribir una función max() que tome como argumentos dos números e imprima el mayor.

def maximo(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

x = int(input("Introduce un numero: "))
x2 = int(input("Introduce otro numero: "))
print(maximo(x, x2), "es el mayor")
