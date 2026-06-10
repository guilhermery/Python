from rich import print
from rich import inspect

class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta {self.id} criada com sucesso. Saldo atual de R${self.saldo:.2f}')

    #Ao colocar print(objeto):
    def __str__(self):
        return f'A conta {self.id} de {self.titular} tem R${self.saldo:.2f} de saldo.'

    def depositar(self, valor):
        print(f'Depósito de R${valor:.2f} autorizado na conta.')
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Saque NEGADO de R${valor:.2f} na conta {self.id} SALDO INSUFICIENTE.')
        else:
            print(f'Saque de R${valor:.2f} autorizado na conta.')
            self.saldo -= valor

c1 = ContaBancaria(112, 'Guilherme', 2000)
c1.depositar(500)
c1.sacar(300)
print(c1)

inspect(c1) #Mostra todas as informações do objeto da classe ContaBancaria
inspect(ContaBancaria, all=True) #Mostra todas as informações da classe ao inves de usar __doc__ ou __dict__