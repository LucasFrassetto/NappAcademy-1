import csv
from abc import ABC, abstractmethod


class Relatorios(ABC):
    @abstractmethod
    def criar_relatorio(self, lista):
        pass


class Relatorio_TXT(Relatorios):
    def criar_relatorio(self, lista, nome_arquivo):
        nome_arquivo = nome_arquivo + '.txt'
        with open(nome_arquivo, "w") as f:
            f.write('Relatório de Vendas\n')
            f.write(40 * '*' + '\n')
            f.write("DATA\t\t\t\t VALOR\n")
            for i in lista:
                f.write(str(i[0]) + 8 * " ")
                f.write(str(i[1]) + 7 * " ")
                f.write('\n')
            return True

class Relatorio_CSV(Relatorios):
    def criar_relatorio(self, lista, nome_arquivo):
        nome_arquivo = nome_arquivo + '.csv'
        with open(nome_arquivo, "w", newline='') as csvfile:
            fieldnames = ['vendido_em', 'valor']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for i in lista:
                writer.writerow({'vendido_em': str(i[0]), 'valor': str(i[1])})
            return True

    #fieldnames = ['first_name', 'last_name']
    #writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    #writer.writeheader()
    #writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    #writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    #writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
