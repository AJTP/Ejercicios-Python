class Calculadora:

    def __init__(self):
        self.n1 = int(input("Introduzca el valor del primer numero: "))
        self.n2 = int(input("Introduzca el valor del segundo numero: "))

    def suma(self):
        print("El resultado de la suma es: ", (self.n1 + self.n2))

    def resta(self):
        print("El resultado de la resta es: ", (self.n1 - self.n2))

    def multiplicacion(self):
        print("El resultado de la multiplicacion es: ", (self.n1 * self.n2))

    def division(self):
        print("El resultado de la division es: ", (self.n1 / self.n2))


t1 = Calculadora()
t1.suma()
t1.resta()
t1.multiplicacion()
t1.division()
t2 = Calculadora()
t2.suma()
t2.resta()
t2.multiplicacion()
t2.division()