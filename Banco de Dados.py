class BancoDados:
    def __init__(self):
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def listar_contas(self):
        return self.contas