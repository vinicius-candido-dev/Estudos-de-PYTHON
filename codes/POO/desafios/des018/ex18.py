from rich import print
from rich.panel import Panel
class Churasco():
    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant

    def analisar(self):
        try:
        #cosumo padrão: 400 por pessoa
        #R$82,40/kg
            comprar = self.quant * 0.4
            custo = 82.40 * comprar
            pag_perso = custo / self.quant
            write = f'Analisando [bold green]{self.titulo}[/] com [blue]{self.quant} convidados[/]\n'
            write += 'Cada participante comerá 0.4Kg e cada Kg custa R$82.40\n'
            write += f'Recomendo [bold blue]compra {comprar:,.2f}0Kg[/] de carnez\n'
            write += f'O custo total será de [bold green]R${custo:.2f}[/]\n'
            write += f'Cada pessoa pegará [bold yellow]R${pag_perso:.2f}[/] para participar.'
            panel = Panel(write, title='Churras dos amigos')
            return panel
        except Exception as e:
            return f'Existe um erro {e}. Por favor, resolva!'


c1 = Churasco('Churras dos amigos',100)
print(c1.analisar())