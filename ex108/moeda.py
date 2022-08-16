def metade(price):
    resp = price / 2
    return resp


def dobro(price):
    resp = price * 2
    return resp


def aporcent(price, taxa):
    resp = price + (price * taxa / 100)
    return resp


def rporcent(price, taxa):
    resp = price - (price * taxa / 100)
    return resp


def moeda(price=0, moeda= 'R$'):
    resp = f"{moeda}{price:>.2f}".replace('.', ',')
    return resp
