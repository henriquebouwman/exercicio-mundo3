"""def leiaInt(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            break
        print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')

    return int(num)


def leiaFloat(msg):
    while True:
        num = input(msg)
        if num.replace('.', '').isnumeric():
            break
        print('\033[31mERRO: por favor, digite um número real válido.\033[m')
    return float(num)"""


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


def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO: por favor, digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return num


i = leiaInt('Digite um Inteiro: ')
r = leiaFloat('Digite um real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {r}')
