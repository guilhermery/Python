from math import degrees as graus
from math import radians as radiano
from math import cos, sin, tan
#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do cosseno, seno e tangente do mesmo.
num = float(input("Informe o valor do ângulo: "))
num = radiano(num) #Serve para transformar o número em radianos, pois a função math utiliza eles.
print('O valor do seno do angulo {:.0f} é {:.1f}, o valor do cosseno é {:.1f} e o valor da tangente é {:.1f}'.format(round(graus(num), 2), sin(num), cos(num), tan(num)))
#Utilizei degrees para transformar de volta em angulo apenas para exibir o valor.