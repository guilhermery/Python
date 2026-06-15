from pathlib import Path

pasta_atual = Path(__file__).parent
caminho = pasta_atual/"desafio.txt"

with open(caminho, "w", encoding="utf-8") as arquivo:
    arquivo.write("Linha1\nLinha2\nLinha3\nLinha4")

with open(caminho, "r", encoding="utf-8") as arquivo:
    for i, linha in enumerate(arquivo):
        if i < 3:
            print(linha.strip())

with open(caminho, "a", encoding="utf-8") as arquivo:
    arquivo.write("\nLinha5")