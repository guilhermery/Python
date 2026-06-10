# dados = {
#     'nome':'Pedro',
#     'idade': 26
# }

#Para adicionar algo novo ao dicionário:
# dados['sexo'] = 'M'

#Para excluir um dado:
# del dados['idade']
# print(dados.values()) - Para mostrar os valores apenas
# print(dados.keys()) - Para mostrar as chaves (nome, idade)
# print(dados.items()) - Para mostrar tanto as chaves quanto os valores

# for k, v in dados.items():
#     print(f'o {k} é {v}')

pessoas = {
    'nome': 'Gustavo',
    'sexo': 'M',
    'idade': 22
}
print(pessoas['nome'])
print(f'O {pessoas['nome']} tem {pessoas['idade']} anos')
print(pessoas.keys())
for k in pessoas.keys():
    print(k)
pessoas['peso'] = 73.5
for k, v in pessoas.items():
    print(f'{k} = {v}')
