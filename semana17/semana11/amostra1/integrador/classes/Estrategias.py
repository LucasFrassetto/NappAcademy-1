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
                lista_registros.append(linha)
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
                total = line['total']
                vendido_em = line['vendido_em']
                lista_registros.append({total, vendido_em})
                # lista_registros.append(line)
        return lista_registros

    def parametros_necessarios(self):
        return ('algoritmo', 'arquivo')

    def nome(self):
        return 'Algoritmo CSV'


#Modificar classe estratégia texto1 e texto2
class Estrategia_Texto_1(Estrategia):
    def execute(self, dados):
        lista_registros = []
        arquivo = dados['arquivo']
        f = open(arquivo, 'r', encoding='UTF-8')

        #Pula Cabeçalho
        for i in range(3):
            f.readline()

        # if(arquivo[-11:-4] == 'modelo1'):
        
        for line in f:
            data = line[:10]
            #quantidade = line[11:26].strip()
            #valor = line[27:37].strip()
            total = line[36:48].strip()
            produto = line[-13::].strip()
            lista_registros.append((produto, total, data))
            # for line in f:
            #     data = line[:10]
            #     produto = line[11:31].strip()
            #     total = line[-10::].strip()
            #     lista_registros.append((produto, total, data))

        return lista_registros

    def parametros_necessarios(self):
        return ('algoritmo', 'arquivo')

    def nome(self):
        return 'Algoritmo Texto_1'


class Estrategia_Texto_2(Estrategia):
    def execute(self, dados):
        lista_registros = []
        arquivo = dados['arquivo']
        f = open(arquivo, 'r', encoding='UTF-8')

        #Pula Cabeçalho
        for i in range(3):
            f.readline()
            
        for line in f:
            data = line[:10]
            produto = line[11:31].strip()
            total = line[-10::].strip()
            lista_registros.append((produto, total, data))

        return lista_registros

    def parametros_necessarios(self):
        return ('algoritmo', 'arquivo')

    def nome(self):
        return 'Algoritmo Texto_2'