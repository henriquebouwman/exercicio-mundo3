import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é R${moeda.metade(p)}')
print(f'O dobro de {p} é R${moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.aporcent(p, 10)}')
print(f'Reduzindo 13%, temos R${moeda.rporcent(p, 13)}')
