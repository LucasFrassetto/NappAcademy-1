from abc import ABC, abstractmethod
from contextlib import closing
import sqlite3
import csv
import re

class Estrategia(ABC):
    """
    Classe Base para as estratégias (algoritmos)

    """
    @abstractmethod
    def execute(self, dados):
        """ Método em que o algoritmo é contido.
        Implementação do algoritmo na classe filha deve
        sobreescrever este método."""
        pass

    @abstractmethod
    def parametros_necessarios(self):
        """Sobreescrever este método para que retorne uma tupla
        com a lista de parâmetros necessários.
        Exemplo:
        ('algoritmo', 'dbname', 'host', 'user', 'password')
        """
        pass

    @abstractmethod
    def nome(self):
        """Sobreescrever este método para que
        retorne o nome do algoritmo utilizado."""
        pass


class Estrategia_SQLite(Estrategia):
    def execute(self, dados):
        lista_registros = []
        teste = []
        db = dados['db']
        with closing(sqlite3.connect(db)) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM vendas;")
            for linha in cursor.fetchall():
                lista_registros.append(linha)
        #Modificação Desafio 6
        for item in lista_registros:
            teste.append((item[-2],item[-1]))   
        return teste
        #Finaliza Modificação 6

    def parametros_necessarios(self):
        return ('algoritmo', 'db')

    def nome(self):
        return 'Algoritmo SQLite'

class Estrategia_CSV(Estrategia):
    def execute(self, dados):
        teste=[]
        arquivo = dados['arquivo']
        with open(arquivo, newline='\n') as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
                lista_registros = []
                lista_registros2 = []
                lista_registros.append(line['total'])
                lista_registros2.append(line['vendido_em'])
                teste.append(dict(zip(lista_registros2, lista_registros)))
        return teste

    def parametros_necessarios(self):
        return ('algoritmo', 'arquivo')

    def nome(self):
        return 'Algoritmo CSV'


class Estrategia_Texto1(Estrategia):
    def execute(self, dados):
        lista_registros = []
        arquivo = dados['arquivo']
        with open(arquivo) as txtfile:
            lines = txtfile.readlines()
            for line in lines:
                if lines.index(line) > 2:
                    txt_final = line.replace('        ',';').replace('       ',';')
                    lista_valores = txt_final.split(';')
                    data = lista_valores[0]
                    valor = lista_valores[3]
                    produto = lista_valores[-1].replace('\n', '')
                    dados = (produto, valor, data)
                    lista_registros.append(dados)

        return lista_registros
                   
    
    def parametros_necessarios(self):
        return ('algoritmo', 'arquivo')

    def nome(self):
        return 'Algoritmo TXT'


class Estrategia_Texto2(Estrategia):
    def execute(self, dados):
        lista_registros = []
        arquivo = dados['arquivo']
        with open(arquivo) as txtfile:
            lines = txtfile.readlines()
            for line in lines:
                if lines.index(line) > 2:
                    txt_final = line.replace('        ',';').replace('       ',';')
                    lista_valores = txt_final.split(';')
                    data = lista_valores[0]
                    valor = lista_valores[2].replace('\n', '')
                    produto = lista_valores[1]
                    dados = (produto, valor, data)
                    lista_registros.append(dados)

        return lista_registros
    
    def parametros_necessarios(self):
        return ('algoritmo', 'arquivo')

    def nome(self):
        return 'Algoritmo TXT'