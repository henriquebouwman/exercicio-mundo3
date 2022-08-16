def maior(* num):
    print('Analisando os valores passados...')
    contador = maior = 0
    for n in num:
        print(n, end=' ')
        if contador == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        contador += 1
    print(f'\nForam informados {contador} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
    print('-=' * 30)


maior(5, 2)
maior(1, 5, 9, 0, 22)
maior(3, 5, 8, 0, 1, 6, 1, 2, 8)
maior(1, 52, 41, 22, 45, 82, 84, 12, 95, 33, 22, 75)
