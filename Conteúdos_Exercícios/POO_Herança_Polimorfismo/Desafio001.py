from abc import ABC, abstractmethod
from rich.traceback import install
install()

class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, lados):
        super().__init__(4) #Define a qtd_lados como 4
        self.lados = lados

    def perimetro(self):
        p = self.qtd_lados*self.lados
        return p
    
    def area(self):
        a = self.lados**2
        return a

class Circulo(Poligono):
    def __init__(self, raio):
        super().__init__(0) #Define a qtd_lados como 0
        self.raio = raio

    def perimetro(self):
        p = 2*3.14*self.raio
        return p

    def area(self):
        a = 3.14*(self.raio**2)
        return a 
    
p1 = Quadrado(20)

print(f"Perímetro = {p1.perimetro():.1f}")
print(f"Área = {p1.area():.1f}")