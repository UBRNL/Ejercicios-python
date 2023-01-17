class CuentaBancaria:
    
    def _init_(self, num_cuenta, nombre_titular, balance):
        self.num_cuenta = num_cuenta
        self.nombre_titular = nombre_titular
        self.balance = balance

    def generar_balance(self):
        print(self.balance)

    def depositar(self,monto):
        if monto > 0:
            self.balance += monto
            
mi_cuenta = CuentaBancaria("105-356-998-145", "Ubernel", 9000)

mi_cuenta.generar_balance()
mi_cuenta.deposito(425)
mi_cuenta.generar_balance()

## tiene un problema que aun no resuelvo ...
