num = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in num:
        num.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não será adicionado.')
    resp = input('Deseja continuar? [S/N] ').upper()
    if resp == 'N':
        break
num.sort()
print('-='*30)
print(f'Você digitou os valores {num}')
