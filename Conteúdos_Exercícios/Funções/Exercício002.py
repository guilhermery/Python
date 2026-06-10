def área(largura, comprimento):
    area = largura*comprimento
    print(f'A área do terreno é de {area:.2f} metros quadrados')

largura = float(input('Informe a largura do terreno: '))
comprimento = float(input('Informe o comprimento do terreno: '))
área(largura, comprimento)