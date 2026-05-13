jogador = dict()
jogador['nome'] = str(input('Nome: '))
partidas = int(input('Quantidade de partidas: '))
jogador['gols'] = list()
jogador['total'] = 0
for i in range(0, partidas):
    jogador['gols'].append(int(input(f'Quantos gols na partida {i+1}? ')))
    jogador['total'] += jogador['gols'][i]
print('-='*30)
print(jogador)
print('-='*30)
for pos, v in jogador.items():
    print(f'O campo {pos} tem o valor {v}.')
print('-='*30)
print(f'O jogador {jogador['nome']} jogou {partidas} partidas.')
for pos, v in enumerate(jogador['gols']):
    print(f'   => Na partida {pos+1}, fez {v} gols.')
print(f'Foi um total de {jogador['total']} gols.')