from abc import ABC, abstractmethod


class Caracteristicas(ABC):
    @abstractmethod
    def operation_implementation(self):
        pass


class Tamanho600ml(Caracteristicas):
    def operation_implementation(self):
        return " 600ml."


class Tamanho1litro(Caracteristicas):
    def operation_implementation(self):
        return " 1 litro."


class Tamanho2litros(Caracteristicas):
    def operation_implementation(self):
        return " 2 litros."


class Tamanho3litros(Caracteristicas):
    def operation_implementation(self):
        return " 3 litros."
