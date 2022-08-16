# num = [int(input('Digite um valor para posição 0: ')), int(input('Digite um valor para posição 1: ')), int(input('Digite um valor para posição 2: ')),
#        int(input('Digite um valor para posição 3: ')), int(input('Digite um valor para posição 4: '))]
# count = 0
# maior = 0
# menor = 0
# for n in num:
#     count +=1
#     if count == 1:
#         menor = n
#         maior = n
#     if n > maior:
#         maior = n
#     if n < menor:
#         menor = n
#
# print(f'O maior valor digitado foi {maior} nas posições', end='')
# for m in maior:
#     print(f'{num.index(maior)+1}.')
# print(f'O menor valor digitado foi {menor}.')
listanum = []
maior = 0
menor = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum[c]
        if listanum[c] < menor:
            menor = listanum[c]


print('=-' * 30)
print(f'Você digitou os valores {listanum}.')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}... ', end='')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}... ', end='')