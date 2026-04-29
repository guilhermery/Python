nome = str(input('Qual o seu nome? '))
if nome == 'Guilherme':
    print('Que nome bonito!')
elif nome == 'Demogorgon':
    print('Que nome estranho!')
elif nome in 'Ana Claudia Jessica Juliana': #A condição é true se o nome for algum dentro do "in".
    print('Belo nome feminino!')
else:
    print('Nome bem normal.')
print('Tenha um bom dia, {}!'.format(nome))