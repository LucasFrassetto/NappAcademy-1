from integrador.classes.Extrair import ERP1, ERP2
from integrador.classes.Relatorios import Relatorio_TXT, Relatorio_CSV

extratores = {
    'erp1': ERP1(),
    'erp2': ERP2(),
}

relatorios = {
    'txt': Relatorio_TXT(),
    'csv': Relatorio_CSV(),
}


class Abstracao:
    def __init__(self, **kwargs):
        self._dados = kwargs
        try:
            erp_cliente = kwargs['erp'].lower()
            self.implementacao = extratores[erp_cliente]
        except KeyError:
            raise Exception('ERP não implementado')
        try:
            formato_relatorio = kwargs['relatorio'].lower()
            self.relatorio = relatorios[formato_relatorio]
        except KeyError:
            raise Exception('Formato de relatório não implementado')

    def extrair_dados(self):
        query_sql = self.implementacao.get_query()
        return self.implementacao.execute(self._dados, query_sql)

    def relatorio_simples(self):
        query_sql = self.implementacao.get_query_report()
        return self.implementacao.execute(self._dados, query_sql)

    def criar_relatorio(self):
        arquivo_saida = self._dados.get('relatorio_nome', 'output')
        return self.relatorio.criar_relatorio(self.relatorio_simples(),
                                              arquivo_saida)
