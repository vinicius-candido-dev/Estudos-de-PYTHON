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
            panel = Panel(f'Analisando [bold green]{self.titulo}[/] com [blue]{self.quant} convidados[/]'
                          '\nCada participante comerá 0.4Kg e cada Kg custa R$82.40' 
                          f'\nRecomendo [bold blue]compra {comprar}00Kg[/] de carne'
                          f'\nO custo total será de [bold green]R${custo:.2f}[/]'
                          f'\nCada pessoa pegará [bold yellow]R${pag_perso}[/] para participar.'
                          ,title='vini')
            return panel
        except Exception as e:
            return f'Existe um erro {e}. Por favor, resolva!'



c1 = Churasco('Churras dos amigos',15)
print(c1.analisar())