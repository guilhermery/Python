import random
from abc import ABC, abstractmethod
from rich import print

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []
    
    def atacar(self, alvo, forca):
        dano = random.randint(1, forca)
        print(f"{self.nome}({self.vida}) atacou {alvo.nome}({alvo.vida}) com um {random.choice(self.golpes)} de força {forca}")
        alvo.receber_dano(dano)

    def receber_dano(self, dano):
        print(f"{self.nome} recebeu dano de {dano}!")
        self.vida -= dano

    @abstractmethod
    def curar(self):
        pass

class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Soco', 'Punho Giratório', 'Chute']

    def curar(self):
        cura = random.randint(1, 100)
        self.vida += cura
        print(f"{self.nome} enrolou uma atadura nos ferimentos e recuperou {cura} pontos de vida.")

class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Meteoro', 'Raio', 'Feixe de Luz']

    def curar(self):
        cura = random.randint(1, 100)
        self.vida += cura
        print(f"{self.nome} fez magia de cura e recuperou {cura} pontos de vida.")

p1 = Guerreiro("Kratos", 2000)
p2 = Mago("Merlin", 3000)

p1.atacar(p2, 1000)
p2.curar()
p2.atacar(p1, 2000)
p1.curar()