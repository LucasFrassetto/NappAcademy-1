from produtos.classes.Produtos import CocaCola, Pepsi, Dolly, GuaranaAntartica
from produtos.classes.Caracteristicas import Tamanho600ml, Tamanho1litro, Tamanho2litro, Tamanho3litro


def client_code(produto):
    print(produto.operation())


if __name__ == "__main__":
    # ------ CocaCola ------ #
    tamanho = Tamanho600ml()
    produto = CocaCola(tamanho)
    client_code(produto)

    tamanho = Tamanho1litro()
    produto = CocaCola(tamanho)
    client_code(produto)

    tamanho = Tamanho2litro()
    produto = CocaCola(tamanho)
    client_code(produto)

    tamanho = Tamanho3litro()
    produto = CocaCola(tamanho)
    client_code(produto)

    # ------ Pepsi ------ #
    tamanho = Tamanho600ml()
    produto = Pepsi(tamanho)
    client_code(produto)

    tamanho = Tamanho1litro()
    produto = Pepsi(tamanho)
    client_code(produto)

    tamanho = Tamanho2litro()
    produto = Pepsi(tamanho)
    client_code(produto)

    tamanho = Tamanho3litro()
    produto = Pepsi(tamanho)
    client_code(produto)

    # ------ Dolly ------ #
    tamanho = Tamanho600ml()
    produto = Dolly(tamanho)
    client_code(produto)

    tamanho = Tamanho1litro()
    produto = Dolly(tamanho)
    client_code(produto)

    tamanho = Tamanho2litro()
    produto = Dolly(tamanho)
    client_code(produto)

    tamanho = Tamanho3litro()
    produto = Dolly(tamanho)
    client_code(produto)

    # ------ GuaranaAntartica ------ #
    tamanho = Tamanho600ml()
    produto = GuaranaAntartica(tamanho)
    client_code(produto)

    tamanho = Tamanho1litro()
    produto = GuaranaAntartica(tamanho)
    client_code(produto)

    tamanho = Tamanho2litro()
    produto = GuaranaAntartica(tamanho)
    client_code(produto)

    tamanho = Tamanho3litro()
    produto = GuaranaAntartica(tamanho)
    client_code(produto)