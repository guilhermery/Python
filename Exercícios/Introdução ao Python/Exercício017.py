#Faça um programa que le nome de quatro alunos, sorteie e escreva o nome do escolhido.
import random
n1 = input('Informe o primeiro nome: ')
n2 = input('Informe o segundo nome: ')
n3 = input('Informe o terceiro nome: ')
n4 = input('Informe o quarto nome: ')
print('O aluno escolhido foi {}'.format(random.choice([n1, n2, n3, n4])))
#Também pode ser feito por lista antes, por ex. nomes = [n1, n2, n3, n4].