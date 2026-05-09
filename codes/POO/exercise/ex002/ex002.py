#Declaração d classe
class Vini:
    """
Essa classe um gafonhoto, que tem nome e idade

para criar uma nova pessoa, use:
    variavel = Vini(nome, idade)
    """
    def __init__(self, n = '', i = 0): #Método-construtor
        #atributo de instancia
        self.nome = n
        self.idade = i


        #Metodo de instancia
    def aniversario(self):
        self.idade = self.idade + 1


    def msg(self):
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de idade."


# Declaração de objeto
g1 = Vini('Maria',20)
print(g1.msg())

g2 = Vini("Mateus", 30)
print(g2.msg())

g3 = Vini()
print(g3.msg())

print(Vini.__doc__)


print(g1.__doc__)# Dunder Attribute
print(g1.__dict__) # attribute
print(g1.__getstate__()) # Method
print(g1.__class__)