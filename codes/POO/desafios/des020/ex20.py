from rich import print
from rich.panel import Panel
class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome 
        self.nick = nick
        self.all = list()
        
    def add_favorite(self, add):
        #self.all += f'\n:video_game: [blue]{add}[/blue]'
        self.all.append(add)
        self.all = sorted(self.all, key=str.lower)


    def ficha(self):
        conteudo = f'Nome real: [reverse blue] {self.nome}[/]'
        conteudo += f'\nJogos favoritos:'
        for num, game in enumerate(self.all):
            conteudo += f'\n:video_game: [blue]{game}[/]'
        jog = Panel(conteudo, title=f"jogador <{self.nick}>",width=50)
        return jog


g1 = Gamer("Vinicius Cândido","vini")
g1.add_favorite('Silksong')
g1.add_favorite('God of War')
g1.add_favorite('Chess')
g1.add_favorite('Dark souls')
print(g1.ficha())
