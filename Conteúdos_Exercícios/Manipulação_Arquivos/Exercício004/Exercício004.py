from pathlib import Path
import pickle

pasta_mae = Path(__file__).parent

with open(pasta_mae/"dados.bin", "wb") as arquivo:
    meu_texto = "Aprendendo arquivos binários em Python"
    meus_bytes = meu_texto.encode("utf-8")
    arquivo.write(meus_bytes)

with open(pasta_mae/"dados.bin", "rb") as arquivo:
    conteudo_arquivo = arquivo.read()
    string_arquivo = conteudo_arquivo.decode("utf-8")
    print(string_arquivo)

dados_jogador = {"nome": "Guilherme", "nivel": 45, "itens": ["Espada", "Escudo"]}

with open(pasta_mae/"savegame.bin", "wb") as arquivo:
    pickle.dump(dados_jogador, arquivo)

with open(pasta_mae/"savegame.bin", "rb") as arquivo:
    jogo_carregado = pickle.load(arquivo)
    print("Dados recuperados do binário: ", jogo_carregado)
    print(type(jogo_carregado))

with open(pasta_mae/"imagem.jpg", "rb") as arquivo:
    bytes_da_imagem = arquivo.read()
    print(f"A imagem foi lida e possui {len(bytes_da_imagem)} bytes")

with open(pasta_mae/"imagem_copia.jpg", "wb") as arquivo_copia:
    arquivo_copia.write(bytes_da_imagem)
    print("Copia da imagem criada com sucesso!")