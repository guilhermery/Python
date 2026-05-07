teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
totmaior = 0
totmenor = 0

#Para adicionar na lista galera uma cópia da lista teste no estado atual:
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)

#Para dar print apenas em Gustavo:
print(galera[0][0])

pessoal = list()
dado = list()
for c in range(5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    pessoal.append(dado[:])
    dado.clear()

for p in pessoal:
    if p[1] >= 18:
        print(f'O {p[0]} é maior de idade!')
        totmaior += 1
    else:
        print(f'O {p[0]} é menor de idade!')
        totmenor += 1
print(f'Temos {totmaior} pessoas maior de idade e {totmenor} pessoas de menor.')