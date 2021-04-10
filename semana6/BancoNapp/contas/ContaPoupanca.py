from BancoNapp.contas.Conta import Conta


class ContaPoupanca(Conta):
    def __init__(self,  **kwargs):
        self.limite = kwargs.get('limite', 0)
        self.profissao = kwargs.get('profissao','')
        kwargs.update({'limite': self.limite})

        super(ContaPoupanca, self).__init__(**kwargs)

    def saque(self, valor):
        """
        Método para realizar saque.
        Este método suporta somente números maiores que zero.

        Args:
            valor (float ou int): Valor positivo do saque

        Raises:
            ValueError: Erro ocorre quando é informado valor negativo.
            TypeError: Quando o tipo passado não for inteiro ou float.

        Returns:
            Float: Valor do saque realizado.
        """
        if isinstance(valor, (float, int)):
            if valor > (self.saldo + self.limite):
                raise ValueError('Valor do saque supera seu saldo.')
                return
            self.saldo = self.saldo - valor
            self.extrato.append(('S', valor))
            return valor
        raise TypeError('O valor do saque precisa ser numérico')


    def rendimento_aniversario(self, juros):
        if isinstance(juros, (float, int)):
            if juros < 0 or juros > 1:
                raise ValueError('Os juros precisam ser entre 0 (0%) e 1 (100%).')
            self.saldo += self.saldo * juros
            return
        raise TypeError('O valor do juros precisa ser numérico')
