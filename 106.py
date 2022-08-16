from time import sleep

c = ('\033[m',           # 0 - sem cores
     '\033[0;30;41m',    # 1 - vermelho
     '\033[0;30;42m',    # 2 - verde
     '\033[0;30;43m',    # 3 - amarelo
     '\033[0;30;47m',    # 4 - cinza
     '\033[0;30;45m',    # 5 - roxo
     '\033[7;40m'        # 6 - branco
     )


def ajuda(com):
    escreva(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def escreva(txt, cor=0):
    tam = len(txt) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


comando = ''
while True:
    escreva('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca: ')).strip().lower()
    if comando == 'fim':
        break
    else:
        ajuda(comando)
escreva('ATÉ LOGO!', 1)
