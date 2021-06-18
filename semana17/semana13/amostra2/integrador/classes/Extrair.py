from abc import ABC, abstractmethod
from contextlib import closing
import sqlite3


class ExtrairDados(ABC):
    @abstractmethod
    def get_query(self):
        pass

    def execute(self, dados, query_sql):
        lista_registros = []
        db = dados['db']
        with closing(sqlite3.connect(db)) as conn:
            cursor = conn.cursor()
            cursor.execute(query_sql)
            for linha in cursor.fetchall():
                lista_registros.append(linha)
        return lista_registros


class ERP1(ExtrairDados):
    def get_query(self):
        return "SELECT produto, total, vendido_em FROM vendas;"

    def get_query_report(self):
        return "SELECT vendido_em, sum(total) FROM vendas GROUP BY vendido_em;"


class ERP2(ExtrairDados):
    def get_query(self):
        return "SELECT prod, total, vendido_em FROM total_vendas;"

    def get_query_report(self):
        return "SELECT vendido_em, sum(total) FROM total_vendas GROUP BY vendido_em;"
