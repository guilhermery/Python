soma = n = cont = 0
while True:
    n = int(input('Informe um número: '))
    if n != 999:
        soma += n
        cont += 1
    else:
        break
print(f'A soma entre os {cont} números informados é igual a: {soma}')