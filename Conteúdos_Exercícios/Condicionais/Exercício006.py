dist = float(input('Qual a distância da viagem? '))
if dist <= 200:
    valor = dist*0.50
else:
    valor =dist*0.45
print('O valor da viagem é de R${:.2f}'.format(valor))