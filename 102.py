def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (Opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    if show:
        if n < 0:
            print('Não existe fatorial de número negativo!')
        elif n == 0:
            return 1
        else:
            f = 1
            while n > 1:
                print(f'{n} x ', end='')
                f *= n
                n -= 1
            print(f'1 = {f}')
            return
    else:
        if n < 0:
            print('Não existe fatorial de número negativo!')
        elif n == 0:
            return 1
        else:
            f = 1
            while n > 1:
                f *= n
                n -= 1
            return print(f)


num = int(input('Digite um número para saber seu fatorial: '))
while True:
    op = str(input('Quer ver o cálculo da operação? [S/N] ')).upper().strip()[0]
    if op in 'SN':
        break
    print('Erro! Tente novamente...')
if op == 'S':
    fatorial(num, True)
if op == 'N':
    fatorial(num)
