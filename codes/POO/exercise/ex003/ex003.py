class ContaBancaria:
    """
cria uma conta bancária e permite fazer saques e depósitoa
    """
    def __init__(self, id, name, saldo = 0):
        self.id = id
        self.titular = name
        self.saldo = saldo




c1 = ContaBancaria(122, vini, 3000)