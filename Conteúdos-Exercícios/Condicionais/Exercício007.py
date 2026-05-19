print('Informe três números inteiros:')
n1, n2, n3 = int(input()), int(input()), int(input())
if n1>n2 and n1>n3:
    maior = n1
    if n2>n3:
        menor = n3
    else:
        menor = n2
elif n2>n3 and n2>n1:
    maior = n2
    if n3>n1:
        menor = n1
    else:
        menor = n3
else:
    maior = n3
    if n2>n1:
        menor = n1
    else:
        menor = n2
print('O maior valor informado foi {} e o menor foi {}'.format(maior, menor))
