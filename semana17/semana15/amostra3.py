import csv


def busca_ano():
    for linha in open(file):
        if 'ano_eleicao' in linha:
            continue
        if str(ano) in linha[0:10]:
            yield linha


file = 'candidatura.csv'

for i in range(0, 24, 2):
    ano = 1996 + i
    with open(f'eleicao_{ano}.csv', 'w', newline='') as csvfile:
        s_writer = csv.writer(csvfile)
        linhas = busca_ano()
        for linha in linhas:
            s_writer.writerow([linha])
    print(f'eleicao_{ano}.csv Criado com sucesso')
