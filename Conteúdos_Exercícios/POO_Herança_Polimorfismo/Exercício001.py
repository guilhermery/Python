#Classe Pai (Superclasse)
class Veiculo:

    #Metodo construtor da classe pai
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False

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

#Classe filha (Subclasse que herda de veiculo)
class Carro(Veiculo):

    #Metodo construtor da classe filha
    def __init__(self, marca, modelo, portas):
        #super().__init__() chama o construtor da classe pai
        super().__init__(marca, modelo)
        self.portas = portas

    def exibir_info_carro(self,):
        print(f'Carro: {self.marca} {self.modelo}, Portas: {self.portas}')

#Outra classe filha
class Moto(Veiculo):

    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    def empinar(self):
        print(f'A moto {self.modelo} está empinando! Cuidado.')

    def exibir_info_moto(self):
        print(f'Moto: {self.marca} {self.modelo}, Cilindradas: {self.cilindradas}')

meu_carro = Carro('Volkswagen', 'Golf', 4)

minha_moto = Moto('Honda', 'CB 500', 500)

meu_carro.exibir_info_carro()

meu_carro.ligar() #Metodo herdado de veiculo

minha_moto.ligar() #Metodo herdado de veiculo
minha_moto.empinar() #Metodo proprio da moto