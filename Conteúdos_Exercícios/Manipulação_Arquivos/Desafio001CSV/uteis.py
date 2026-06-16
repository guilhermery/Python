import csv
from pathlib import Path

pasta_mae = Path(__file__).parent

# Para criar o arquivo caso ele não exista
if not (pasta_mae/"produtos.csv").exists():
    with open(pasta_mae / "produtos.csv", "w", newline="") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["id", "nome", "preco", "estoque"])

# Para cadastrar cada produto
def cadastrar_produto(nome, preco, estoque):
    id_atual = 1
    # Para pegar o id do próximo produto a ser adicionado
    with open(pasta_mae/"produtos.csv", "r") as arquivo:
        leitor = csv.DictReader(arquivo)

        for produto in leitor:
            id_atual = int(produto["id"]) + 1

    with open(pasta_mae/"produtos.csv", "a", newline="") as arquivo:
        escritor = csv.writer(arquivo)

        escritor.writerow([id_atual, nome, preco, estoque])

# Para listar produtos
def listar_produtos():
    with open(pasta_mae/"produtos.csv", "r") as arquivo:
        leitor = csv.DictReader(arquivo)

        for produto in leitor:
            if int(produto["estoque"]) > 0:
                print(produto)

# Para buscar produtos pelo nome
def buscar_produtos(nome):
    produto_encontrado = False
    with open(pasta_mae/"produtos.csv", "r") as arquivo:
        leitor = csv.DictReader(arquivo)

        for produto in leitor:
            if produto["nome"] == nome:
                print(f"Produto encontrado: {produto}")    
                produto_encontrado = True
        
        if produto_encontrado == False:
            print("Produto não encontrado.")

# Para atualizar o preco de algum produto
def atualizar_preco(nome, preco):
    produtos = []
    with open(pasta_mae/"produtos.csv", "r") as arquivo:
        leitor = csv.DictReader(arquivo)

        for produto in leitor:
            if nome == produto["nome"]:
                produto["preco"] = preco

            produtos.append(produto)

    # Para verificar se a lista possui produtos.
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    
    with open(pasta_mae/"produtos.csv", "w", newline="") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=produtos[0].keys())

        escritor.writeheader()

        escritor.writerows(produtos)