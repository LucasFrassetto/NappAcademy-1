from ecommerce.classes.Ecommerce import Loja
from ecommerce.classes.Cliente import Cliente
from ecommerce.classes.Pedido import Pedido


class TestEcommerce:
    def test_class_declared(self):
        objeto = Loja('Lojão Tabajara')
        assert isinstance(objeto, Loja)

    def test_instanciar(self):
        objeto = Loja('Lojão Tabajara')
        assert objeto.nome, 'Lojão Tabajara'

    def test_setters(self):
        objeto = Loja('Lojão Tabajara')
        assert objeto.nome == 'Lojão Tabajara'
        objeto.nome = 'Lojão Tabajara Centro'
        assert objeto.nome == 'Lojão Tabajara Centro'
        assert objeto.estoque == {}

    def test_str_repr(self):
        objeto = Loja('Lojão Tabajara')
        assert str(objeto) == 'Lojão Tabajara'
        assert repr(objeto) == 'Nome da Loja => Lojão Tabajara'

    def test_metodo_add_estoque_ok(self):
        loja = Loja('Lojão Tabajara')
        loja.add_estoque('12345678911', 15, 1)
        assert len(loja.estoque) == 1

    def test_metodo_add_estoque_ok2(self):
        loja = Loja('Lojão Tabajara')
        loja.add_estoque('12345678911', 15, 3)
        loja.add_estoque('123', 12, 5)
        assert len(loja.estoque) == 2

    def test_quantidade_produtos(self):
        loja = Loja('Lojão Tabajara')
        loja.add_estoque('123', 15, 10)
        loja.add_estoque('1234', 20, 5)
        loja.add_estoque('12345', 20, -1)
        loja.add_estoque('123456', 20, 0)
        assert loja.quantidade_produtos('123') == 10
        assert loja.quantidade_produtos('1234') == 5
        assert loja.quantidade_produtos('12345') == 0
        assert loja.quantidade_produtos('123456') == 0

    def test_metodo_comprar_ok(self):
        loja = Loja('Lojão Tabajara')
        loja.add_estoque('123', 15, 3)
        assert loja.estoque['123'].quantidade == 3
        loja.comprar('123')
        assert loja.estoque['123'].quantidade == 2

    def test_metodo_comprar_sem_produto(self):
        loja = Loja('Lojão Tabajara')
        assert loja.comprar('9999999') is None

    def test_metodo_comprar_ok2(self):
        loja = Loja('Lojão Tabajara')
        loja.add_estoque('123', 15, 1)
        assert loja.estoque['123'].quantidade == 1
        loja.comprar('123')
        assert loja.estoque['123'].quantidade == 0
        assert loja.comprar('123') is None

    def test_devolver_carrinho(self):
        loja = Loja('Lojão Tabajara')
        loja.add_estoque('123', 15, 10)
        loja.add_estoque('1234', 20, 5)
        assert len(loja.estoque) == 2
        cliente = Cliente('John Doe')
        pedido = Pedido(cliente)
        pedido.add_item(loja.comprar('1234'))
        pedido.add_item(loja.comprar('123'))
        assert len(pedido.itens) == 2
        assert len(loja.estoque) == 2
        assert loja.quantidade_produtos('1234') == 4
        assert loja.quantidade_produtos('123') == 9
        loja.devolver_carrinho(pedido)
        assert len(pedido.itens) == 0
        assert len(loja.estoque) == 2
