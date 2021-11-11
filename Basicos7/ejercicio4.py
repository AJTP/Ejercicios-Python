# Desarrollar un módulo para validación de nombres de usuarios. Dicho módulo, deberá
# cumplir con los siguientes criterios de aceptación:
# • El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12
# • El nombre de usuario debe ser alfanumérico
# • Nombre de usuario con menos de 6 caracteres, retorna el mensaje “El nombre de usuario debe contener al menos 6 caracteres”
# • Nombre de usuario con más de 12 caracteres, retorna el mensaje “El nombre de usuario no puede contener más de 12 caracteres”
# • Nombre de usuario con caracteres distintos a los alfanuméricos, retorna el mensaje “El nombre de usuario puede contener solo letras y números”
# • Nombre de usuario válido, retorna True

def comprobarNombre(nombre):
    mensaje=""

    if len(nombre)<6:
        mensaje="El nombre de usuario debe contener al menos 6 caracteres"
        return mensaje
    if len(nombre)>12:
        mensaje = "El nombre de usuario no puede contener más de 12 caracteres"
        return mensaje
    if nombre.isalnum()==False:
        mensaje="El nombre de usuario puede contener solo letras y números"
        return mensaje

    return mensaje


class Usuario:
    nombre=""
    def __init__(self,nombre):
        mensaje = comprobarNombre(nombre)
        if mensaje=="":
            self.nombre=nombre
            print("Nombre correcto:",self.nombre)
        else:
            print(mensaje)


# usuario = Usuario("Pepito")
# usuario2 = Usuario("Ana")
# usuario3 = Usuario("Pruebaaaaaaaa")
# usuario4 = Usuario("%%AAAA")
