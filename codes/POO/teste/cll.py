class Celular:
    def __init__(self,bateria = 100, tela_aces = False) :
        self.bateria = bateria
        self.tela_acesa = tela_aces

    def __str__(self):
        return f'A batéria é igual {self.bateria}%'

    def tela_acesa(self):
        self.bateria -= 5
        return f'A batéria igual {self.bateria}'


h = Celular()
print(h.tela_acesa)
