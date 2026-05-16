import random
import time
numeros = list()

def sorteia(numeros):
    print('Sorteando 5 valores da lista:', end=' ')
    for i in range(0, 5):
        n = random.randint(0, 1000)
        numeros.append(n)
        print(n, end=' ')
        time.sleep(0.5)
    print('PRONTO!')

def somaPar(numeros):
    soma = 0
    print(f'Somando os valores pares de {numeros}, temos', end=' ')
    for v in numeros:
        if v%2 == 0:
            soma += v
    print(soma)

sorteia(numeros)
somaPar(numeros)