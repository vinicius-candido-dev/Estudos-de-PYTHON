from rich import print
from rich.panel import Panel
class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome 
        self.nick = nick 
        
    def add_favorite(self, add):
        lista = []
        lista.append(add)
        





    def ficha(self):
        jog = Panel(f'Nome real: [reverse blue] {self.nome} [/]' '\nJogos favoritos:',
                    title=f"jogador <{self.nick}>",width=50, height=10)

        return jog



g1 = Gamer("Vinicius Cândido","vini")
print(g1.ficha())
