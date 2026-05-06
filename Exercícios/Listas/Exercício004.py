numeros = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0:
        numeros.append(n)
    elif n > numeros[len(numeros)-1]:
        numeros.append(n)
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados em ordem crescente foram: {numeros}')
