from rich import print
import time

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1
        self.final_livro = False
        print(f":open_book: [blue]Você acabou de abrir o livro '[red]{self.titulo}[/]' que tem [green]{self.paginas} páginas[/] no total. Você agora está na[/] [yellow]página {self.pagina_atual}[/]")

    def avancar_paginas(self, quant):
        paginas_avancadas = 0
        for i in range(self.pagina_atual, self.pagina_atual+quant, 1):
            if self.pagina_atual == self.paginas:
                self.final_livro = True
                break
            else:
                self.pagina_atual += 1
                time.sleep(0.5)
                print(f"Pág{self.pagina_atual} :arrow_right:  ", end='')
                paginas_avancadas += 1
        print(f"[blue]Você avançou {paginas_avancadas} páginas e agora está na página[/] [yellow]{self.pagina_atual}[/]")
        if self.final_livro == True:
            print(f":rotating_light:  [red]Você chegou ao final do livro '{self.titulo}'[/]")


livro1 = Livro('As vantagens de ser invisivel', 20)
livro1.avancar_paginas(5)
livro1.avancar_paginas(10)
livro1.avancar_paginas(100)