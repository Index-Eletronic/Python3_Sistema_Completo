def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') # rt = read text... vai tentar abrir o arquivo como texto.
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