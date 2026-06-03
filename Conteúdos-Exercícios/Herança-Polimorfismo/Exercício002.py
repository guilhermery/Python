class Veiculo:
    def __init__(self, marca, modelo):

        #Atributos do objeto
        self.marca = marca
        self.modelo = modelo

    def exibir_informacoes(self):
        print(f'Veiculo genérico: {self.marca} {self.modelo}')

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    #Sobrescrevendo o metodo da classe pai
    def exibir_informacoes(self):
        print(f'Carro: {self.marca} {self.modelo} | Portas: {self.portas}')

class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    # Sobrescrevendo o metodo da classe pai
    def exibir_informacoes(self):
        print(f'Moto: {self.marca} {self.modelo} | Cilindradas: {self.cilindradas}')

#Lista de veiculos de tipos diferentes:
veiculos = [
    Carro('Toyota', 'Corolla', 4),
    Moto('Yamaha', 'MT-07', 700),
    Veiculo("Calloi", "Ceci")
]

#O metodo se comporta de forma diferente em cada objeto da classe filha
for v in veiculos:
    v.exibir_informacoes() #Polimorfismo em ação