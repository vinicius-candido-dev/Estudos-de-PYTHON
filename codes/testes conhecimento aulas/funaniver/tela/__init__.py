#tipo tilulo
def lines(line = 30):
    print("-" * line)

def cabeçalho(text, line):
    lines(line)
    print(f'{text:^{line}}')
    lines(line)


def menu(text, line):
    lines(line)
    print(f"{text:^{line}}")
    lines(line)
    print("Digite o número que você quer sobre aniversário:")
    print('''  1 - Adicionar um novo aniversário
  2 - Ver todos os aniversários 
  3 - Ver se caso existe um aniversário hoje
  4 - Especificar a data para ver se existe aniversário
  5 - parar o programa''')


