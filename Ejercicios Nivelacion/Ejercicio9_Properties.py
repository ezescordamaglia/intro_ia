
class Categoria:
    def __init__(self, nombre, contabilidad):
        self._nombre = nombre
        self.contabilidad=contabilidad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def deposito(self, monto, descripcion=""):
        self.contabilidad.append({'monto': monto, 'descripcion': descripcion})

    def extraccion(self, monto, descripcion=""):
        if (self.verificar_fondos(monto)):
            self.contabilidad.append({'monto': (monto*-1), 'descripcion': descripcion})
            return True
        else:
            return False

    def obtener_balance(self):
        balance=0
        for reg in self.contabilidad:
            balance = balance + reg['monto']
        return balance

    def total_egresos(self):
        egresos=0
        for reg in self.contabilidad:
            if (reg['monto'] < 0):
                egresos = egresos + reg['monto']
        return egresos*-1

    def transferencia(self, monto, otraCategoria):
        if (self.verificar_fondos(monto)):
            self.contabilidad.append({'monto': (monto*-1), 'descripcion': "Transf. a Categoria " + otraCategoria.nombre})
            otraCategoria.contabilidad.append({'monto': monto, 'descripcion': "Transf. de Categoria " + self.nombre})
            return True
        else:
            return False

    def verificar_fondos(self, monto):
        if (self.obtener_balance() >= monto):
            return True
        else:
            return False

    def imprimir_resumen(self):
        print("\n\n**********" + self.nombre + "**********")
        for reg in self.contabilidad:
            print(reg['descripcion'] + " $" + str(reg['monto']))
        print("TOTAL: $" + str(self.obtener_balance()))

    @staticmethod
    def crear_tabla_gastos(listaCat):
        print("\n\nTabla de Gastos")
        total = 0
        for cat in listaCat:
            total = total + cat.total_egresos()
        print("Total gastado: $" + str(total))
        for cat in listaCat:
            print(cat.nombre + " % gastado " + str((cat.total_egresos()/total)*100))

contabilidadAlimentos = []
alimentos = Categoria('Alimentos', contabilidadAlimentos)

# Pasando por el setter
alimentos.nombre = "Alimenticios"

# Sin pasar por el setter
alimentos._nombre = "Alimenticios2"

alimentos.deposito(1000, "deposito inicial")
alimentos.extraccion(200, "Extraccion")
alimentos.deposito(300, "Cobro sueldo")
alimentos.extraccion(100, "Extraccion")

contabilidadVestimenta = []
vestimenta = Categoria('Vestimenta', contabilidadVestimenta)

vestimenta.deposito(500, "Devolucion banco")
vestimenta.extraccion(300, "Compra Ropa")

alimentos.transferencia(200, vestimenta)

alimentos.imprimir_resumen()
vestimenta.imprimir_resumen()

listaCat = [alimentos, vestimenta]

Categoria.crear_tabla_gastos(listaCat)