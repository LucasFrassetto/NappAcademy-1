from rh.classes.Departamento import Departamento
from datetime import date, timedelta


class TestDepartamento:
    def test_class_declared(self):
        objeto = Departamento('Departamento XYZ')
        assert isinstance(objeto, Departamento)

    def test_instanciar(self):
        objeto = Departamento('Departamento XYZ')
        assert objeto.nome == 'Departamento XYZ'
        assert objeto.responsavel is None

    def test_str_repr(self):
        objeto = Departamento('Departamento XYZ')
        assert str(objeto) == 'Departamento XYZ'
        assert repr(objeto) == 'Departamento = Departamento XYZ'

    def test_setters(self):
        objeto = Departamento('Curadoria')
        assert objeto.nome == 'Curadoria'
        objeto.nome = 'ETL'
        assert objeto.nome == 'ETL'

    def test_properties(self):
        objeto = Departamento('Departamento XYZ')
        assert objeto.nome == 'Departamento XYZ'

    def test_responsavel(self):
        departamento = Departamento('Departamento XYZ')
        assert departamento.responsavel == None
        responsavel = {'nome': 'José da Silva', 'dia': 1, 'mes': 1, 'ano': 1990}
        departamento = Departamento('Departamento XYZ', responsavel)

    def test_responsavel_substituido(self):
        departamento = Departamento('Departamento XYZ')
        assert departamento.responsavel is None
        departamento.informar_responsavel('José da Silva', 1, 1, 1990)
        assert departamento.responsavel == 'José da Silva'
        departamento.informar_responsavel('João Oliveira', 1, 1, 1990)
        assert departamento.responsavel == 'João Oliveira'

    def test_add_colaborador(self):
        departamento = Departamento('Departamento XYZ')
        departamento.informar_responsavel('José da Silva', 1, 1, 1990)
        departamento.add_colaborador('João Oliveira', 18, 3, 1992)
        departamento.add_colaborador('Pedro Mendonça', 18, 4, 1993)
        assert len(departamento.colaboradores) == 2

    def test_verificar_aniversariantes(self):
        retorno = [('João Oliveira', '1992-04-10', 'Departamento XYZ'),
                   ('Luis Fernando', '2000-04-10', 'Departamento XYZ')]
        dt1 = date.today() - timedelta(days=11)
        hoje = date.today()
        depto = Departamento('Departamento XYZ')
        depto.informar_responsavel('José da Silva', dt1.day, dt1.month, 1990)
        depto.add_colaborador('João Oliveira', hoje.day, hoje.month, 1992)
        depto.add_colaborador('Pedro Mendonça', dt1.day, dt1.month, 1993)
        depto.add_colaborador('Luis Fernando', hoje.day, hoje.month, 2000)
        depto.add_colaborador('Maurício Souza', dt1.day, dt1.month, 1085)
        aniversariantes = depto.verificar_aniversariantes()
        assert aniversariantes == retorno
        assert len(aniversariantes) == 2
        assert len(aniversariantes[0]) == 3
        assert type(aniversariantes[0]) == tuple
        assert type(aniversariantes) == list
