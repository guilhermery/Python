pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
pessoa['idade'] = int(input('Ano de Nascimento: '))
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = (pessoa['contratação'] - pessoa['idade']) + 35
    pessoa['idade'] = 2026 - pessoa['idade']
    print('-='*35)
    print(pessoa)
    for pos, v in pessoa.items():
        print(f'{pos} tem o valor {v}')
else:
    pessoa['idade'] = 2026 - pessoa['idade']
    print('-=' * 35)
    print(pessoa)
    for pos, v in pessoa.items():
        print(f'{pos} tem o valor {v}')