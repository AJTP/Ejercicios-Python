# Escribir un algoritmo que, para una suma de dinero dada, indique
# cómo descomponerla en billetes y monedas corrientes. Se desea utilizar el mínimo de
# billetes y monedas. No hay ninguna limitación respecto al número de billetes y
# monedas disponibles.

cantidades = [500, 200, 100, 50, 20, 10, 5, 2, 1]
dinero = int(input("Introduce la cantidad de dinero: "))

for i in cantidades:
    c = int(dinero/i)
    dinero=dinero%i
    if c>0:
        if i > 5:
            if c>1:
                print(c," billetes de", i)
            else:
                print(c, " billete de", i)
        else:
            if c > 1:
                print(c, " monedas de", i)
            else:
                print(c, " moneda de", i)
