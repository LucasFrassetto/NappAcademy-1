class Conta:
    def __init__(self, **kwargs):
        """
        Construtor da classe Conta.
        Recebe por kwargs :
        - nome
        - limite
        - saldo

        Raises:
            ValueError: Caso o saldo seja menor ou igual a zero.
        """
        self.extrato = []
        self.limite = kwargs.get('limite', 500)
        self.nome = kwargs.get('nome', None)
        self.saldo = 0
        saldo = kwargs.get('saldo', self.saldo)
        if saldo < 0:
            raise ValueError('Saldo negativo')
        self.saldo = saldo
        self.extrato.append(('I', saldo))

    def deposito(self, valor):
        """
        Método para realizar depósito.
        Este método suporta somente números maiores que zero.

        Args:
            valor (float ou int): Valor positivo do depósito

        Raises:
            ValueError: Erro ocorre quando é informado valor negativo.
            TypeError: Quando o tipo passado não for inteiro ou float.
        """
        if isinstance(valor, (float, int)):
            if valor <= 0:
                raise ValueError('Valor do depósito precisa ser maior que zero')
            self.saldo = self.saldo + valor
            self.extrato.append(('D', valor))
            return
        raise TypeError('O depósito precisa ser numérico')

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
                raise ValueError('Valor do saque supera seu saldo e seu limite')
                return
            self.saldo = self.saldo - valor
            self.extrato.append(('S', valor))
            return valor
        raise TypeError('O valor do saque precisa ser numérico')

    def get_extrato(self):
        """
        Retorna a lista dos saques e depósitos feitos na conta.

        Returns:
            List: Lista de operações
        """
        return self.extrato
