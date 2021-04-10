from rh.classes.Colaborador import Colaborador


class Departamento:
    def __init__(self, nome_setor, responsavel={}):
        self._nome_setor = nome_setor
        self._responsavel = None
        if responsavel:
            self.informar_responsavel(responsavel['nome'], responsavel['dia'], responsavel['mes'], responsavel['ano'])
        self._colaboradores = []

    @property
    def nome(self):
        return self._nome_setor

    @nome.setter
    def nome(self, value):
        self._nome_setor = value

    @property
    def responsavel(self):
        if self._responsavel is None:
            return None
        return str(self._responsavel)

    @property
    def colaboradores(self):
        return self._colaboradores

    def informar_responsavel(self, nome, dia, mes, ano):
        self._responsavel = Colaborador(nome, dia, mes, ano)

    def add_colaborador(self, nome, dia, mes, ano):
        self._colaboradores.append(Colaborador(nome, dia, mes, ano))

    def verificar_aniversariantes(self):
        lista = []
        for colaborador in self.colaboradores:
            if colaborador.aniversario_hoje():
                lista.append((colaborador.nome, colaborador.aniversario, self.nome))

        if self.responsavel:
            if self._responsavel.aniversario_hoje():
                lista.append((self._responsavel.nome, self._responsavel.aniversario, self.nome))
        return lista

    def __str__(self):
        return self._nome_setor

    def __repr__(self):
        return 'Departamento = ' + self._nome_setor
