times = (
'Palmeiras', 'Flamengo', 'Fluminense', 'São Paulo', 'Athletico-PR', 'Bahia', 'Red Bull Bragantino', 'Coritiba', 'Vitória', 'Botafogo', 'Atlético-MG', 'Grêmio', 'Corinthians', 'Cruzeiro', 'Internacional', 'Santos', 'Vasco da Gama', 'Mirassol', 'Chapecoense', 'Remo'
)
print(f'Os 5 primeiros colocados são: {times[:5]}')
print(f'Os últimos 4 colocados são {times[16:]}')
print(f'Em ordem alfabética: {sorted(times)}')
for cont in range(0, len(times)):
    if times[cont] == 'Chapecoense':
        print(f'O Chapecoense está em {cont+1}° lugar')