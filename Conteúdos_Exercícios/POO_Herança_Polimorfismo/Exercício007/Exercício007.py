from classes import Avaliacao
from rich import print, inspect

def main():
    av1 = Avaliacao("Guilherme", "Sistemas Computacionais", 9.5)
    av1.nota = -234
    inspect(av1, private=True)

if __name__ == "__main__":
    main()