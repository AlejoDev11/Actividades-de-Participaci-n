class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_de_cuenta = numero_cuenta(12345)
        self.propietarios = propietarios(["Juan", "Maria"])
        self.balance = balance(0)  

    def depositar(self, monto):
        self.balance += monto

    def retirar(self, monto):
        if monto <= self.balance:
            self.balance -= monto
        else: 
            print("No hay suficiente dinero en la cuenta.")

    def aplicar_cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota 

    def mostrar_detalles(self):
        print("Numero de cuenta", self.numero_de_cuenta)
        print("Propietarios:", self.propietarios)
        print("Balance:", self.balance)