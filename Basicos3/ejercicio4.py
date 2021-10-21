Lista = []
for i in range(6):
    x = int(input("Introduce un numero: "))
    Lista.append(x)

Lista.sort()

for i in Lista:
    print(i)