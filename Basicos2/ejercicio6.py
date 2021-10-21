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
