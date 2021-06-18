from integrador.classes.Contexto import Contexto
from integrador.classes.Estrategias import Estrategia
import pytest


class TestContexto:
    def test_instanciar_objeto_ok(self):
        dicionario = {'algoritmo': 'csv',
                      'arquivo': 'file.csv',
                      'pass': '123mudar'}
        objeto = Contexto(**dicionario)
        assert isinstance(objeto, Contexto)
        objeto2 = Contexto(algoritmo='csv', arquivo="file.csv")
        assert isinstance(objeto2, Contexto)

    def test_instanciar_objeto_fail(self):
        msg_erro = "Credendiais inválidas. "
        msg_erro = msg_erro + "Necessário: ('algoritmo', 'arquivo')"
        with pytest.raises(Exception) as error:
            dicionario = {'algoritmo': 'csv', 'pass': '123mudar'}
            Contexto(**dicionario)
        assert str(error.value) == msg_erro

    def test_algoritmo_nao_implementado(self):
        msg_erro = 'Algoritmo não implementado'
        with pytest.raises(Exception) as error:
            dicionario = {'algoritmo': 'algoritmo_nao_implementado'}
            Contexto(**dicionario)
        assert str(error.value) == msg_erro

    def test_str_repr(self):
        dicionario = {'algoritmo': 'csv',
                      'arquivo': 'file.csv',
                      'pass': '123mudar'}
        objeto = Contexto(**dicionario)
        assert str(objeto) == 'Algoritmo CSV'
        assert repr(objeto) == 'Algoritmo CSV'

    def test_setters(self):
        dicionario = {'algoritmo': 'csv',
                      'arquivo': 'file.csv',
                      'pass': '123mudar'}
        objeto = Contexto(**dicionario)
        assert objeto.algoritmo == 'Algoritmo CSV'
        isinstance(objeto.algoritmo, Estrategia)
        objeto.algoritmo = 'Sqlite'
        isinstance(objeto.algoritmo, Estrategia)
        assert objeto.dados == dicionario
        objeto.dados = {}
        assert objeto.dados == {}

    def test_setters_fail(self):
        msg_erro = 'Algoritmo não implementado'
        dicionario = {'algoritmo': 'csv',
                      'arquivo': 'file.csv'}
        with pytest.raises(Exception) as error:
            objeto = Contexto(**dicionario)
            objeto.algoritmo = 'algoritmo_nao_implementado'
        assert str(error.value) == msg_erro

    def test_metodo_dados_armazenados(self):
        dicionario = {'algoritmo': 'csv',
                      'arquivo': 'file.csv',
                      'pass': '123mudar'}
        objeto = Contexto(**dicionario)
        assert type(objeto.dados_armazenados()) == list
        assert objeto.dados_armazenados() == ['algoritmo', 'arquivo', 'pass']

    def test_metodo_algoritmos_implementados(self):
        dicionario = {'algoritmo': 'csv',
                      'arquivo': 'file.csv',
                      'pass': '123mudar'}
        objeto = Contexto(**dicionario)
        assert type(objeto.algoritmos_implementados()) == list

    def test_metodo_executar_csv(self):
        dados = {'algoritmo': 'CSV',
                 'arquivo': 'integrador/dados/arquivo1.csv'}
        objeto = Contexto(**dados)
        assert type(objeto.executar()) == list

    def test_metodo_executar_sqlite(self):
        dados = {'algoritmo': 'SQLite',
                 'db': 'integrador/dados/banco1.db'}
        objeto = Contexto(**dados)
        assert type(objeto.executar()) == list
