def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        num = str(input(msg)).strip()
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print(f'\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return f'\033[32m{valor}\033[m'


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}!')