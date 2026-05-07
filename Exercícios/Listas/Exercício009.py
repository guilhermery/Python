pessoas = list()
dados = list()
maiores = list()
menores = list()
tot = 0
maior = 0
menor = 0
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(int(input('Digite o peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Deseja continuar? '))
    if resp in 'Nn':
        break
for p, v in enumerate(pessoas):
    if v[0]:
        tot += 1
    if v[1]:
        if v[1] > maior:
            maior = v[1]
        if p == 0:
            menor = v[1]
        elif v[1] < menor:
            menor = v[1]
for p in pessoas:
    if p[1] == maior:
        maiores.append(p[0])
    elif p[1] == menor:
        menores.append(p[0])
print('-='*30)
print(f'Ao todo, você cadastrou {tot} pessoas.')
print(f'O maior peso foi de {maior:.1f}Kg. Peso de {maiores}')
print(f'O menor peso foi de {menor:.1f}Kg. Peso de {menores}')