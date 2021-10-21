Lista = ["Matemáticas","Física","Química","Historia","Lengua"]
Lista2 = []
for i in Lista:
    m = int(input("Introduce la nota de {}: ".format(i)))
    if m>=5:
        Lista2.append(i)

for i in Lista2:
    Lista.remove(i)

print("\nDeberás repetir: ")
for i in Lista:
    print(i)
