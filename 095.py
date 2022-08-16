jogador = {}
time = []
gols = []
while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).strip()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for i in range(partidas):
        gols.append(int(input(f'    Quantos gols na partida {i+1}? ')))
        jogador['gols'] = gols[:]
        jogador['total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if op in 'SN':
            break
        print('Erro! Tente novamente...')
    if op == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    op2 = int(input('Mostrar dados de qual jogador? (999 para encerrar o programa) '))
    if op2 == 999:
        break
    elif op2 >= len(time):
        print(f'Erro! Não existe jogador com código {op2}!')
    else:
        print(f'  -- LEVANTAMENTO DO JOGADOR {time[op2]["nome"]}:')
        for i, g in enumerate(time[op2]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print()
print('<< VOLTE SEMPRE >>')
