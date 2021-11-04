# Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá
# las palabras en español e inglés separadas por dos puntos, y cada
# par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las
# palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para
# traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.

cadena = input("Introduce las palabras <palabra>:<traduccion>: ")
par = cadena.split(',')
dic={}
for i in par:
    palabras = i.split(':')
    dic[palabras[0]]=palabras[1]
frase = input("Introduce una frase a traducir: ")
palabra = frase.split(' ')
for j in palabra:
    if j in dic:
        print(dic[j], end=' ')
