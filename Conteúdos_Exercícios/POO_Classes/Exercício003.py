#Define a classe
class Carro:

    #Metodo construtor
    def __init__(self, marca, modelo, ano):
        #Inicializa os atributos
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self._velocidade = 0 #é um atributo protegido, não deve ser acessado diretamente
        self.__horsepower = 300 #é um atributo privado (name mangling), não deve ser acessado diretamente

    #Metodo getter para obter o valor da velocidade
    def get_velocidade(self):
        return self._velocidade

    #Metodo setter para alterar o valor da velocidade com lógica de controle
    def acelerar(self, valor):
        if valor > 0:
            self._velocidade += valor
            print(f'O {self.modelo} acelerou para {self._velocidade} km/h.')
        else:
            print('O valor de aceleração deve ser positivo.')

    #Metodo geral
    def frear(self, valor):
        if valor > 0:
            self._velocidade -= valor
            if self._velocidade < 0:
                self._velocidade = 0
            print(f'O {self.modelo} freou para a velocidade {self._velocidade} km/h.')
        else:
            print('O valor de freagem deve ser positivo.')

carro_encapsulado = Carro('Fiat', 'Pulse', 2024)

carro_encapsulado.acelerar(50)
print(f'Velocidade atual: {carro_encapsulado.get_velocidade()} km/h.')
carro_encapsulado.frear(20)
print(f'Velocidade atual : {carro_encapsulado.get_velocidade()} km/h.')

#Acessando diretamente o atributo protegido (não recomendado também)
print(carro_encapsulado._velocidade)

#Acesso direto (não recomendado pois quebra o encapsulamento)
carro_encapsulado._velocidade = 200
print(f'Velocidade alterada diretamente: {carro_encapsulado._velocidade} km/h.')