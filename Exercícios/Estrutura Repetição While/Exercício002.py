import random
n = random.randint(0,10)
n1 = 12
cont = 0
while n1 != n:
    n1 = int(input('Adivinhe um número de 0 a 10: '))
    cont += 1
print('Foram necessários {} palpites para vencer'.format(cont))