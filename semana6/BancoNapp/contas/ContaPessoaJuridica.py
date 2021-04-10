from BancoNapp.contas.Conta import Conta


class ContaPessoaJuridica(Conta):
    def __init__(self,  **kwargs):
        self.empresa = kwargs.get('empresa', '')
        self.limite = kwargs.get('limite', 1500)
        kwargs.update({'limite': self.limite})

        super(ContaPessoaJuridica, self).__init__(**kwargs)