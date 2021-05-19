from lib.interface import *
from lib.arquivo import *
from time import sleep

#============= VERIFICANDO SE O ARQUIVO EXISTE===================================
arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
#================================================================================

while True:
    resposta = menu(['Ver pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema']) # Lista
    if resposta == 1:
        #Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)

    elif resposta == 2:
        # Opção para cadastrar um conteudo no arquivo.
        cabeçalho('NOVO CADASTRO')
        nome =str(input('Nome: '))
        idade = leiaInt('Idade: ') # Vai ler a idade como numero inteiro.
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do Sistema ... Até Logo!')
        break
    else:
        print('\33[31mErro! Digite uma das opções válidas\33[m')
    sleep(2)