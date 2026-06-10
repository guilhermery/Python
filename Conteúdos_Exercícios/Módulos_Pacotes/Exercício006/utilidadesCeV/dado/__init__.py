def leiaDinheiro(frase):
    valido = False

    while not valido:
        entrada = input(frase).replace(',', '.').strip()

        if entrada.count('.') > 1:
            print(f'ERRO: "{entrada}" é um preço inválido')

        elif entrada.replace('.', '').isdigit():
            valido = True
            return float(entrada)

        else:
            print(f'ERRO: "{entrada}" é um preço inválido')