fecha = input("Introduce la fecha: ")
anio = 2000 + int(fecha[len(fecha)-2:])
mes = int(fecha[len(fecha)-4:len(fecha)-2])
dia = int(fecha[:len(fecha)-4])
cadena = '%d-%d-%d' % (dia, mes, anio)

print (cadena)