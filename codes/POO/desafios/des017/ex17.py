from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} custa R${self.preco:,.2f}"

    def etiqueta(self):
        conteudo = f"{self.nome.center(30, '-')}"
        conteudo += f"{'-' * 30}" 
        precof = f"R${self.preco:,.2f}"
        conteudo += f"{precof.center(30, '-')}"
        etiqueta = Panel(conteudo, width=34,title="Produto ")
        return etiqueta 


p1 = Produto("kinder ovo",500)
print(p1.etiqueta())
p2 = Produto("iPhone 19 pro max", 20000)
print(p2.etiqueta())