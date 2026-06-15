import csv
from pathlib import Path

caminho_mae = Path(__file__).parent

# Criar arquivo e escrever 
with open(caminho_mae/"usuarios.csv", "w", newline="") as arquivo:
    # Criar um objeto responsável por escrever o CSV
    escritor = csv.writer(arquivo)

    # Escrever uma linha
    escritor.writerow(["id", "nome", "email"])
    escritor.writerow([1, "Ana", "ana@gmail.com"])
    escritor.writerow([2, "Guilherme", "guilherme@gmail.com"])

# Ler um arquivo CSV

with open(caminho_mae/"usuarios.csv", "r") as arquivo:

    # Criar um objeto responsável por ler o CSV
    leitor = csv.reader(arquivo)

    # Para ler cada linha do arquivo 
    for linha in leitor:
        print(linha) # Imprime tudo como string, até números

        try:
            Id = int(linha[0]) # Caso seja número inteiro, transforma em um
            print(Id)
        except:
            pass
    
    