n = int(input('Informe um número: '))
decisao = int(input('Você deseja traduzir para binário (1), octal (2) ou hexadecimal (3)? '))
traducao = ''
if decisao == 1:
    while n > 0:
        traducao += str(n % 2)  # Pega o resto e soma na string
        n = n // 2  # Divisão inteira para ignorar o resto
elif decisao == 2:
    while n > 0:
        traducao = traducao + str(n % 8)
        n = n // 8
elif decisao == 3:
    digitos = '0123456789ABCDEF'
    while n > 0:
        traducao = traducao + digitos[n % 16]
        n = n // 16
elif decisao == 0:
    traducao = 0
else:
    print('Você não escolheu uma opção válida.')
if decisao in [1, 2, 3]:
    print('Resultado: {}'.format(traducao[::-1]))

