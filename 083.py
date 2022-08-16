# expr = str(input('Digite a expressão: '))
# a = expr.count('(')
# b = expr.count(')')
# if (a + b) % 2 == 0:
#     print('Sua expressão está válida!')
# else:
#     print('Sua expressão está errada!')
expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')

if len(pilha) == 0:
     print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')