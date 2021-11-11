# Desarrollar un módulo para validación de contraseñas. Dicho módulo, deberá cumplir
# con los siguientes criterios de aceptación:
# • La contraseña debe contener un mínimo de 8 caracteres
# • Una contraseña debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico
# • La contraseña no puede contener espacios en blanco
# • Contraseña válida, retorna True
# • Contraseña no válida, retorna el mensaje “La contraseña elegida no es segura”

def comprobarNombre(nombre):
    ok = True
    mayuscula = False
    minuscula = False
    numero = False
    # Compruebo longitud
    if len(nombre) < 8:
        ok = False
        return ok

    # Compruebo que no tenga espacios
    if " " in nombre:
        ok = False
        return ok
    # Compruebo que tiene simbolos
    for letra in nombre:
        if letra.isupper():
            mayuscula = True
        if letra.islower():
            minuscula = True
        if letra.isnumeric():
            numero = True

    # Compruebo que tenga símbolo, una mayuscula, una minuscula y un número
    if nombre.isalnum() == True or mayuscula == False or minuscula == False or numero == False:
        ok = False
        return ok

    return ok


class Password:
    pwd = ""

    def __init__(self, pwd):
        ok = comprobarNombre(pwd)
        if ok:
            self.pwd = pwd
            print("Contraseña válida")
        else:
            print("La contraseña elegida no es segura")


# pwd1 = Password("eeeeeee")
# pwd2 = Password("e e e e e e e e")
# pwd3 = Password("Prueba1")
# pwd4 = Password("Prueba1@")
