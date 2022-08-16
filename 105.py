def notas(* num, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação do aluno.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    d = {}
    contador = maior = menor = soma = 0
    for n in num:
        soma += n
        if contador == 0:
            maior = menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
        contador += 1
    d['total'] = contador
    d['maior'] = maior
    d['menor'] = menor
    d['media'] = soma/contador
    if sit:
        if d['media'] >= 9:
            d['situação'] = 'ÓTIMA'
        elif d['media'] >= 7:
            d['situação'] = 'BOA'
        elif d['media'] >= 5:
            d['situação'] = 'REGULAR'
        else:
            d['situação'] = 'RUIM'
    return d


resp = notas(10, 5, 6, sit=True)
print(resp)
