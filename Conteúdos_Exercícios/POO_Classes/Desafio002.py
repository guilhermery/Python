from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome = '', preco = 0):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        etiqueta = Panel(f"{self.nome:^41}\n{'-'*41}\n{f'{self.preco:,.2f}':.^41}", title='Produto', width=45)
        print(etiqueta)

p1 = Produto('iPhone 17 Pro Max', 25_000.85)
p1.etiqueta()

p2 = Produto('Notebook Gamer', 8_000.)
p2.etiqueta()