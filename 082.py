lista = []
par = []
impar = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    if n % 2 != 0:
        impar.append(n)
    op = str(input('Quer continuar? [S/N]').strip().upper())
    while True:
        if op not in 'NS' or op == '':
            print('Comando inválido! Tente novamente...')
            op = str(input('Quer continuar? [S/N]').strip().upper())
        else:
            break
    if op == 'N':
        break
    if op == 'S':
        continue
print('-=' * 30)
print(f'A lista completa é {lista}.')
print(f'A lista de pares é {par}.')
print(f'A lista de ímpares é {impar}.')
