# Escribe un programa que pida un número y después nos informe si el número es divisible por 2,
# de no ser así compruebe si es divisible por 3 e informe y si tampoco es así, si es divisible por 5 e informe.
x = int(input("Introduce un número: "))
if(x%2==0):
    print("Es divisible por 2")
elif(x%3==0):
    print("Es divisible por 3")
elif(x%5==0):
    print("Es divisible por 5")