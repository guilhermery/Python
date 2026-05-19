n = 6
print('Informe dois valores inteiros:')
v1, v2 = int(input()), int(input())
while n != 5:
    print('---------------------------------------')
    print('[1]Somar')
    print('[2]Multiplicar')
    print('[3]Maior')
    print('[4]Novos números')
    print('[5]Sair do programa')
    print('---------------------------------------')
    n = int(input('Informe a opção desejada: '))
    if n == 1:
        print('O resultado de {}+{} é {}'.format(v1, v2, v1+v2))
    elif n == 2:
        print('O resultado de {}x{} é {}'.format(v1, v2, v1*v2))
    elif n == 3:
        if v1 > v2:
            print('O maior valor é {}'.format(v1))
        elif v1 < v2:
            print('O maior valor é {}'.format(v2))
        else:
            print('Os dois valores são iguais')
    elif n == 4:
        print('Informe os novos valores:')
        v1, v2 = int(input()), int(input())
    elif n == 5:
        print('Saindo do programa...')
    else:
        print('Informe uma opção válida')