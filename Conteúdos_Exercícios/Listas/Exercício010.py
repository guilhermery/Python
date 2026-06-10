numeros = [[], []]
for c in range(7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print('-='*30)
print(f'Os valores pares digitados foram {numeros[0]}')
print(f'Os valores ímpares digitados foram {numeros[1]}')