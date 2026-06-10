import math
co = float(input('Informe o comprimento do cateto oposto do triângulo: '))
ca = float(input('Informe o cateto adjacente: '))
hip = math.sqrt(pow(co, 2) + pow(ca, 2))
print('O valor do comprimento da hipotenusa é de {:.0f}'.format(hip))