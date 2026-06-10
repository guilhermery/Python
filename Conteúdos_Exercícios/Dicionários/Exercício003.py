estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #É necessário copiar, pois senão a lista irá pegar apenas o ultimo
print(brasil)
for e in brasil: #Cada "e" é um dicionário
    for k, v in e.items(): #Para cada posição/nome k, o valor v do dicionario e
        print(f'O campo {k} tem valor {v}.')