from rich import print
from rich.panel import Panel

class Churrasco:
    def __init__(self, titulo, quant):
        self.titulo = titulo
        self.quant = quant
        precokg = 82.40

    def analisar(self):
        print(Panel(
            f"Analisando [green]{self.titulo}[/] com [blue]{self.quant} convidados[/]"
            f"\nCada participante comerá 0.4kg e cada kg custa R$82.40"
            f"\nRecomendo [blue]comprar {self.quant*0.4}Kg[/] de carne"
            f"\nO custo total será de R${self.quant*0.4*82.40:.2f}"
            f"\nCada pessoa pagará R${82.40*0.4} para participar", title=self.titulo))

c1 = Churrasco('Churras dos Amigos', 15)
c1.analisar()