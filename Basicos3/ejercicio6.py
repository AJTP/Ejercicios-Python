# Escribir un programa que almacene las asignaturas de un curso (por ejemplo
# Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
# nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas.
# Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene
# que repetir.

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
