from rich import print
from rich.panel import Panel
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        return Panel(f'{self.nome:^32}\n {"-----------------------------":^30}\n {f".........R${self.preco}.00.........."} ', title="Produto",style="red", width=35, height=5)


p1 = Produto("kinder ovo","R$500")
print(p1.etiqueta())
p2 = Produto("iPhone 19 pro max", '20000')
print(p2.etiqueta())