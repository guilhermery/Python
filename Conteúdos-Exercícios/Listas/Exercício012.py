import random
totjogos = []
jogo = []
print('-'*20)
print(''*6, 'JOGA NA MEGA SENA')
print('-'*20)
n = int(input('Informe quantos jogos devem ser gerados: '))
print('-='*3, f'  SORTEANDO {n} JOGOS  ', '-='*3)
for c in range(n):
    for i in range(6):
        jogo.append(random.randint(1, 60))
    totjogos.append(jogo[:])
    jogo.clear()
    print(f'Os valores sorteados para o {c+1}º jogo foram: {totjogos[c]}')
