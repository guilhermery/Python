print('Informe a idade e o peso, respectivamente:')
idade = int(input())
peso = int(input())
if idade < 12:
    print('Não Permitido')
else:
    if 12 <= idade <= 17:
        print('Categoria Juvenil')
    else:
        if idade >= 18 and peso <= 75:
            print('Categoria Adulto Leve')
        else:
            print('Categoria Adulto Pesado')
