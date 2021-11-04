# Escribir un programa que pida una frase e indique si es un palíndromo.

def palindromo(palabra):
    aux = palabra[::-1]
    if palabra==aux:
        return True
    else:
        return False

x = input("Introduce una palabra: ")

if palindromo(x):
    print("Es Palindromo")
else:
    print("NO es Palindromo")