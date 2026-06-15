import csv
from pathlib import Path

pasta_mae = Path(__file__).parent

usuario = {
    "id":1,
    "nome":"Guilherme",
    "email":"guilherme@email.com"
}

usuarios = []

with open(pasta_mae/"usuarios.csv", "w", newline="") as arquivo:
    campos = ["id", "nome", "email"]

    # Criar um escritor que entende dicionários. Recebe o arquivo e nomes das colunas
    escritor = csv.DictWriter(arquivo, fieldnames=campos)

    # Escrever o header do CSV "primeira linha"
    escritor.writeheader()

    # Escrever uma linha com os dados
    escritor.writerow(usuario)

# Para ler o arquivo .CSV
with open(pasta_mae/"usuarios.csv", "r") as arquivo:
    
    # Criar o leitor que transforma o CSV em dicionário Python
    leitor = csv.DictReader(arquivo)

    for usuario in leitor:

        # Converter o id para inteiro
        try: 
            usuario["id"] = int(usuario["id"])
        except:
            pass

        # Adicionar o usuario lido dentro da lista de usuarios 
        usuarios.append(usuario)

print(usuario)
print(usuarios)

# Para alterar algo dentro do arquivo CSV 
for usuario in usuarios:
    if usuario['nome'] == 'Guilherme':
        usuario['nome'] = 'Guilherme Ryan'

with open(pasta_mae/"usuarios.csv", "w", newline="") as arquivo:

    # Criar o escritor usando como parametro para colunas as chaves do primeiro dicionário da lista de usuários
    escritor = csv.DictWriter(arquivo, fieldnames=usuarios[0].keys())
    
    # Criar as colunas a partir do escritor
    escritor.writeheader()

    # Cria as linhas de acordo com cada usuario dentro da lista de usuarios
    escritor.writerows(usuarios)