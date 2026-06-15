import json
from pathlib import Path

# Pega o caminho atual da pasta pai
pasta_atual = Path(__file__).parent 

with open(pasta_atual/"livros.json", "r", encoding="utf-8") as arquivo:
    # Para ler um arquivo json como objeto Python (lista ou dicionário)
    livros = json.load(arquivo)
    # print(livros) #Imprime o objeto como um todo
    # print(type(livros)) #Mostra o tipo do objeto lido
    # print(livros[0]) #Imprime as informações do primeiro livro da lista
    # print(livros[0]["titulo"]) #Imprime o titulo do primeiro livro da lista

for livro in livros:
    # Para imprimir cada livro por vez da forma que eu escolher.
    if livro["em_estoque"]:
        print(f"{livro["titulo"]} custa R${livro["preco"]:.2f}")

print("\n")

# Adicionando novo livro
novo_livro = {
    "id": 3,
    "titulo": "Percy Jackson e o Mar de Monstros",
    "autor": "Rick Riordan",
    "preco": 29.90,
    "em_estoque" : True
}

livros.append(novo_livro)
print(livros)

with open(pasta_atual/"livros_att.json", "w", encoding="utf-8") as arquivo:
    json.dump(livros, arquivo, indent=4, ensure_ascii=False) # Ensure_ascii para acentuação

dados_livro = {"id": 4, "titulo": "Magnus Chase", "autor": "Rick Riordan", "preco": 29.90, "em_estoque": True}

# Python → string JSON
texto_json = json.dumps(dados_livro, ensure_ascii=False)

print(type(texto_json)) # Retorna tipo string

# String JSON → Python
texto_json = json.loads(texto_json)

print(type(texto_json)) # Retorna tipo dict