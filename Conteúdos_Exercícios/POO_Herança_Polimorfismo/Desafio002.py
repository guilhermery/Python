from abc import ABC, abstractmethod

class BebidaQuente(ABC):
    def __init__(self):
        pass

    def preparar(self):
        print('--- Iniciando o Preparo ---')
        self.ferver_agua()
        self.misturar()
        self.servir()
        print('--- Bebida Pronta ---')

    def ferver_agua(self):
        print('1. Fervendo a água a 100 graus Celsius.')

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

class Cafe(BebidaQuente):
    def misturar(self):
        print('2. Passando água pressurizada pelo pó de café moído.')
    
    def servir(self):
        print('3. Servindo em xícara pequena.')

class Leite(BebidaQuente):
    def misturar(self):
        print('2. Passando vapor pressurizado pelo bico do leite.')

    def servir(self):
        print('3. Servindo na caneca grande, já com café.')

class Cha(BebidaQuente):
    def misturar(self):
        print('2. Passando água pressurizada pela erva.')
    
    def servir(self):
        print('3. Servindo em uma xícara pequena.')

bebida = Cafe()
bebida.preparar()