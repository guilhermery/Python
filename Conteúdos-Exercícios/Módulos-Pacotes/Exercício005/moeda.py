def aumentar(preco, porc, formatado=False):
    preco = preco + (preco*(porc/100))
    if formatado:
        return str(f'R${preco:.2f}').replace('.', ',')
    else:
        return preco

def diminuir(preco, porc, formatado=False):
    preco = preco - (preco*(porc/100))
    if formatado:
        return str(f'R${preco:.2f}').replace('.', ',')
    else:
        return preco

def metade(preco, formatado=False):
    if formatado:
        return str(f'R${preco/2:.2f}').replace('.', ',')
    else:
        return preco/2

def dobro(preco, formatado=False):
    if formatado:
        return str(f'R${preco*2:.2f}').replace('.', ',')
    else:
        return preco*2

def moeda(preco):
    return str(f'R${preco:.2f}').replace('.', ',')

def resumo(preco, porcmaior, porcmenor):
    print('-'*29)
    print('       RESUMO DO VALOR       ')
    print('-'*29)
    print(f'Preço analisado:   ', end='')
    print(moeda(preco))
    print(f'Dobro do preço:   ', end='')
    print(dobro(preco, True))
    print(f'Metade do preço:   ', end='')
    print(metade(preco, True))
    print(f'{porcmaior}% de aumento:   ', end='')
    print(aumentar(preco, porcmaior, True))
    print(f'{porcmenor}% de redução:   ', end='')
    print(diminuir(preco, porcmenor, True))
    print('-' * 29)