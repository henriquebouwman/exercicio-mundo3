temp = []
princ = []
pmaior = pmenor =0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        pmaior = pmenor = temp[1]
    else:
        if temp[1] > pmaior:
            pmaior = temp[1]
        if temp[1] < pmenor:
            pmenor = temp[1]
    princ.append(temp[:])
    temp.clear()
    op = str(input('Quer continuar? [S/N]').strip().upper())
    while True:
        if op not in 'SN' or op == '':
            print('Comando inválido! Tente novamente...')
            op = str(input('Quer continuar? [S/N]').strip().upper())
        else:
            break
    if op == 'N':
        break
    if op == 'S':
        continue
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {pmaior}Kg. Peso de: ', end='')
for p in princ:
    if p[1] == pmaior:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {pmenor}Kg. Peso de: ', end='')
for p in princ:
    if p[1] == pmenor:
        print(f'[{p[0]}]', end='')
print()


