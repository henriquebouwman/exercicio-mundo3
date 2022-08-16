lista_de_palavras = 'APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO',\
        'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', \
        'PROGRAMADOR', 'FUTURO'
for palavra in lista_de_palavras:
    print(f'\nNa palavra {palavra} temos: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')