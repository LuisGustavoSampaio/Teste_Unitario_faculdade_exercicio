# model.py

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)


class Conta:
    def __init__(self, cliente, numero):
        self.saldo = 0
        self.numero = numero
        self.agencia = "0001"
        self.cliente = cliente
        self.historico = Historico()

    def sacar(self, valor):
        if valor > self.saldo:
            return False
        self.saldo -= valor
        return True

    def depositar(self, valor):
        self.saldo += valor
        return True


class ContaCorrente(Conta):
    def __init__(self, cliente, numero, limite=500, limite_saques=3):
        super().__init__(cliente, numero)
        self.limite = limite
        self.limite_saques = limite_saques
        self.saques_realizados = 0

    def sacar(self, valor):
        if valor > self.limite:
            return False

        if self.saques_realizados >= self.limite_saques:
            return False

        if super().sacar(valor):
            self.saques_realizados += 1
            return True

        return False


class ContaPoupanca(Conta):
    def __init__(self, cliente, numero, taxa_rendimento=0.005):
        super().__init__(cliente, numero)
        self.taxa_rendimento = taxa_rendimento

    def aplicar_rendimento(self):
        rendimento = self.saldo * self.taxa_rendimento
        self.saldo += rendimento
        return rendimento


class Cliente:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class BancoDados:
    def __init__(self):
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def listar_contas(self):
        return self.contas


class Transacao:
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)


class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)


class InvestimentoPoupanca(Transacao):
    def registrar(self, conta):
        if hasattr(conta, "aplicar_rendimento"):
            conta.aplicar_rendimento()
            conta.historico.adicionar_transacao(self)
