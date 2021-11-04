# Escribir una función que calcule el factorial de un número. Por ejemplo, 5! =
# 5*4*3*2*1 = 120.
def factorial(numero):
    if numero>1:
        return numero*factorial(numero-1)
    else:
        return numero

x = int(input("Introduce un numero: "))

print("Resultado:",factorial(x))