from abc import ABC, abstractmethod
from rich import print
from rich.table import Table

class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0

    @abstractmethod
    def calc_frete(self):
        pass

class Moto(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 0.5
    
    def calc_frete(self):
        self.frete = self.fator*self.distancia
        return f'R${self.frete}'
    
class Caminhao(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 1.2

    def calc_frete(self):
        if self.distancia < 50:
            return "Raio mínimo de 50km"
        else:
            self.frete = self.fator*self.distancia
            return f'R${self.frete}'
    
class Drone(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 9.5
    
    def calc_frete(self):
        if self.distancia > 10:
            return "Raio máximo de 10km"
        else: 
            self.frete = self.fator*self.distancia
            return f'R${self.frete}'
        
dist = 10
entrega_moto = Moto(dist)
entrega_caminhao = Caminhao(dist)
entrega_drone = Drone(dist)

tabela = Table(title="Tabela de Fretes")

tabela.add_column("Distancia")
tabela.add_column("Tipo")
tabela.add_column("Frete")

tabela.add_row(f"{dist}Km", type(entrega_moto).__name__, entrega_moto.calc_frete())
tabela.add_row(f"{dist}Km", type(entrega_caminhao).__name__, entrega_caminhao.calc_frete())
tabela.add_row(f"{dist}Km", type(entrega_drone).__name__, entrega_drone.calc_frete())

print(tabela)