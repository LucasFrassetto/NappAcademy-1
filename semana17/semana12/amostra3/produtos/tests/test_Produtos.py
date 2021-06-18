from produtos.classes.Produtos import Produto
from produtos.classes.Produtos import CocaCola
from produtos.classes.Produtos import Pepsi
from produtos.classes.Produtos import Dolly
from produtos.classes.Produtos import GuaranaAntartica
from produtos.classes.Caracteristicas import Tamanho600ml
import pytest


class TestColaborador:
    def test_class_Pepsi(self):
        msg = 'Pepsi tamanho: 600ml.'
        objeto = Pepsi(Tamanho600ml())
        assert isinstance(objeto, Produto)
        assert isinstance(objeto, Pepsi)
        assert objeto.operation() == msg

    def test_class_CocaCola(self):
        msg = 'CocaCola tamanho: 600ml.'
        objeto = CocaCola(Tamanho600ml())
        assert isinstance(objeto, Produto)
        assert isinstance(objeto, CocaCola)
        assert objeto.operation() == msg

    def test_class_Dolly(self):
        msg = 'Dolly tamanho: 600ml.'
        objeto = Dolly(Tamanho600ml())
        assert isinstance(objeto, Produto)
        assert isinstance(objeto, Dolly)
        assert objeto.operation() == msg

    def test_class_GuaranaAntartica(self):
        msg = 'GuaranaAntartica tamanho: 600ml.'
        objeto = GuaranaAntartica(Tamanho600ml())
        assert isinstance(objeto, Produto)
        assert isinstance(objeto, GuaranaAntartica)
        assert objeto.operation() == msg

    def test_class_abstractClass(self):
        msg_erro = "Can't instantiate abstract class Produto "
        msg_erro = msg_erro + "with abstract methods operation"
        with pytest.raises(TypeError) as error:
            Produto()
        assert str(error.value) == msg_erro

    def test_class_CaracteristaClass(self):
        msg_erro = \
            "Produto recebe somente uma variavél do tipo Caracteristicas"
        with pytest.raises(TypeError) as error:
            Pepsi("2 Litros.")
        assert str(error.value) == msg_erro
