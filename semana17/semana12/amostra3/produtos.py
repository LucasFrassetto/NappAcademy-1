from produtos.classes.Produtos import Pepsi
from produtos.classes.Produtos import Dolly
from produtos.classes.Produtos import CocaCola
from produtos.classes.Produtos import GuaranaAntartica
from produtos.classes.Caracteristicas import Tamanho600ml
from produtos.classes.Caracteristicas import Tamanho1litro
from produtos.classes.Caracteristicas import Tamanho2litro
from produtos.classes.Caracteristicas import Tamanho3litro


def client_code(produto):
    print(produto.operation())


if __name__ == "__main__":
    tamanho = Tamanho600ml()
    produto = CocaCola(tamanho)
    client_code(produto)

    tamanho = Tamanho1litro()
    produto = CocaCola(tamanho)
    client_code(produto)

    tamanho = Tamanho600ml()
    produto = Pepsi(tamanho)
    client_code(produto)

    tamanho = Tamanho1litro()
    produto = Pepsi(tamanho)
    client_code(produto)

    tamanho = Tamanho2litro()
    produto = Dolly(tamanho)
    client_code(produto)

    tamanho = Tamanho3litro()
    produto = GuaranaAntartica(tamanho)
    client_code(produto)
