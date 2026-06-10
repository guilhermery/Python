numeros = [x for x in range(1, 6)]

#A função map aplica a função anonima à lista de numeros.
quadrados = list(map(lambda x: x ** 2, numeros))

#A função filter + lambda filtra os pares dentro da lista de quadrados
quadrados_pares = list(filter(lambda x: x % 2 == 0, quadrados))

print(quadrados_pares)