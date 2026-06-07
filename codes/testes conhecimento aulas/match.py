class Point:
    def __init__(self, escolhar):
        self.escolha = escolhar

def number(point ):
    match point:
        case 500:
            return '500 reais'
        case 1000:
            return '1000 reais'
        case point():
            return 'Não disse nada'
        case _:
            raise ValueError('Error de tipo')


print(number(500))
print(number(1000))
