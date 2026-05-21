class Empty:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'


pessoa = Empty('vini','maia',6000)
print(pessoa.email)
print(pessoa.pay)
print(pessoa.fullname())