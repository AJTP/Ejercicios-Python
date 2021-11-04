# Consideremos una hora expresada en forma de tripleta. Escribir un algoritmo que
# imprima la hora correspondiente al siguiente segundo. Por ejemplo, para la entrada
# 13,43,24 tiene que devolver 13,43,25.

hora = input("Introduce la hora: ")
cadenas = hora.split(',')
datos = []
for i in range(len(cadenas)):
    t = int(cadenas[i])
    datos.append(t)

datos[2]+=1

if datos[2]==60:
    datos[2]=0
    datos[1]+=1
    if datos[1]==60:
        datos[1]=0
        datos[0]+=1
        if datos[0]==24:
            datos[0]=0

print(str(datos[0]) + "," + str(datos[1]) + "," + str(datos[2]))