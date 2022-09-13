def sacar(self, valor: float):
    if self.saldo >= valor:
        self.saldo -= valor