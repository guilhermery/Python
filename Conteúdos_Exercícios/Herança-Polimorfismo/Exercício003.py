#Metodos especiais são metodos com nomes que começam e terminam com duplo sublinhado.
#Servem para que os objetos se comportem como nativos em Python

class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    #Chamado quando usamos print() ou str() no objeto
    def __str__(self):
        return f"'{self.titulo}' por {self.autor}"

    #Chamado quando usamos len() no objeto
    def __len__(self):
        return self.paginas

#Cria o objeto
livro_python = Livro("Functions book", "GuilhermeRyan", 100)

#O tipo do objeto é justamente do tipo "Livro" que foi da classe usada para criar essa instância
type(livro_python)

#Metodo __str__ é chamado aqui e o print vai imprimir aquela string que foi retornada
print(livro_python)

#Metodo __len__ é chamado aqui
print(f'O livro tem {len(livro_python)} páginas.')