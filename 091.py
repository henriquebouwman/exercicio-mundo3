from random import randint
from time import sleep
from operator import itemgetter
dados = {}
ranking = []
print('Valores sorteados:')
for i in range(0, 4):
    n = randint(1, 6)
    dados[f'[Jogador {i+1}]'] = n
for k, v in dados.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print('-=' * 30 )
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'    {i+1} lugar: {v[0]} com {v[1]}')
    sleep(1)
print('FIM')
