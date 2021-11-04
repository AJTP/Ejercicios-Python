# Vamos a hacer un programa que nos pida introducir números hasta que una entrada se deje vacía.
# El programa debe ir contando cuántos números se introducen y la suma de esos números.

c=0;
s=0;
while(1):
    x = input("Introduce un número: ")
    if(x.isdigit()):
        x = int(x)
        c=c+1
        s=s+x
    else:
        break;
print("Introducidos: ",c,"Suma: ",str(s))
