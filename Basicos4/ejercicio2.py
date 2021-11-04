# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte
# al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de
# kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

dicFrutas = {'Plátano': 1.35, 'Manzana': 0.8, 'Pera': 0.85, 'Naranja': 0.7}
fruta = input("Introduce una fruta: ")
kilos = int(input("Introduce los kilos de fruta: "))

if fruta in dicFrutas:
    print("Precio: ", (kilos * dicFrutas[fruta]))
else:
    print("La fruta no está en el diccionario")