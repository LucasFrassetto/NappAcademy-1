from integrador.classes.Estrategias import Estrategia
from integrador.classes.Estrategias import Estrategia_SQLite
from integrador.classes.Estrategias import Estrategia_CSV
import pytest


class TestEstrategias:
    def test_instanciar_classe_abstrata(self):
        msg_erro = "Can't instantiate abstract class Estrategia with abstract"
        msg_erro = msg_erro + " methods execute, nome, parametros_necessarios"
        with pytest.raises(Exception) as error:
            Estrategia()
        assert str(error.value) == msg_erro


class TestEstrategia_SQLite:
    def test_instanciar_classe(self):
        objeto = Estrategia_SQLite()
        assert isinstance(objeto, Estrategia)
        assert isinstance(objeto, Estrategia_SQLite)

    def test_metodo_parametros_necessarios(self):
        objeto = Estrategia_SQLite()
        dados_retornados = objeto.parametros_necessarios()
        assert type(dados_retornados) is tuple
        assert dados_retornados == ('algoritmo', 'db')

    def test_metodo_executar(self):
        dados = {'algoritmo': 'SQLite', 'db': 'integrador/dados/banco1.db'}
        objeto = Estrategia_SQLite()
        dados_retornados = objeto.execute(dados)
        assert type(dados_retornados) is list


class TestEstrategia_CSV:
    def test_instanciar_classe(self):
        objeto = Estrategia_CSV()
        assert isinstance(objeto, Estrategia)
        assert isinstance(objeto, Estrategia_CSV)

    def test_metodo_parametros_necessarios(self):
        objeto = Estrategia_CSV()
        dados_retornados = objeto.parametros_necessarios()
        assert type(dados_retornados) is tuple
        assert dados_retornados == ('algoritmo', 'arquivo')

    def test_metodo_executar(self):
        dados = {'algoritmo': 'CSV',
                 'arquivo': 'integrador/dados/arquivo1.csv'}
        objeto = Estrategia_CSV()
        dados_retornados = objeto.execute(dados)
        assert type(dados_retornados) is list
