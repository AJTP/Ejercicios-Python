Lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Lista2 = []

c=0
for i in Lista:
    if c%3==0 :
        Lista2.append(i)
    c = c + 1

for a in Lista2:
    if a in Lista :
        Lista.remove(a)

for a in Lista:
    print(a)