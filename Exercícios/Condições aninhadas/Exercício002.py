cores = {
    'limpa':'\033[m',
    'azul':'\033[34m',
    'vermelho':'\033[31m'
}
vCasa = float(input('Informe o valor da casa: '))
salario = float(input('Informe o salário do comprador: '))
tempo = int(input('Informe em quantos anos irá pagar: '))
prestacao = vCasa / (tempo*12)
if prestacao > (salario*0.3):
    print('Emprestimo {}negado{}!'.format(cores['vermelho'], cores['limpa']))
else:
    print('Emprestimo {}aprovado{}!'.format(cores['azul'], cores['limpa']))
