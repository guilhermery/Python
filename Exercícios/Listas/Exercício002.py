#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista
num = []
for c in range(0, 5):
    num.append(int(input('Digite um valor: ')))
print('=-'*25)
print(f'Você digitou os valores {num}')
for c, v in enumerate(num):
    if v == max(num):
        print(f'O maior valor digitado foi {v} na posição {c}!')
    elif v == min(num):
        print(f'O menor valor digitado foi {v} na posição {c}!')