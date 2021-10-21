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
