# Una juguetería tiene mucho éxito en dos de sus productos: tambores y patinetes.
# Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben
# calcular el peso de los tambores y patinetes que saldrán en cada paquete a demanda. Cada tambor pesa 112 g
# y cada patinete 975 g. Escribir un programa que pida el número de tambores y patinetes vendidos
# y calcule el peso total del paquete que será enviado.

t = int(input("Introduce la cantidad de tambores: "))*112
p = int(input("Introduce la cantidad de patinetes: "))*975
print("Peso total: ",t+p)
