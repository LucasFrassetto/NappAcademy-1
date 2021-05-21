def abre_log(file='access.log'):
    for linha in open(file):
        yield linha, linha.upper()
        
def abre_csv(file='caso_full.csv'):
    for linha in open(file):
        yield linha

def busca_leme(file='caso_full.csv'):
    for linha in open(file):
        if 'Leme' in linha:
            yield linha

file = open('caso_full.csv')

arquivo_carregado_em_memoria = open('caso_full.csv').read()