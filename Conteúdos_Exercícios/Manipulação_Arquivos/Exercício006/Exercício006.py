import csv
from pathlib import Path

caminho_mae = Path(__file__).parent

with open(caminho_mae/"usuarios.csv", "w", newline="") as arquivo:
    # Criar um objeto responsável por escrever o CSV
    escritor = csv.writer(arquivo)

    # Escrever uma linha
    escritor.writerow(["id", "nome", "email"])
    escritor.writerow([1, "Ana", "ana@gmail.com"])
    escritor.writerow([2, "Guilherme", "guilherme@gmail.com"])

with open(caminho_mae/"usuarios.csv", "r") as arquivo:

    # Transforma as informações CSV em um dicionário
    leitor = csv.DictReader(arquivo)

    # Para cada usuario(chave) no dicionario, imprime nome
    for usuario in leitor:

        print(usuario["nome"])