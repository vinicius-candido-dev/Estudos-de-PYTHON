#Declaração d classe
'''class Vini:
    def __init__(self): #Método-construtor
        #atributo de instancia
        self.nome = ''
        self.idade = 0


        #Metodo de instancia
    def aniversario(self):
        self.idade = self.idade + 1


    def msg(self):
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de idade."


# Declaração de objeto
g1 = Vini()
g1.nome = 'Maria'
g1.idade = 20
print(g1.msg())

g2 = Vini()
g2.nome = "Maria"
g2.idade = 30
print(g2.msg())'''

#My test
class Vc:
    def __init__(self):
        self.pessoa1 = 0.00
        self.pessoa2 = 0.00

    def altura(self):
        try:
            if self.pessoa1 > self.pessoa2:
                return 'O mais alto é a primeira pessoa'
            elif self.pessoa2 > self.pessoa1:
                return 'O mais alto é a segunda pessoa'
            else:
                return 'Ambos tem a mesma altura'
        except(TypeError):
            return 'Erro de tipo'

result = Vc()
result.pessoa1 = 2.00
result.pessoa2 = 2.00
print(result.altura())
