from abc import ABC, abstractmethod
from contextlib import closing
import sqlite3
import csv


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
        db = dados['db']
        with closing(sqlite3.connect(db)) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM vendas;")
            for linha in cursor.fetchall():
                lista_registros.append((linha[4], linha[5]))
        return lista_registros

    def parametros_necessarios(self):
        return ('algoritmo', 'db')

    def nome(self):
        return 'Algoritmo SQLite'


class Estrategia_CSV(Estrategia):
    def execute(self, dados):
        lista_registros = []
        arquivo = dados['arquivo']
        with open(arquivo, newline='\n') as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
                lista_registros.append((line['total'], line['vendido_em']))
        return lista_registros

    def parametros_necessarios(self):
        return ('algoritmo', 'arquivo')

    def nome(self):
        return 'Algoritmo CSV'


class Estrategia_Texto_1(Estrategia):
    def execute(self, dados):
        lista_registros = []
        arquivo = dados['arquivo']
        headers = []
        with open(arquivo, 'r') as in_file:
            stripped = (line.strip() for line in in_file)
            for line in stripped:
                if 'Arquivo TXT com os dados' in line or '***' in line:
                    continue
                if 'data' in line.lower():
                    headers = [ln.lower() for ln in line.strip().replace(' ', '').split('\t') if ln]
                    continue
                columns = [ln for ln in line.strip().split('  ') if ln]
                line_dict = dict(zip(headers, columns))
                lista_registros.append((line_dict['produto'], line_dict['total'], line_dict['data']))

        return lista_registros

    def parametros_necessarios(self):
        return ('algoritmo', 'arquivo')

    def nome(self):
        return 'Algoritmo Texto 1'


class Estrategia_Texto_2(Estrategia):
    def execute(self, dados):
        lista_registros = []
        arquivo = dados['arquivo']
        headers = []
        with open(arquivo, 'r') as in_file:
            stripped = (line.strip() for line in in_file)
            for line in stripped:
                if 'Arquivo TXT com os dados' in line or '***' in line:
                    continue
                if 'data' in line.lower():
                    headers = [ln.lower() for ln in line.strip().replace(' ', '').split('\t') if ln]
                    continue
                columns = [ln for ln in line.strip().split('  ') if ln]
                line_dict = dict(zip(headers, columns))
                lista_registros.append((line_dict['produto'], line_dict['total'], line_dict['data']))

        return lista_registros

    def parametros_necessarios(self):
        return ('algoritmo', 'arquivo')

    def nome(self):
        return 'Algoritmo Texto 2'