# it = 'Lápis', 'Borracha', 'Caderno', 'Estojo', 'Transferidor', \
#      'Compasso', 'Mochila', 'Canetas', 'Livro'
# preco = 1.75, 2.00, 15.90, 25.00, 4.20, 9.99, 120.32, 22.30, 34.90
#
# print('--' * 30)
# print('LISTAGEM DE PREÇOS')
# print('--' * 30)
# cont = 0
# for produto in it:
#      print(produto + '......................R$   ' + str(preco[cont]))
#      cont += 1
# print('--' * 30)
lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.9,
         'Estojo', 25,
         'Transferidor', 4.2,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.3,
         'Livro', 34.9)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for item in range(len(lista)):
     if item % 2 == 0:
          print(f'{lista[item]:.<30}', end='')
     else:
          print(f'R${lista[item]:>7.2f}')
print('-'*40)
