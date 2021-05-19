from lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') # rt = read text... vai tentar abrir o arquivo e ler como texto.
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')# wt = write text e o + ele criar o arquivo. Gravação de Arquivo.
        a.close()
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome} Criado com sucesso.')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a: # Para cada linha em arquivo
            dado = linha.split(';') # dado vai ser uma lista e split vai separar por ;
            dado[1] = dado[1].replace('\n', '') # Vai retirar o espaço entre as palavras  do \n
            print(f'{dado[0]:<30}{dado[1]:>} anos') # Dado 0 = nome e Dado 1 = Idade

        print(a.read())

    finally:
        a.close()

def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a= open(arq, 'at')# a = apppend (colocar coisas dentro do arquivo
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados.')
        else:
            print(f'Nome registro de {nome} adicionado')
            a.close()

