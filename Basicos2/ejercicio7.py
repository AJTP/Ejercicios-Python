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