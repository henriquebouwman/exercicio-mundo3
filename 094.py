galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Sexo inválido! Tente novamente...')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        op = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if op in 'SN':
            break
        print('Opção inválida! Tente novamente...')
    if op == 'N':
        break
print('-=' *30)
print(f'=> Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'=> A média de idade é de {media:5.2f} anos.')
print('=> As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'F':
        print(f'[{p["nome"]}] ', end='')
print('\n=> Lista das pessoas que estão com a idade acima da média: ', end='')
for p in galera:
    if p['idade'] > media:
        print()
        print(f'    Nome = {p["nome"]}', end=' / ')
        print(f'    Sexo = {p["sexo"]}', end=' / ')
        print(f'    Idade = {p["idade"]}')
print()
print('<< ENCERRADO >>')
