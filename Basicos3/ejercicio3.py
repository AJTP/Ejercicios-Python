# Escribir un programa que almacene las asignaturas de un curso (por ejemplo,
# Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
# nota que ha sacado en cada asignatura, y después las muestre por pantalla con el
# mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una de las
# asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas
# por el usuario. Finalmente, debe mostrar la nota media de todas las asignaturas.

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