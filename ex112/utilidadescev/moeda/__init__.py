def metade(price, f=False):
    resp = price / 2
    if f:
        return moeda(resp)
    else:
        return resp


def dobro(price, f=False):
    resp = price * 2
    if f:
        return moeda(resp)
    else:
        return resp


def aporcent(price, taxa=100, f=False):
    '''
    -> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param price: o preço que se quer reajustar.
    :param taxa: qual é a porcentagem do aumento.
    :param f: quer a saída formatada ou não?
    :return: o valor reajustado com ou sem formatação.
    '''
    resp = price + (price * taxa / 100)
    if f:
        return moeda(resp)
    else:
        return resp


def rporcent(price, taxa=100, f=False):
    resp = price - (price * taxa / 100)
    if f:
        return moeda(resp)
    else:
        return resp


def moeda(price=0, coin='R$'):
    resp = f"{coin}{price:>.2f}".replace('.', ',')
    return resp


def resumo(price=0, taxaa=100, taxar=100):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(price)}')
    print(f'Dobro do preço: \t{dobro(price, True)}')
    print(f'Metade do preço: \t{metade(price, True)}')
    print(f'{taxaa}% de aumento: \t{aporcent(price, taxaa, True)}')
    print(f'{taxar}% de redução: \t{rporcent(price, taxar, True)}')
    print('-' * 30)