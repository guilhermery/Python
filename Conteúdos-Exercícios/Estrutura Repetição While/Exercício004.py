n = int(input('Informe um número: '))
n1 = n-1
fat = n
while n1 > 0:
    fat = fat*n1
    n1 -= 1
print('O fatorial de {} é igual a {}'.format(n, fat))