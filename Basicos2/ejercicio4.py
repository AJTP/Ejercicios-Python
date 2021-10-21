d = int(input("Introduce un número: "))
cadena = ""
while d > 1:
    cadena += str(int(d % 2))
    d = d / 2
print(cadena[::-1])
