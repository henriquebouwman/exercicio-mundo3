def escreva(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'{txt:^{tam}}')
    print('~' * tam)


escreva('Gustavo Guanabara')
escreva('Henrique')
escreva('Oi')
