vitoria = {
    'PEDRA':'TESOURA',
    'TESOURA':'PAPEL',
    'PAPEL':'PEDRA'
}

opcoes = {
    'PEDRA': '🪨',
    'PAPEL': '📄',
    'TESOURA':'✂️'
}

print('=' * 42)
print('      PEDRA, PAPEL E TESOURA')
print('=' * 42)

print('\nREGRAS:')
print('-' * 42)
print('🪨 Pedra   vence ✂️ Tesoura')
print('📄 Papel   vence 🪨 Pedra')
print('✂️ Tesoura vence 📄 Papel')
print('🤝 Escolhas iguais = Empate')
print('-' * 42)

print('\nOPÇÕES DISPONÍVEIS:')
print('[ PEDRA ]  [ PAPEL ]  [ TESOURA ]')
print('=' * 42)

while True:
    jogador1 = input('Jogador 1 faça sua jogada: ').upper()
    jogador2 = input('Jogador 2 faça sua jogada: ').upper()
    if jogador1 in opcoes and jogador2 in opcoes:
        break
    else:
        print('Um dos jogadores não escolheu uma opção válida. Jogem novamente.')

print('\n              JO-KEN-PÔ!!!')
print('=' * 42)
print(f'{opcoes[jogador1]}  VS  {opcoes[jogador2]}')
print('=' * 42)

if jogador1 == jogador2:
    print(f'Empate! Pois os dois jogadores escolheram {jogador1}')
elif vitoria[jogador1] == jogador2:
    print(f'Jogador 1 venceu! Pois {jogador1} vence {jogador2}')
else:
    print(f'Jogador 2 venceu! Pois {jogador2} vence {jogador1}')