numeros = []
for c in range(5):
    valor = int(input('Digite um valor: '))
    if len(numeros) == 0:
        numeros.insert(0, valor)
    else:
        for pos in range(len(numeros)):
            if valor <= numeros[pos]:
                numeros.insert(pos, valor)
                break
            if pos == len(numeros) - 1:
                numeros.insert(len(numeros), valor)
print(numeros)