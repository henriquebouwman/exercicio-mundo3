def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return num


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    op = leiaInt('\033[32mSua opção: \033[m')
    return op
