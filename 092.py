from datetime import datetime
dados = {}
dados['Nome'] = str(input('Nome: '))
dados['Ano'] = int(input('Ano de nascimento: '))
dados['Idade'] = datetime.today().year - dados['Ano']
dados['CTPS'] = int(input('Carteira de Trabalho (0 se não possuir): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = (dados['Contratação'] - dados['Ano']) + 35
del dados['Ano']
print('-=' * 40)
for k, v in dados.items():
    if k == 'Contratação':
        print(f'O ano de {k} foi em {v}')
    elif k == 'Aposentadoria':
        print(f'A {k} será com {v} anos.')
    elif k == 'Idade':
        print(f'A {k} do usuário é {v} anos.')
    else:
        print(f'{k} do usuário é {v}')
