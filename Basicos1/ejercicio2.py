# Escribe un programa que nos pida el nombre del usuario y compruebe la longitud en caracteres del nombre introducido.
# Nos dirá si el nombre es largo o se trata de un nombre corto y además en el caso de que el nombre sea largo,
# nos debe decir si el nombre es compuesto o no.

x = str(input("Introduce tu nombre: "))
if(len(x)>7):
    print("Es largo")
    if(' ' in x):
            print("Es compuesto")
else:
    print("Es corto")