class Digimon:
    """
    Essa classe cria um monstro Digimon que possui nome, vida e força. Ele consegue
    atacar, dormir e brincar.
    """
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.vida = vida
        self.forca = forca

    def atacar(self):
        return f'{self.nome} atacou o inimigo!!'
    
    def dormir(self):
        return f'{self.nome} tirou um cochilo...'
    
    def brincar(self):
        return f'{self.nome} brincou e está mais feliz :)'
    
    def __str__(self):
        return f'O {self.nome} possui {self.vida} de vida e {self.forca} de força.'

    def __getstate__(self):
        return f'Estado nome: {self.nome}. Vida: {self.vida}'
    
gaomon = Digimon('Gaomon', 300, 50)
agumon = Digimon('Agumon', 350, 45)
gaomon.atacar()
gaomon.dormir()
gaomon.brincar()
print(gaomon)
print(agumon)
print(gaomon.__dict__) #Atributo
print(gaomon.__getstate__()) #Metodo
print(gaomon.__class__) #Atributo
print(gaomon.__doc__)