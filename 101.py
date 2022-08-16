def voto(a):
    from datetime import datetime
    idade = datetime.today().year - a
    if 16 <= idade < 18 or idade > 70:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    elif idade < 16:
        return f'Com {idade} anos: VOTO NEGADO.'
    elif idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


print('-' * 30)
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
