from pathlib import Path
"""
r: leitura
w: escrita (sobrescreve o conteúdo existente)
a: anexa ao final do arquivo
x: criar aquivo novo (se o arquivo já existir, dá erro)
rb: ler arquivo binário
wb: escrever arquivo binário
r+: leitura e escrita (so funciona se o arquivo já existir)
"""

#Para guardar o caminho da pasta em que está o arquivo, considerando que não é a pasta atual em execução
pasta_atual = Path(__file__).parent
caminho = pasta_atual / "exemplo001.txt"

#Criar um arquivo novo que não existe para escrever algo nele. O UTF-8 faz a acentuação correta
with open(caminho, "w", encoding='utf-8') as arquivo:
    arquivo.write("Olá, estou aprendendo manipulação de arquivos com Python!")
    arquivo.write("\nComo você está?")

#Adicionar conteúdo ao final do conteúdo presente no arquivo
with open(caminho, "a", encoding="utf-8") as arquivo:
    arquivo.write("\nEspero que esteja bem. ")

#Lê o conteúdo presente no arquivo. O UTF-8 lê a acentuação correta
with open(caminho, "r", encoding='utf-8') as arquivo:
    # conteudo = arquivo.read()
    # print(conteudo)
    for linha in arquivo:
        print(linha.rstrip()) #Remove espaços no final de cada linha, para evitar quebra de linha a mais 