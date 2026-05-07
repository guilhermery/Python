numeros = []
numerospares = []
numerosimpares = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    print('Valor adicionado na lista!')
    r = str(input('Deseja digitar outro valor? [S/N]: '))
    if r in 'Nn':
        break
for c in numeros:
    if c % 2 == 0:
        numerospares.append(c)
    else:
        numerosimpares.append(c)
print('+='*30)
print(f'Todos os valores digitados foram {numeros}')
print(f'Os valores pares digitados foram {numerospares}')
print(f'Os valores ímpares digitados foram {numerosimpares}')