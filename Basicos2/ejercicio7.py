# Escribir un algoritmo que simule el funcionamiento de una calculadora. El dato es
# una serie de tres caracteres: una cifra, un símbolo de operación y otra cifra. El
# resultado es el valor de la expresión dada.

cadena = input("Introduce una operación: ")
resultado = 0

cifras = cadena.split('+')
if len(cifras) == 2:
    resultado = int(cifras[0]) + int(cifras[1])
else:
    cifras = cadena.split('-')
    if len(cifras) == 2:
        resultado = int(cifras[0]) - int(cifras[1])
    else:
        cifras = cadena.split('*')
        if len(cifras) == 2:
            resultado = int(cifras[0]) * int(cifras[1])
        else:
            cifras = cadena.split('/')
            if len(cifras) == 2:
                resultado = int(cifras[0]) / int(cifras[1])

print (resultado)