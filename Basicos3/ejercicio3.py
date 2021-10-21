Lista = ["Matemáticas","Física","Química","Historia","Lengua"]
Notas = []
for i in Lista:
    m = int(input("Introduce la nota de {}: ".format(i)))
    Notas.append(m)
suma=0
for i in range(5):
    print("En ", Lista[i], " has sacado ", Notas[i])
    suma+=Notas[i]

print("Media: ",suma/6)