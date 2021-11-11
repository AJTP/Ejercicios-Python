# Desarrollar un módulo que solicite al usuario el ingreso de un nombre de usuario y contraseña y que los valide
# utilizando los módulos generados en los dos ejercicios anteriores. Ayuda: para contar la cantidad de caracteres
# de una cadena, en Python se utiliza la función incorporada: len(cadena).

from Basicos7.ejercicio4 import Usuario
from Basicos7.ejercicio5 import Password

while True:
    usuario = input("Introduce el usuario: ")
    pwd = input("Introduce la contraseña: ")
    u = Usuario(usuario)
    p = Password(pwd)
