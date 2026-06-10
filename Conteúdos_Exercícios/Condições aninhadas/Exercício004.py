color = {
    'limpa':'\033[m',
    'azul':'\033[34m',
    'amarelo':'\033[33m'
}
def padrao_cores(c): #A função facilita eu não ter que escrever tudo três vezes
    return c['amarelo'], c['limpa'], c['azul'], c['limpa']
print('Informe dois números inteiros: ')
n1, n2 = int(input()), int(input())
if n1 > n2: #O * dentro do .format é para desempacotar a função, pois ela retorna 4 variáveis, que é uma tupla
    print('O {}primeiro valor{} é {}maior{}'.format(*padrao_cores(color)))
elif n2 > n1:
    print('O {}segundo valor{} é {}maior{}'.format(*padrao_cores(color)))
else:
    print('{}Não existe{} valor maior, os dois são {}iguais{}'.format(*padrao_cores(color)))