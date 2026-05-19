salario = float(input('Informe o valor do salário: '))
if salario > 1250:
    salario = salario + (salario*0.10)
else:
    salario = salario + (salario*0.15)
print('O salário com aumento fica de R${:.2f}'.format(salario))
