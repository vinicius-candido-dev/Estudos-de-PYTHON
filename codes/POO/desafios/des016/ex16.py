from rich import print
from rich import inspect 
    
class Funcionario:
    # atributi de classe -> serve para todas as classes
    empresa = 'Curso em Vídeo'

    def __init__(self, nome, setor, cargo):
        # atributo de instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentação(self):
        return f"[bold red]:handshake:[/] Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do {self.setor} da empresa {Funcionario.empresa}  "

# Funcionario.empresa = 'Hostnet'
c1 = Funcionario('Maria','Adiministração', 'Diretora')
print(c1.apresentação())

c2 = Funcionario('Pedro','TI', 'Progrmador')
print(c2.apresentação())

#inspect(c1, methods=True) #-> ver os atributos e informação. tem como colocar "dunder = True"
