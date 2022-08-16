#Brasileirão 2022 no dia 09/08

lista_times = ('Palmeiras', 'Corinthians', 'Fluminense', 'Athletico-PR', 'Flamengo',
               'Internacional', 'Atlético-MG', 'Bragantino', 'Santos', 'América-MG',
               'São Paulo', 'Botafogo', 'Goiás', 'Ceará SC', 'Coritiba',
               'Avaí', 'Fortaleza', 'Cuiabá', 'Atlético-GO', 'Juventude')
print('-='*20)
print(f'Lista de times do Brasileirão: {lista_times}')
print('-='*20)
print(f'Os 5 primeiros são: {lista_times[0:5]}')
print('-='*20)
print(f'Os 4 últimos são: {lista_times[-4:]}')
print('-='*20)
print(f'Times em ordem alfabética: {sorted(lista_times)}')
print('-='*20)

while True:
    time = str(input('Qual time você deseja ver a posição? '))
    if time in lista_times:
        break
    print('Time inválido. Tente novamente!')
print(f'O {time} está na {lista_times.index(str(time))+1}ª posição.')
while True:
    op = str(input('Quer ver a posição de outro time? [S/N]').upper())
    if op == 'S':
        time = str(input('Qual time você deseja ver a posição? '))
        if time not in lista_times:
            print('Time inválido. Tente novamente!')
            time = str(input('Qual time você deseja ver a posição? '))
        print(f'O {time} está na {lista_times.index(str(time))+1}ª posição.')
    elif op == 'N':
        break
    else:
        print('Opção inválida! Tente novamente utilizando [S/N].')
print('Obrigado, volte sempre!')


