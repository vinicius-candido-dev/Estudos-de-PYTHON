from rich import print
from rich import emoji

class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentação(self):
        return f"[bold red]:red_heart-text:[/]Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do {self.setor} da empresa Curso em Vídeo "


c1 = Funcionario('Maria','Adiministração', 'Diretora')
print(c1.apresentação())

c2 = Funcionario('Pedro','TI', 'Progrmador')
print(c2.apresentação())
