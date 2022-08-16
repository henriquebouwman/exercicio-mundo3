from lib.interface import *
from time import sleep
from lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arqExiste(arq):
    criarArq(arq)

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resp == 1:
        # Opção de listar o conteúdo do arquivo
        lerArquivo(arq)
    elif resp == 2:
        # Opção de cadastrar uma nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
