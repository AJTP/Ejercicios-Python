# Una panadería vende barras de pan a 0.69€ cada una. El pan que no es el día tiene un descuento del 60%.
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día.
# Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que
# se le hace por no ser fresca y el coste final total.

p = 0.69
x = int(input("Introduce el número de barras: "))
d = p * 60 / 100
print("Precio habitual: ", p * x, "Descuento: ", d * x, "Coste final: ", round((p - d) * x, 2))
