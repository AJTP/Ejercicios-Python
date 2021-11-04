# Escribir un programa en Python que almacene las asignaturas de un curso (por
# ejemplo, Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre
# por pantalla.

Lista = []
m = int(input("Introduce la nota de Matemáticas: "))
Lista.append(m)
f = int(input("Introduce la nota de Física: "))
Lista.append(f)
q = int(input("Introduce la nota de Química: "))
Lista.append(q)
h = int(input("Introduce la nota de Historia: "))
Lista.append(h)
l = int(input("Introduce la nota de Lengua: "))
Lista.append(l)

for i in Lista:
    print(i)