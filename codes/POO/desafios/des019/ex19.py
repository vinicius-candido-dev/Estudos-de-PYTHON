from rich import print
from rich import emoji
from time import sleep
class Livro():
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pag_atual = 1
        
        print(f':open_book: [blue]Você acabou de abrir o livro [red]"{self.titulo}"[/] que tem [green] {self.paginas} página[/] no total. Você agora está na [yellow]página {self.pag_atual}[/][/blue]')

    def avancar_paginas(self, qtd = 1):
        cont = 0
        for a in range(self.pag_atual,qtd, 1):
                if not self.fim_livro():
                    self.pag_atual +=1
                    print( f'Pág{self.pag_atual} :arrow_forward:', end=' ')
                    sleep(0.4)
                    cont +=1
        print(f"[blue]Você avançou {cont} páginas e agora está na [yellow]página {self.pag_atual}[/][/blue]')")
        if self.fim_livro():
            print(f':closed_book: [red]Você chegou ao final do filme "{self.titulo}"[/]')
    def fim_livro(self) -> bool:
        return True if self.pag_atual == self.paginas else False

        '''if self.paginas == self.pag_atual:
            return True
        else:
            return False'''



d1 = Livro('Em busca da verdade', 20)
d1.avancar_paginas(5)
d1.avancar_paginas(10)
d1.avancar_paginas(50)

#print(d1.avancar_paginas(5))
