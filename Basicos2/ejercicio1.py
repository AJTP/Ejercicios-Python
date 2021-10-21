s = int(input("Introduce el número de segundos: "))
if s<1000000:
    d=int(s/86400)
    s-=d*86400
    h=int(s/3600)
    s-=h*3600
    m=int(s/60)
    s-=m*60;
    print("Dias ", d, " Horas ", h, " Minutos ", m, " Segundos ", s)



