#Definindo a classe (molde)
class Carro:

    #O metodo init é como um construtor. É chamado quando um novo objeto é criado.
    #O 'self' é a instancia do objeto que está sendo criado.
    def __init__(self, marca, modelo, ano):

        #Atributos do objeto
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False

    #Metodos do objeto
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f'O {self.modelo} está ligado')
        else:
            print(f'O {self.modelo} já estava ligado')

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f'O {self.modelo} foi desligado')
        else:
            print(f'O {self.modelo} já estava desligado')

    def exibir_informacoes(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}')

#Criando objeto (instância da classe Carro)
carro_1 = Carro("Volkswagen", "Fusca", 1967)
carro_1.exibir_informacoes()
carro_1.ligar()
carro_1.desligar()
print("")

#Criando objeto 2 (instância da classe Carro)
carro_2 = Carro("Tesla", "Model S", 2025)
carro_2.exibir_informacoes()
carro_2.ligar()
print("")

print(isinstance(carro_1, Carro))