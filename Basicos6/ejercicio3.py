# Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase
# con los métodos para inicializar los atributos, imprimir el valor del lado con un tamaño
# mayor y el tipo de triángulo que es (equilátero, isósceles o escaleno).

class Triangulo:

    def __init__(self):
        self.l1 = int(input("Introduzca el valor del primer lado: "))
        self.l2 = int(input("Introduzca el valor del segundo lado: "))
        self.l3 = int(input("Introduzca el valor del tecer lado: "))

    def mayor(self):
        if self.l1 > self.l2:
            if self.l1 > self.l3:
                print(self.l1)
            else:
                print(self.l3)
        else:
            if self.l2 > self.l3:
                print(self.l2)
            else:
                print(self.l3)
        if self.l1 == self.l2 == self.l3:
            print("Es Equilatero")
        elif self.l1 != self.l2 != self.l3:
            print("Es Escaleno")
        else:
            print("Es Isosceles")


t1 = Triangulo()
t1.mayor()
t2 = Triangulo()
t2.mayor()