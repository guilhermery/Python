from pathlib import Path

pasta_atual = Path(__file__).parent
caminho = pasta_atual / "exemplo002.txt"

with open(caminho, "r", encoding="utf-8") as arquivo:
    # print(arquivo.read(5)) #Lê os 5 primeiros caracteres
    # arquivo.seek(0) #Reposiciona a leitura para o local informado (nesse caso, o início)
    # print(arquivo.read(5)) #Continua de onde o outro parou e conta com " "
    pass

with open(caminho, "r", encoding="utf-8") as arquivo:
    #Para ler um número delimitado de linhas:
    # for i, linha in enumerate(arquivo):
    #     if i < 3:
    #         print(linha.strip())
    pass

with open(caminho, "r+", encoding="utf-8") as arquivo:
    # arquivo.seek(10) #Inicia no caractere 10 e realiza o que vem após (write)
    # arquivo.write("TEXTO NOVO")
    pass

with open(caminho, "r+", encoding="utf-8") as arquivo:
    while True:
        bloco = arquivo.read(50)
        if not bloco:
            break
        print("Início do bloco")
        print(bloco)
        print("Fim do Bloco")