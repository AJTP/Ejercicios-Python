def factorial(numero):
    if numero>1:
        return numero*factorial(numero-1)
    else:
        return numero

x = int(input("Introduce un numero: "))

print("Resultado:",factorial(x))