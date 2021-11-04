# Escribir un programa en Python que pida al usuario su peso (en kg) y su estatura (en cm) y calcule su índice de
# masa corporal y lo almacene en una variable. A continuación, debe mostrar por pantalla la frase
# “Tu índice de masa corporal es …”, redondeado con dos decimales.

p = int(input("Introduce tu peso(kg): "))
e = int(input("Introduce tu estatura (cm): "))
e=e/100
r = round(p/(e*e),2)
print("Tu indice de masa corporal es: ",r)