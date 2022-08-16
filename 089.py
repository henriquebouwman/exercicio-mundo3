from time import sleep
ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    op = str(input('Quer continuar? [S/N]')).strip().upper()
    while True:
        if op not in 'SN' or op == '':
            print('Comando inválido! Tente novamente...')
            op = str(input('Quer continuar? [S/N]')).strip().upper()
        else:
            break
    if op == 'N':
        break
print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    op = int(input('Mostrar notas de qual aluno? (999 para interromper): '))
    if op == 999:
        print('Finalizando...')
        break
    if op <= len(ficha) - 1:
        print(f'Notas de {ficha[op][0]} são {ficha[op][1]}')
sleep(1)
print('VOLTE SEMPRE!')
