import time
def ataque(hp, ataque, defesa, vivo=True):
    hp = hp - (ataque * (100 / (100 + defesa)))
    return hp

def vidaUsuario(hp):
    if hp <= 0:
        print('O hp do seu Pokémon desceu para 0.')
        print('O seu Pokémon desmaiou! Você perdeu.')
        print('\033[32mBatalha encerrada.\033[m')
        return False
    else:
        print(f'O seu hp desceu para {int(hp)}')
        time.sleep(1)
        return True

def vidaInimigo(hp):
    if hp <= 0:
        print('O hp do inimigo desceu para 0.')
        print('O Pokémon inimigo desmaiou! Você venceu. Parabens!!')
        print('\033[32mBatalha encerrada.\033[m')
        return False
    else:
        print(f'O hp do inimigo desceu para {int(hp)}')
        time.sleep(1)
        return True

def continuar(frase):
    resposta = input(frase)
    if resposta in 'Nn':
        return False
    elif resposta in 'Ss':
        return True
    else:
        return None

def confirmar_ataque(frase):
    while True:
        continua = continuar(frase)
        if continua in [True, False]:
            return continua
        else:
            print('Informe uma resposta válida.')