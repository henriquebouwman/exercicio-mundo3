lista = []
op = ''
n = []
while True:
    n = (int(input('Digite um valor: ')))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    op = str(input('Quer continuar? [S/N]'))
    while True:
        if op.strip().upper() not in 'SN' or op.strip().upper() == '':
            print('Comando inválido! Tente novamente...')
            op = str(input('Quer continuar? [S/N]'))
        else:
            break
    if op.strip().upper() == 'N':
        break
    if op.strip().upper() == 'S':
        continue
print('-=' * 30)
lista.sort()
print(f'Você digitou os valores: {lista}')