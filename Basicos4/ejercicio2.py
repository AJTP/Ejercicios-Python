dicFrutas = {'Plátano': 1.35, 'Manzana': 0.8, 'Pera': 0.85, 'Naranja': 0.7}
fruta = input("Introduce una fruta: ")
kilos = int(input("Introduce los kilos de fruta: "))

if fruta in dicFrutas:
    print("Precio: ", (kilos * dicFrutas[fruta]))
else:
    print("La fruta no está en el diccionario")