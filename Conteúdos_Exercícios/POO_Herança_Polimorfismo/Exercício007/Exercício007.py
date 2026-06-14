from classes import Avaliacao
from rich import print, inspect

def main():
    av1 = Avaliacao("Guilherme", "Sistemas Computacionais", 9.5)
    av1.set_nota(10)
    print(f'{av1.nome} tirou {av1.get_nota()} em {av1.disciplina}')
    inspect(av1, private=True)

if __name__ == "__main__":
    main()