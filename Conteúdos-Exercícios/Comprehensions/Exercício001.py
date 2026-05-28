#Cria uma lista do quadrado dos numeros de 0 a 9
quadrados = [x ** 2 for x in range(9)]

print(f'Lista de quadrados de 0 a 8: {quadrados}')

#Cria uma lista dos numeros pares de 0 a 20
pares = [x for x in range(21) if x % 2 == 0]

print(f'Lista de números pares de 0 até 20: {pares}')

#Cria um dicionario com os numeros e o quadrado deles
quadrados_dict = {x: x ** 2 for x in range(6)}
print(f'Dicionario de quadrados: {quadrados_dict}')

#Cria um conjunto com os quadrados dos numeros sem repetição
quadrados_set = {x ** 2 for x in [1, 2, 2, 3, 3, 4, 5]}
print(f'Conjuntos de quadrados: {quadrados_set}')

#Generator expression
gen = (x ** 2 for x in range(6))
print(f'Generator: {gen}')

#Uma tupla com os quadrados dos numeros
quadrados_tupla = tuple(x ** 2 for x in range(6))
print(f'Tupla dos numeros quadrados: {quadrados_tupla}')