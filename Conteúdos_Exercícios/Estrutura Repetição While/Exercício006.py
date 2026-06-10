n = int(input('Informe um número inteiro: '))
a1 = cont = a3 = 0
a2 = 1
while cont < n:
    print(a1)
    a3 = a1 + a2
    a1 = a2
    a2 = a3
    cont += 1
