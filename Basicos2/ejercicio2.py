n1 = int(input("Introduce el primer número: "))
n2 = int(input("Introduce el segundo número: "))
n3 = int(input("Introduce el tercer número: "))

if n1>n2 and n1>n3:
    maximo=n1
elif n3>n2 and n3>n1:
    maximo=n3
else:
    maximo=n2

if n1 < n2 and n1 < n3:
    minimo = n1
elif n3 < n2 and n3 < n1:
    minimo = n3
else:
    minimo = n2

print ("Máximo: ",maximo)
print ("Mínimo: ",min(n1,n2,n3))
print ("Media: ",(n1+n2+n3)/3)