from rich import print
class Caneta:
    def __init__(self, cor = "azul"):
        match cor.lower().strip():
            case "azul":
                escolha = "[blue]"
            case  "vermelho":
                escolha = "[red]"
            case "verde":
                escolha = "[green]"
            case _:
                escolha = "[white]"
        self.cor =  escolha

    def queb_linh(self, qtd = 1):
        return'\n' * qtd

    def escrever(self, msg):
        return f'{self.cor}{msg}[/]'

    def tampar(self):
        pass

    def destampar(self):
        pass




c1 = Caneta("azul")
c2 = Caneta('vermelha')
c3 = Caneta()
print(c1.escrever('Olá, mundo'))

