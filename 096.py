def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno ({larg}x{comp}) é igual a {a}m².')


print(f'{"Controle de terrenos":^40}')
print('-' * 40)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
print('-' * 40)
area(l, c)
