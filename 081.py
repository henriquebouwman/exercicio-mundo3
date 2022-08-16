lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    op = str(input('Quer continuar? [S/N]').upper().strip())
    while True:
        if op not in 'SN' or op == '':
            print('Comando inválido! Tente novamente...')
            op = str(input('Quer continuar? [S/N]').upper().strip())
        else:
            break
    if op == 'N':
        break
    if op == 'S':
        continue
print('=-' * 30)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')