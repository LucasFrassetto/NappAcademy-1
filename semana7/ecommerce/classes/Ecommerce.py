from ecommerce.classes.Produto import Produto
from ecommerce.classes.Pedido import Pedido


class Loja:
    def __init__(self, nome):
        self._nome = nome
        self._estoque = {}

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def estoque(self):
        return self._estoque

    def __str__(self):
        return self.nome

    def __repr__(self):
        return 'Nome da Loja => ' + self.nome

    def _produto_exist(self, ean):
        if ean in self.estoque:
                return True
        return False

    def add_estoque(self, ean, preco, quantidade):
        if not self._produto_exist(ean):
            if quantidade < 0:
                quantidade = 0
            self._estoque.update({ean: Produto(ean=ean, preco=preco, quantidade=quantidade)})

    def quantidade_produtos(self, ean):
        quantidade = 0
        if ean in self.estoque:
                quantidade = self.estoque[ean].quantidade
        return quantidade

    def comprar(self, ean):
        if ean in self.estoque:
            if self.estoque[ean].quantidade == 0:
                return None
            self.estoque[ean].quantidade -= 1
            return self.estoque[ean]
        return None

    def devolver_carrinho(self, pedido):
        if isinstance(pedido, Pedido):
            for item in pedido.itens:
                if isinstance(item, Produto):
                    self.estoque[item.ean].quantidade += 1
            pedido.itens = []
            return pedido
