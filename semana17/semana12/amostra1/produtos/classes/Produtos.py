from abc import ABC, abstractmethod
# from .Caracteristicas import Caracteristicas


class Produto(ABC):
    def __init__(self, implementation):
        self.implementation = implementation
        if not isinstance(self.implementation, Caracteristicas):
            raise ('Implementation not subclass of Caracteristicas')

    @abstractmethod
    def operation(self):
        pass


class CocaCola(Produto):
    def operation(self):
        return (f"CocaCola tamanho:"
                f"{self.implementation.operation_implementation()}")


class Pepsi(Produto):
    def operation(self):
        return (f"Pepsi tamanho:"
                f"{self.implementation.operation_implementation()}")


class Dolly(Produto):
    def operation(self):
        return (f"Dolly tamanho:"
                f"{self.implementation.operation_implementation()}")


class GuaranaAntartica(Produto):
    def operation(self):
        return (f"GuaranaAntartica tamanho:"
                f"{self.implementation.operation_implementation()}")
