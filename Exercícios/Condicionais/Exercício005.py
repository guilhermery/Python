vel = float(input('Informe a velocidade do carro: '))
if vel > 80:
    multa = (vel - 80) * 7
    print('Você foi multado!! O valor da multa é de R${:.2f}'.format(multa))