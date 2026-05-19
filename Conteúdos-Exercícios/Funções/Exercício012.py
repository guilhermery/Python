def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

nome = str(input('Nome do Jogador: '))
gols = str(input('Número de Gols: '))
if nome == '':
    if gols == '':
        ficha()
    else:
        ficha(gols=int(gols))
elif nome != '' and gols == '':
    ficha(nome)
else:
    ficha(nome, int(gols))