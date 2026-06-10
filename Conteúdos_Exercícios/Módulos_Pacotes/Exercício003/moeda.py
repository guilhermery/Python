def aumentar(preco, porc):
    preco = preco + (preco*(porc/100))
    return preco

def diminuir(preco, porc):
    preco = preco - (preco*(porc/100))
    return preco

def metade(preco):
    return preco/2

def dobro(preco):
    return preco * 2

def moeda(preco):
    return str(f'R${preco:.2f}').replace('.', ',')