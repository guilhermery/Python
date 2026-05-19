num = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in num:
        num.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar.')
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
num.sort()
print('-='*30)
print(f'Você digitou os valores {num}')
