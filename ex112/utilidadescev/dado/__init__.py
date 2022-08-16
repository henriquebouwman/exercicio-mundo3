def leiaDinheiro(msg):
    valido = False
    while not valido:
        num = str(input(f'{msg}')).replace(',', '.').strip()
        if num.isalpha() or num == '':
            print(f'\033[0;31mERRO: "{num}" é um preço inválido!\033[m')
        else:
            valido = True
            return float(num)
