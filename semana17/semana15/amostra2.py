import csv
from os import write

def abre_log(file='access.log'):
    for linha in open(file):
        yield linha, linha.upper()
        
def abre_csv(file='candidatura.csv'):
    with open(file) as csv_file:
        yield linha

def consulta_csv(ano, file='candidatura.csv'):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')        
        for linha in csv_reader:            
            if ano in linha[0] or 'ano_eleicao' in linha:           
                yield linha        

def gera_csv():
    lista_anos = ['1996','1998','2000','2002','2004','2006','2008','2010','2012','2014','2016','2018']
    for ano in lista_anos:
        g = consulta_csv(ano)
        with open(f'eleicao_{ano}.csv','w') as csv_file:
            fwiter = csv.writer(csv_file, delimiter=',')
            for v in g:
                fwiter.writerow(v)
                
