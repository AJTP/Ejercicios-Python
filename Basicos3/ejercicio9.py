x = input("Introduce una palabra: ")
vocales = ['a', 'e', 'i', 'o', 'u']

for vocal in vocales:
    print("Tiene ", x.count(vocal), " veces la ", vocal)