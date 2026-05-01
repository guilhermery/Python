cont = 0
n = int(input('Informe um número: '))
if n == 1:
    print('O número {} não é um número primo'.format(n))
else:
    for c in range(1, n+1):
        if n % c == 0:
            cont += 1
    if cont > 2:
        print('O número {} não é um número primo'.format(n))
    else:
        print('O número {} é um número primo'.format(n))