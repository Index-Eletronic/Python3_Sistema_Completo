from lib.interface import *
from time import sleep

while True:
    resposta = menu(['Ver pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabeçalho('Opção 1')
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('Saindo do Sistema ... Até Logo!')
        break
    else:
        print('\33[31mErro! Digite uma das opções válidas\33[m')
    sleep(2)