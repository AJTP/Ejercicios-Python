# Desarrollar un programa que conste de una clase padre Cuenta y dos subclases PlazoFijo y CajaAhorro.
# Definir los atributos titular y cantidad y un método para imprimir los datos en la clase Cuenta.
# La clase CajaAhorro tendrá un método para heredar los datos y uno para mostrar la información.
# La clase PlazoFijo tendrá dos atributos propios, plazo e interés. Tendrá un método
# para obtener el importe del interés (cantidad*interés/100) y otro método para mostrar
# la información, datos del titular plazo, interés y total de interés.
# Crear al menos un objeto de cada subclase.

class Cuenta:
    titular = ""
    cantidad = ""

    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    def imprimir(self):
        print("Titular: ", self.titular, "\tCantidad: ", self.cantidad)


class CajaAhorro(Cuenta):

    def heredar(self, cuenta):
        self.titular = cuenta.titular
        self.cantidad = cuenta.cantidad


class PlazoFijo(Cuenta):
    plazo = ""
    interes = ""

    def __init__(self, titular, cantidad, plazo, interes):
        super().__init__(titular,cantidad)
        self.plazo = plazo;
        self.interes = interes;

    def importe(self):
        return (self.cantidad * self.interes / 100)

    def imprimir(self):
        print("Titular: ", self.titular, "\tCantidad: ", self.cantidad, "\tPlazo: ", self.plazo, "\tInterés: ",
              self.interes, "\t Total Interés: ", self.importe())


cuenta = Cuenta("Padre", 20000)

caja = CajaAhorro("Pepito", 1000)
plazo = PlazoFijo("Juanito", 6000, 30, 20)

caja.imprimir()
caja.heredar(cuenta)
caja.imprimir()

plazo.imprimir()
