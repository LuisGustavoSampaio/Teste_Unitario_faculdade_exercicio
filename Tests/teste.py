import os
import sys
import unittest


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from model import Cliente, ContaPoupanca, InvestimentoPoupanca


class TestInvestimentoPoupanca(unittest.TestCase):
    def test_deve_aplicar_rendimento_ao_investir_na_poupanca(self):
        # Arrange
        cliente = Cliente("Luis", "12345678900", "01/01/2000", "Salvador")
        conta_poupanca = ContaPoupanca(cliente, numero=1, taxa_rendimento=0.01)
        conta_poupanca.depositar(1000)
        investimento = InvestimentoPoupanca()

        # Act
        investimento.registrar(conta_poupanca)

        # Assert
        self.assertEqual(conta_poupanca.saldo, 1010)
        self.assertEqual(len(conta_poupanca.historico.transacoes), 1)
        self.assertIs(conta_poupanca.historico.transacoes[0], investimento)


if __name__ == "__main__":
    unittest.main()
