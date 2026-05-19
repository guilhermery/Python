palavras = (
    'COMER',
    'ESTUDAR',
    'VIVER',
    'CURSOEMVIDEO',
    'FUTEBOL',
    'PROGRAMADOR',
    'FUTURO',
    'GRATIS',
    'BRINCAR',
    'PRATICAR',
    'THYSS'
)
vogais = (
    'a', 'e', 'i', 'o', 'u'
)
for n in palavras:
    print(f'Na palavra {n} temos ', end='')
    for letra in n:
        if letra.lower() in vogais:
            print(f'{letra.lower()}', end=' ')
    print('\n')
