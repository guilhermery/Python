class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id #Atributo público
        self._titular = nome #Atributo protegido, sem alteração direta em main
        self.__saldo = saldo #Atributo privado, sem alteração direta em main e classes
        print(f'Conta {self.id} criada com sucesso. Saldo atual de R${self.__saldo:,.2f}')

    #Ao colocar print(objeto):
    def __str__(self):
        #return f'A conta {self.id} de {self._titular} tem R${self.__saldo:,.2f} de saldo.'
        return f'Estado atual da conta: {self.__dict__}'

    def depositar(self, valor):
        valor = abs(valor) #Retorna o valor absoluto, apenas positivos.
        print(f'Depósito de R${valor:.2f} autorizado na conta.')
        self.__saldo += valor

    def sacar(self, valor):
        valor = abs(valor) #Retorna o valor absoluto, apenas positivos.
        if valor > self.__saldo:
            print(f'Saque NEGADO de R${valor:.2f} na conta {self.id} SALDO INSUFICIENTE.')
        else:
            print(f'Saque de R${valor:.2f} autorizado na conta.')
            self.__saldo -= valor