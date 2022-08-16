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
