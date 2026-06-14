from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.lista_favoritos = []
    
    def add_favoritos(self, favorito):
        self.lista_favoritos.append(favorito)

    def ficha(self):
        favoritos = "\n".join(f":video_game: [blue]{item}[/]" for item in self.lista_favoritos) 
        painel_ficha = Panel(
            f"Nome real: [black on blue]{self.nome}[/]"
            f"\nJogos favoritos:"
            f"\n{favoritos}",
            title=f"Jogador <{self.nick}>",
            width=45
        )
        print(painel_ficha)

j1 = Gamer("Guilherme Ryan", "Thunderus")
j1.add_favoritos('God of War')
j1.add_favoritos('Pokemon Black e White')
j1.add_favoritos('Downhill')
j1.ficha()