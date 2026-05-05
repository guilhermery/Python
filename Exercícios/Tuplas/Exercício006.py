listagem = (
    'Caderno', 10.99,
    'Lápis', 2,
    'Corretivo', 4.5,
    'Bolsa', 59.99,
    'Lapiseira', 6.80,
    'Caneta', 1.50,
    'Coleção', 7.00
)
print('-'*30)
print('LISTAGEM DE PREÇOS')
print('-'*30)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>6.2f}')
print('-'*30)
print('FIM DO PROGRAMA')