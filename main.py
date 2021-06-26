from Opções import *

num_func = 1
while True:
    # opção
    print('''(1) Resoluções de matematica\n(0) Para SAIR ''')
    opção = valida_int(input('Opção : '))

    if opção < 0 or opção > num_func:
        print('\n\033[1;31mOPÇÃO INVALIDA !\033[m')

    elif opção == 0:
        break

    elif opção == 1:
        Opção1()

    print('-'*30)
print('\n\033[1;32mObrigado VOLTE SEMPRE !\033[m')