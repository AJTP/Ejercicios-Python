def superposicion(l1, l2):
    for i in l1:
        if i in l2:
            return True
    return False


lista1 = []
lista2 = []
for i in range(3):
    lista1.append(input("Palabra Lista1: "))
for i in range(3):
    lista2.append(input("Palabra Lista2: "))

if superposicion(lista1, lista2):
    print("Tienen al menos un elemento en común")
else:
    print("No tienen elementos en común")
