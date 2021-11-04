# Haremos un programa que estará pidiendo números pares indefinidamente hasta que se introduzca un número impar.
# El programa finalizará cuando se introduzca el primer número impar.

while(1):
    x = int(input("Introduce un numero: "))
    if(x%2!=0):
        break;