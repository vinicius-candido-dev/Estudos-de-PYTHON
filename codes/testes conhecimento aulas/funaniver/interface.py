import função
import tela
from time import sleep


while True:
    # se existe
    função.existe("birthdays.txt")
    #tela
    tela.cabeçalho("Aniversário", 70)
    tela.menu("Menu de informações", 70)
    choice = int(input('Qual sua escolha?  '))
    try:

        if choice == 1:
            name = input("Qual o nome da pessoa a ser cadastrada: ").capitalize()
            day = int(input(f"Digite o dia desse aniversário de {name}:  "))
            month = int(input(f"Digite o mes desse aniversário de {name}:  "))

            função.add(day,month,name)
        elif choice == 2:
            função.all()

        elif choice == 3:
            função.aniversario_hoje()

        elif choice == 4:
            day = int(input("Qual o dia que você deseja saber?  "))
            month = int(input("Qual o mês que você deseja saber?  "))
            print(função.especificar(day,month))

        elif choice == 5:
            break
        else:
            print('Por favor, digite numero de 1 a 4')
    except:
        print( f"Erro, pessoa não adicionada")
    finally:
        sleep(3)


