import csv


def abre_csv(file='candidatura.csv'):
    for linha in csv.reader(open(file)):
        yield linha


iter_csv = abre_csv()
header = next(iter_csv)
anos = []
for row in iter_csv:
    anos.append(row[0])

anos = list(set(anos))

arquivos = dict()

for ano in anos:
    arquivos[ano] = csv.writer(open("eleicao_"+ano+".csv", 'w'))
    arquivos[ano].writerow(header)


iter_csv = abre_csv()
header = next(iter_csv)

for row in iter_csv:
    arquivos[row[0]].writerow(row)
