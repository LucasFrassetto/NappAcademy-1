from produtos.classes.Produtos import Pepsi
from produtos.classes.Produtos import CocaCola
from produtos.classes.Produtos import Dolly
from produtos.classes.Produtos import GuaranaAntartica
from produtos.classes.Caracteristicas import Caracteristicas
from produtos.classes.Caracteristicas import Tamanho600ml
from produtos.classes.Caracteristicas import Tamanho1litro
from produtos.classes.Caracteristicas import Tamanho2litros
from produtos.classes.Caracteristicas import Tamanho3litros
import pytest


class TestCaracteristicas:
    def test_Pepsi_600ml(self):
        msg = 'Pepsi tamanho: 600ml.'
        caracteristica = Tamanho600ml()
        objeto = Pepsi(caracteristica)
        assert isinstance(caracteristica, Caracteristicas)
        assert isinstance(caracteristica, Tamanho600ml)
        assert objeto.operation() == msg

    def test_Pepsi_1_litro(self):
        msg = 'Pepsi tamanho: 1 litro.'
        caracteristica = Tamanho1litro()
        objeto = Pepsi(caracteristica)
        assert isinstance(caracteristica, Caracteristicas)
        assert isinstance(caracteristica, Tamanho1litro)
        assert objeto.operation() == msg

    def test_Pepsi_2_litros(self):
        msg = 'Pepsi tamanho: 2 litros.'
        caracteristica = Tamanho2litros()
        objeto = Pepsi(caracteristica)
        assert isinstance(caracteristica, Caracteristicas)
        assert isinstance(caracteristica, Tamanho2litros)
        assert objeto.operation() == msg

    def test_Pepsi_3_litros(self):
        msg = 'Pepsi tamanho: 3 litros.'
        caracteristica = Tamanho3litros()
        objeto = Pepsi(caracteristica)
        assert isinstance(caracteristica, Caracteristicas)
        assert isinstance(caracteristica, Tamanho3litros)
        assert objeto.operation() == msg

    def test_CocaCola_600ml(self):
        msg = 'CocaCola tamanho: 600ml.'
        caracteristicas = Tamanho600ml()
        objeto = CocaCola(caracteristicas)
        assert isinstance(caracteristicas, Caracteristicas)
        assert isinstance(caracteristicas, Tamanho600ml)
        assert objeto.operation() == msg

    def test_CocaCola_1_litro(self):
        msg = 'CocaCola tamanho: 1 litro.'
        caracteristicas = Tamanho1litro()
        objeto = CocaCola(caracteristicas)
        assert isinstance(caracteristicas, Caracteristicas)
        assert isinstance(caracteristicas, Tamanho1litro)
        assert objeto.operation() == msg

    def test_CocaCola_2_litros(self):
        msg = 'CocaCola tamanho: 2 litros.'
        caracteristicas = Tamanho2litros()
        objeto = CocaCola(caracteristicas)
        assert isinstance(caracteristicas, Caracteristicas)
        assert isinstance(caracteristicas, Tamanho2litros)
        assert objeto.operation() == msg

    def test_CocaCola_3_litros(self):
        msg = 'CocaCola tamanho: 3 litros.'
        caracteristicas = Tamanho3litros()
        objeto = CocaCola(caracteristicas)
        assert isinstance(caracteristicas, Caracteristicas)
        assert isinstance(caracteristicas, Tamanho3litros)
        assert objeto.operation() == msg

    def test_Dolly_600ml(self):
        msg = 'Dolly tamanho: 600ml.'
        caracteristicas = Tamanho600ml()
        objeto = Dolly(caracteristicas)
        assert isinstance(caracteristicas, Caracteristicas)
        assert isinstance(caracteristicas, Tamanho600ml)
        assert objeto.operation() == msg

    def test_Dolly_1_litro(self):
        msg = 'Dolly tamanho: 1 litro.'
        caracteristicas = Tamanho1litro()
        objeto = Dolly(caracteristicas)
        assert isinstance(caracteristicas, Caracteristicas)
        assert isinstance(caracteristicas, Tamanho1litro)
        assert objeto.operation() == msg

    def test_Dolly_2_litros(self):
        msg = 'Dolly tamanho: 2 litros.'
        caracteristicas = Tamanho2litros()
        objeto = Dolly(caracteristicas)
        assert isinstance(caracteristicas, Caracteristicas)
        assert isinstance(caracteristicas, Tamanho2litros)
        assert objeto.operation() == msg

    def test_Dolly_3_litros(self):
        msg = 'Dolly tamanho: 3 litros.'
        caracteristicas = Tamanho3litros()
        objeto = Dolly(caracteristicas)
        assert isinstance(caracteristicas, Caracteristicas)
        assert isinstance(caracteristicas, Tamanho3litros)
        assert objeto.operation() == msg

    def test_GuaranaAntartica_600ml(self):
        msg = 'Guarana Antartica tamanho: 600ml.'
        caracteristicas = Tamanho600ml()
        objeto = GuaranaAntartica(caracteristicas)
        assert isinstance(caracteristicas, Caracteristicas)
        assert isinstance(caracteristicas, Tamanho600ml)
        assert objeto.operation() == msg

    def test_GuaranaAntartica_1_litro(self):
        msg = 'Guarana Antartica tamanho: 1 litro.'
        caracteristicas = Tamanho1litro()
        objeto = GuaranaAntartica(caracteristicas)
        assert isinstance(caracteristicas, Caracteristicas)
        assert isinstance(caracteristicas, Tamanho1litro)
        assert objeto.operation() == msg

    def test_GuaranaAntartica_2_litros(self):
        msg = 'Guarana Antartica tamanho: 2 litros.'
        caracteristicas = Tamanho2litros()
        objeto = GuaranaAntartica(caracteristicas)
        assert isinstance(caracteristicas, Caracteristicas)
        assert isinstance(caracteristicas, Tamanho2litros)
        assert objeto.operation() == msg

    def test_GuaranaAntartica_3_litros(self):
        msg = 'Guarana Antartica tamanho: 3 litros.'
        caracteristicas = Tamanho3litros()
        objeto = GuaranaAntartica(caracteristicas)
        assert isinstance(caracteristicas, Caracteristicas)
        assert isinstance(caracteristicas, Tamanho3litros)
        assert objeto.operation() == msg

    def test_class_abstractClass(self):
        msg_erro = "Can't instantiate abstract class Caracteristicas "
        msg_erro = msg_erro + "with abstract methods operation_implementation"
        with pytest.raises(TypeError) as error:
            Caracteristicas()
        assert str(error.value) == msg_erro
