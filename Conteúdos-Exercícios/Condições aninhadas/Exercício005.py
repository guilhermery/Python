color = {
    'limpa':'\033[m',
    'amarelo':'\033[33m',
}
cor_padrao = (color['amarelo'], color['limpa'])
nasc = int(input('Informe o ano de nascimento: '))
if(2026 - nasc == 18):
    print('É a hora de se {}alistar{}!'.format(*cor_padrao))
elif(2026 - nasc < 18):
    print('Ainda vai se {}alistar no serviço militar{}!'.format(*cor_padrao))
else:
    print('Já passou do tempo do {}alistamento{}!'.format(*cor_padrao))