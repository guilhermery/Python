num = [3, 2, 6, 4]
num[2] = 6 #Troca o número de indice 2 pelo número 6
num.append(7) #Adiciona um numero na lista
num.sort() #Coloca a lista em ordem
num.insert(2, 0) #insere um número na posição indicada
num.pop(2) #remove elementos
print(f'A lista em ordem fica: {num}')
num.sort(reverse=True) #Mostra a ordem decrescente (ordem inversa)
print(f'A lista ao contrário fica: {num}')
print(f'Essa lista tem {len(num)} elementos') #Mostra o numero de valores da lista
if 10 in num:
    num.remove(4)
else:
    print(f'Não achei o número 4 na lista')
for c, v in enumerate(num):
    print(f'Na posição {c} encontrei o valor {v}!')