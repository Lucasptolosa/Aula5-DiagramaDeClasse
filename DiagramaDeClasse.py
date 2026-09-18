from abc import ABC, abstractmethod
from datetime import date

class Transacao(ABC):

    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):

    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.depositar(self.valor)

    def __str__(self):
        return f"Depósito de R$ {self.valor:.2f}"

class Saque(Transacao):

    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.sacar(self.valor)

    def __str__(self):
        return f"Saque de R$ {self.valor:.2f}"

class Historico:

    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def mostrar_historico(self):

        print("\n===== HISTÓRICO =====")

        for transacao in self.transacoes:
            print(transacao)

class Cliente:

    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def realizar_transacao(self, conta, transacao):

        transacao.registrar(conta)

        conta.historico.adicionar_transacao(transacao)

class PessoaFisica(Cliente):

    def __init__(self, endereco, cpf, nome, data_nascimento):

        # chama o construtor de Cliente
        super().__init__(endereco)

        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Conta:

    def __init__(self, cliente, numero, agencia):

        self.saldo = 0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente

        self.historico = Historico()

        cliente.adicionar_conta(self)

    def sacar(self, valor):

        if valor <= 0:
            print("Valor inválido.")
            return False

        if valor > self.saldo:
            print("Saldo insuficiente.")
            return False

        self.saldo -= valor

        print(f"Saque realizado: R$ {valor:.2f}")

        return True

    def depositar(self, valor):

        if valor <= 0:
            print("Valor inválido.")
            return False

        self.saldo += valor

        print(f"Depósito realizado: R$ {valor:.2f}")

        return True

class ContaCorrente(Conta):

    def __init__(
        self,
        cliente,
        numero,
        agencia,
        limite,
        limite_saques
    ):

        # chama o construtor de Conta
        super().__init__(cliente, numero, agencia)

        self.limite = limite
        self.limite_saques = limite_saques

lucas = PessoaFisica(
    endereco="São Paulo - SP",
    cpf="123.456.789-00",
    nome="Lucas",
    data_nascimento=date(2007, 5, 10)
)


conta = ContaCorrente(
    cliente=lucas,
    numero=12345,
    agencia="0001",
    limite=1000,
    limite_saques=3
)

deposito1 = Deposito(1000)

saque1 = Saque(250)

deposito2 = Deposito(500)


lucas.realizar_transacao(conta, deposito1)

lucas.realizar_transacao(conta, saque1)

lucas.realizar_transacao(conta, deposito2)


print(f"\nSaldo atual: R$ {conta.saldo:.2f}")

conta.historico.mostrar_historico()