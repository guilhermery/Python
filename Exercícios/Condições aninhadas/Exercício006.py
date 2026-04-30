color = {
    "limpa":'\033[m',
    'amarelo':'\033[33m'
}
cor_padrao = (color['amarelo'], color['limpa'])
nasc = int(input('Informe o ano de nascimento: '))
idade = 2026 - nasc
if idade <= 9:
    print('Classificação {}Mirim{}'.format(*cor_padrao))
elif idade <= 14:
    print('Classificação {}Infantil{}'.format(*cor_padrao))
elif idade <= 19:
    print('Classificação {}Junior{}'.format(*cor_padrao))
elif idade == 20:
    print('Classificação {}Senior{}'.format(*cor_padrao))
else:
    print('Classificação {}Master{}'.format(*cor_padrao))