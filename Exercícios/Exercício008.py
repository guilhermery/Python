a = int(input('Informe o valor para A: '))
b = int(input('Informe um valor para B: '))
print('O valor de A e B, respectivamente, antes da inversão é {} e {}'.format(a, b))
c = a
a = b
b = c
print('O valor de A e B, respectivamente, após a inversão é {} e {}'.format(a, b))
