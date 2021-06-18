
from integrador.classes.Estrategias import Estrategia_CSV
from integrador.classes.Estrategias import Estrategia_SQLite
from integrador.classes.Estrategias import Estrategia_Texto1
from integrador.classes.Estrategias import Estrategia_Texto2

estrategias = {
    'csv': Estrategia_CSV(),
    'sqlite': Estrategia_SQLite(),
    'texto_1': Estrategia_Texto1(),
    'texto_2': Estrategia_Texto2(),
}


class Contexto():
    """
    Contexto do integrador
    Objeto responsável por armazenar o algoritmo (estratégia)
    e os dados de acesso (credenciais)
    """
    def __init__(self, **kwargs):
        try:
            algoritmo_escolhido = kwargs['algoritmo'].lower()
            objeto = estrategias[algoritmo_escolhido]
        except KeyError:
            raise Exception('Algoritmo não implementado')
        self._algoritmo = objeto
        self._dados = kwargs
        if not self._dados_credenciais_validos():
            esperado = str(self._algoritmo.parametros_necessarios())
            raise Exception('Credendiais inválidas. Necessário: ' + esperado)

    @property
    def algoritmo(self):
        return self._algoritmo.nome()

    @algoritmo.setter
    def algoritmo(self, algoritmo):
        try:
            objeto = estrategias[algoritmo.lower()]
        except KeyError:
            raise Exception('Algoritmo não implementado')
        self._algoritmo = objeto

    @property
    def dados(self):
        return self._dados

    @dados.setter
    def dados(self, dados):
        self._dados = dados

    def _dados_credenciais_validos(self):
        """
        Método interno, verifica se as credendiais informadas são suficientes
        para extrair os dados.
        Retorna
            True, caso credenciais sejam suficientes.
            False, caso não sejam credenciais suficientes.
        """
        key_params = set(self._algoritmo.parametros_necessarios())
        parametros = set(self._dados.keys())
        return key_params.issubset(parametros)

    def dados_armazenados(self):
        return list(self.dados.keys())

    def algoritmos_implementados(self):
        return list(estrategias.keys())

    def executar(self):
        return self._algoritmo.execute(self.dados)

    def __str__(self):
        return self._algoritmo.nome()

    def __repr__(self):
        return self._algoritmo.nome()
