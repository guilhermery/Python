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