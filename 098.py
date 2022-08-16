from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    elif p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}:')

    if i < f:
        c = i
        while c <= f:
            print(f'{c} ', end='')
            sleep(0.5)
            c += p
        print('FIM!')
    else:
        c = i
        while c >= f:
            print(f'{c} ', end='')
            sleep(0.5)
            c -= p
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
while True:
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    passos = int(input('Passo: '))
    contador(inicio, fim, passos)
    print('-=' * 20)
    while True:
        op = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if op in 'SN':
            break
        print('Erro! Tente novamente!')
    print('-=' * 20)
    if op == 'N':
        sleep(0.5)
        print('<< VOLTE SEMPRE >>')
        break

