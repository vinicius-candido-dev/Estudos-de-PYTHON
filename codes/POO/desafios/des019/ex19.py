from rich import print
from rich import emoji
class Livro():
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas

        

    def avamcar_paginas(self, count):
        pag = 1
        if pag == 1:
            return f'[bold blue]Você acabou de abrir o livro "[/][bold red]{self.titulo}[/][bold blue]" que tem[/] [bold green]{self.paginas} paginas[/] [bold blue]no total. Você agora está na [/][bold yellow] página {self.paginas} [/]'
        else:
            pass


d1 = Livro('Em busca da verdade',20)
print(d1)
#print(d1.avamcar_paginas(5))