lista = []
for c in range(0, 5):
    n = int(input(f'Digite o valor {c+1}: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        maior = menor = n
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista.')
                break
print(f'Os valores digitados em ordem foram: {lista} ')
