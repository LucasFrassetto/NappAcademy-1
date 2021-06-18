from integrador.classes.Abstracao import Abstracao
import pytest
import unittest


class TestAbstracaoERP1(unittest.TestCase):
    def setUp(self):
        self.dicionario = {'erp': 'erp1',
                           'db': 'integrador/dados/banco_ERP1.db',
                           'relatorio': 'txt'}

    def test_instanciar_objeto_ok(self):
        objeto = Abstracao(**self.dicionario)
        assert isinstance(objeto, Abstracao)
        objeto2 = Abstracao(erp='erp1', relatorio="txt")
        assert isinstance(objeto2, Abstracao)

    def test_metodo_extrair_dados(self):
        objeto = Abstracao(**self.dicionario)
        assert isinstance(objeto.extrair_dados(), list)

    def test_metodo_relatorio_simples(self):
        objeto = Abstracao(**self.dicionario)
        assert isinstance(objeto.relatorio_simples(), list)

    def test_metodo_criar_relatorio(self):
        objeto = Abstracao(**self.dicionario)
        assert objeto.criar_relatorio()


class TestAbstracaoERP1_csv(unittest.TestCase):
    def setUp(self):
        self.dicionario = {'erp': 'erp1',
                           'db': 'integrador/dados/banco_ERP1.db',
                           'relatorio': 'csv'}

    def test_instanciar_objeto_ok(self):
        objeto = Abstracao(**self.dicionario)
        assert isinstance(objeto, Abstracao)
        objeto2 = Abstracao(erp='erp1', relatorio="csv")
        assert isinstance(objeto2, Abstracao)

    def test_metodo_extrair_dados(self):
        objeto = Abstracao(**self.dicionario)
        assert isinstance(objeto.extrair_dados(), list)

    def test_metodo_relatorio_simples(self):
        objeto = Abstracao(**self.dicionario)
        assert isinstance(objeto.relatorio_simples(), list)

    def test_metodo_criar_relatorio(self):
        objeto = Abstracao(**self.dicionario)
        assert objeto.criar_relatorio()


class TestAbstracaoERP2(unittest.TestCase):
    def setUp(self):
        self.dicionario = {'erp': 'erp2',
                           'db': 'integrador/dados/banco_ERP2.db',
                           'relatorio': 'txt'}

    def test_instanciar_objeto_ok(self):
        objeto = Abstracao(**self.dicionario)
        assert isinstance(objeto, Abstracao)
        objeto2 = Abstracao(erp='erp1', relatorio="txt")
        assert isinstance(objeto2, Abstracao)

    def test_metodo_extrair_dados(self):
        objeto = Abstracao(**self.dicionario)
        assert isinstance(objeto.extrair_dados(), list)

    def test_metodo_relatorio_simples(self):
        objeto = Abstracao(**self.dicionario)
        assert isinstance(objeto.relatorio_simples(), list)

    def test_metodo_criar_relatorio(self):
        objeto = Abstracao(**self.dicionario)
        assert objeto.criar_relatorio()


class TestAbstracaoERP2_csv(unittest.TestCase):
    def setUp(self):
        self.dicionario = {'erp': 'erp2',
                           'db': 'integrador/dados/banco_ERP2.db',
                           'relatorio': 'csv'}

    def test_instanciar_objeto_ok(self):
        objeto = Abstracao(**self.dicionario)
        assert isinstance(objeto, Abstracao)
        objeto2 = Abstracao(erp='erp2', relatorio="csv")
        assert isinstance(objeto2, Abstracao)

    def test_metodo_extrair_dados(self):
        objeto = Abstracao(**self.dicionario)
        assert isinstance(objeto.extrair_dados(), list)

    def test_metodo_relatorio_simples(self):
        objeto = Abstracao(**self.dicionario)
        assert isinstance(objeto.relatorio_simples(), list)

    def test_metodo_criar_relatorio(self):
        objeto = Abstracao(**self.dicionario)
        assert objeto.criar_relatorio()
