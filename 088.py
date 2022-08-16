# from time import sleep
# from random import randint
# jogo = list()
# quant = int(input('Quer gerar quantos jogos? '))
# for j in range(0, quant):
#     while len(jogo) < 6:
#         n = randint(1, 60)
#         if n not in jogo:
#             jogo.append(n)
#     print(f'Jogo {j+1}: {sorted(jogo)}')
#     sleep(.5)
#     jogo.clear()

from random import randint
from time import sleep
lista = []
jogos = []
print('-' * 30)
print('      JOGA NA MEGA SENA      ')
print('-' * 30)
qtd_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= qtd_jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print()
print('-=' * 3, f' SORTEANDO {qtd_jogos} JOGOS ', '-=' * 3)
print()
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print()
print('-=' * 5, ' BOA SORTE! ', '-=' * 5)



