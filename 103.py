def jogador(n="<desconhecido>", g=0):
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


nome = str(input('Nome do Jogador: '))
gols = str(input('Número de Gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    jogador(g=gols)
else:
    jogador(nome, gols)

