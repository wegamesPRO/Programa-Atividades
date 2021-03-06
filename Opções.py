from funções import *
from Calculos_Geometria import *


class Opção1:
    def __init__(self):
        num_func = 1
        while True:
            # Tela inicial
            print(f'\033[1;32m{"Matematica":^60}\033[m ')

            # Opção
            print('''\n(1) para geometria\n(0) para VOLTAR ''')
            opção = valida_int(input('Opção : '))

            if opção < 0 or opção > num_func:
                print('\n\033[1;31mOPÇÃO INVALIDA !\033[m')

            if opção == 0:
                break

            if opção == 1:
                print(f'\033[1;36m{"Geometria":^60}\033[m')
                vertices = valida_int(input('vertices : '))
                faces = valida_int(input('faces : '))
                arestas = valida_int(input('arestas : '))

                poliedro_euler = R_euler(vertices, faces, arestas)
                poliedro_regular = P_regular(vertices, faces, arestas)

                if vertices == 0:
                    vertices = poliedro_euler.know_vertices()
                    print(vertices)
                if faces == 0:
                    faces = poliedro_euler.know_faces()
                    print(faces)
                if arestas == 0:
                    arestas = poliedro_euler.know_arestas()
                    print(arestas)

                print('-' * 40)
                if poliedro_euler.validar():
                    print('é um poliedro')
                else:
                    print('não é um poliedro')
                if poliedro_regular.validar():
                    print('é regular')
                    print(f'é um {poliedro_regular.tipo()}')
                else:
                    print('não é regular')
                print('-'*60)
