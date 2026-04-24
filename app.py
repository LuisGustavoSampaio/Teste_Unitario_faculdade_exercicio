from flask import Flask, render_template, request
from model import Cliente, ContaCorrente, BancoDados

app = Flask(__name__)

banco = BancoDados()

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/criar_conta", methods=["POST"])
def criar_conta():
    nome = request.form["nome"]
    cpf = request.form["cpf"]
    saldo = float(request.form["saldo"])

    cliente = Cliente(nome, cpf, "01/01/2000", "SP")
    numero = len(banco.contas) + 1

    conta = ContaCorrente(cliente, numero)
    conta.depositar(saldo)

    cliente.adicionar_conta(conta)
    banco.adicionar_conta(conta)

    return render_template("conta.html", conta=conta)


if __name__ == "__main__":
    app.run(debug=True)