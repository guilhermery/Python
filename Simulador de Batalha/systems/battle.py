import time
from . import user_input
def ataque_jogador(pokemon, pokemonadv):
    pokemonadv.hp = pokemonadv.hp - (pokemon.ataque * (100 / (100 + pokemonadv.defesa)))
    return vida_inimigo(pokemonadv.hp)

def ataque_inimigo(pokemon, pokemonadv):
    pokemon.hp = pokemon.hp - (pokemonadv.ataque * (100 / (100 + pokemon.defesa)))
    return vida_usuario(pokemon.hp)

def vida_usuario(hp):
    if hp <= 0:
        print('O hp do seu Pokémon desceu para 0.')
        print('O seu Pokémon desmaiou! Você perdeu.')
        print('\033[32mBatalha encerrada.\033[m')
        return False
    else:
        print(f'O seu hp desceu para {int(hp)}')
        time.sleep(1)
        return True

def vida_inimigo(hp):
    if hp <= 0:
        print('O hp do inimigo desceu para 0.')
        print('O Pokémon inimigo desmaiou! Você venceu. Parabens!!')
        print('\033[32mBatalha encerrada.\033[m')
        return False
    else:
        print(f'O hp do inimigo desceu para {int(hp)}')
        time.sleep(1)
        return True

def turno_usuario_primeiro(pokemon, pokemonadv):
    if not user_input.confirmar_ataque('O seu Pokémon ataca primeiro! Deseja continuar? (S/N) '):
        print('\033[32mBatalha encerrada.\033[m')
        return False
    time.sleep(1)
    vivo = ataque_jogador(pokemon, pokemonadv)
    if not vivo:
        return False
    print('O Pokémon inimigo te ataca!')
    time.sleep(1)
    vivo = ataque_inimigo(pokemon, pokemonadv)
    if not vivo:
        return False
    return vivo

def turno_adversario_primeiro(pokemonadv, pokemon):
    print('O Pokémon inimigo ataca primeiro!')
    time.sleep(1)
    vivo = ataque_inimigo(pokemon, pokemonadv)
    if not vivo:
        return False
    if not user_input.confirmar_ataque('O seu Pokémon ataca! Deseja continuar? (S/N) '):
        print('\033[32mBatalha encerrada.\033[m')
        return False
    vivo = ataque_jogador(pokemon, pokemonadv)
    if not vivo:
        return False
    return vivo