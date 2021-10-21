nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
direccion = input("Introduce tu direccion: ")
telefono = int(input("Introduce tu teléfono: "))
dic={'nombre':nombre, 'edad':edad, 'direccion':direccion, 'telefono':telefono}

print(dic['nombre'], "tiene", dic['edad'], "años, vive en", dic['direccion'], "y su numero de teléfono es", dic['telefono'])
