class Pet:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50
        self.felicidade = 50

    def alimentar(self):
        self.fome = max(0, self.fome - 10) #Impede de ficar menor que 0
        print(f'Você alimentou o {self.nome}!! A fome desceu para {self.fome}')

    def brincar(self):
        self.felicidade = min(100, self.felicidade + 5)
        self.fome = min(100, self.fome + 5)
        print(f'Você brincou com o {self.nome}! A felicidade e a fome aumentaram.')

    def mostrar_status(self):
        print('-----Status-----')
        print(f'Nome: {self.nome}')
        print(f'Fome: {self.fome}')
        print(f'Felicidade: {self.felicidade}')

gaomon = Pet('Gaomon')
gaomon.brincar()
gaomon.alimentar()
gaomon.mostrar_status()