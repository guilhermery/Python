soma = 0
for c in range (1, 7):
    n = int(input('Informe um valor: '))
    if n % 2 == 0:
        soma += n
print('A soma de todos os valores pares informados é igual a {}'.format(soma))