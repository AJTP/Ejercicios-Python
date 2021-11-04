# En un banco tienen clientes que pueden hacer depósitos y extracciones de dinero. El
# banco requiere también al final del día calcular la cantidad de dinero que se ha depositado.
# Se deberán crear dos clases, la clase cliente y la clase banco. La clase cliente tendrá los
# atributos nombre y cantidad y los métodos __init__, depositar, extraer, mostrar_total.
# La clase banco tendrá como atributos 3 objetos de la clase cliente y los métodos
# __init__, operar y deposito_total.

class Cliente:
    nombre = ""
    cantidad = 0

    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

    def depositar(self, n):
        self.cantidad = self.cantidad + n

    def extraer(self, n):
        self.cantidad = self.cantidad - n

    def mostrar_total(self):
        print("Total: ", self.cantidad)


class Banco:
    clientes = []

    def __init__(self):
        self.clientes.append(Cliente("Antonio", 100))
        self.clientes.append(Cliente("Ramón", 200))
        self.clientes.append(Cliente("Fran", 300))

    def operar(self, cliente1, cliente2, c):
        transaccion = False
        for i in self.clientes:
            if i.nombre == cliente2:
                i.extraer(c)
                for j in self.clientes:
                    if j.nombre == cliente1:
                        j.depositar(c)
                        print("Cliente ", i.nombre, " Saldo:", i.cantidad)
                        print("Cliente ", j.nombre, " Saldo:", j.cantidad)
                        transaccion = True
                        break
                break
        if transaccion==False:
            print("No se pudo completar la operación")

    def deposito_total(self):
        total = 0
        for i in self.clientes:
            total = total + i.cantidad
        print("Deposito total: ", total)


banco = Banco()
while True:
    print("1. Operar")
    print("2. Deposito total")
    x = int(input("¿Que deseas hacer?: "))

    if x == 1:
        banco.operar(input("Introduce el nombre del receptor: "),input("Introduce el nombre del emisor: "),int(input("Introduce la cantidad: ")))
    elif x == 2:
        banco.deposito_total()
    else:
        break
