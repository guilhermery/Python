matriz = [[],[],[]]
somap = soma3 = maior = 0
for i in range(3):
    for c in range(3):
        matriz[i].append(int(input(f'Digite um valor para [{i}, {c}]: ')))
print('-='*30)
for i in range(3):
    for c in range(3):
        print(f'[  {matriz[i][c]}  ]', end=' ')
        if matriz[i][c] % 2 == 0:
            somap += matriz[i][c]
        if c == 2:
            soma3 += matriz[i][c]
        if i == 1:
            if c == 0:
                maior = matriz[i][c]
            elif matriz[i][c] > maior:
                maior = matriz[i][c]
    print('')
print('-='*30)
print(f'A soma dos valores pares é {somap}.')
print(f'A soma dos valores da terceira coluna é {soma3}.')
print(f'O maior valor da segunda linha é {maior}.')

