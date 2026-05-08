aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno['nome']}: '))
if aluno['media'] >= 60:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'
print(f'Nome é igual a {aluno['nome']}')
print(f'Média é igual a {aluno['media']}')
print(f'Situação é igual a {aluno['situacao']}')