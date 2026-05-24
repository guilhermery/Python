import time
import random
from systems import attack
Bulbasauro = {
    'nome': 'Bulbasauro',
    'ataque': 6,
    'defesa': 6,
    'velocidade': 5,
    'hp': 30.0
}
Charmander = {
    'nome': 'Charmander',
    'ataque': 9,
    'defesa': 3,
    'velocidade': 7,
    'hp': 25.0
}
Squirtle = {
    'nome': 'Squirtle',
    'ataque': 4,
    'defesa': 9,
    'velocidade': 3,
    'hp': 40.0
}
espacamento = '---------------------------------------------------------'
cont = 1
vivo = True
print('Escolha seu primeiro Pokémon!!')
print(espacamento)
print('\033[34mSquirtle\033[m')
print('\033[31mCharmander\033[m')
print('\033[32mBulbasauro\033[m')
print(espacamento)
while True:
    pokemon = input('Qual você deseja? ')
    if pokemon == 'Squirtle':
        pokemon = Squirtle.copy()
        break
    elif pokemon == 'Charmander':
        pokemon = Charmander.copy()
        break
    elif pokemon == 'Bulbasauro':
        pokemon = Bulbasauro.copy()
        break
    else:
        print('Escolha um Pokémon válido!')
print(espacamento)
while True:
    pokemonadv = input('Escolha o pokemon adversário: ')
    if pokemonadv == 'Squirtle':
        pokemonadv = Squirtle.copy()
        break
    elif pokemonadv == 'Charmander':
        pokemonadv = Charmander.copy()
        break
    elif pokemonadv == 'Bulbasauro':
        pokemonadv = Bulbasauro.copy()
        break
    else:
        print('Escolha um Pokémon válido!')
print(espacamento)
print('Início de Batalha')
while True:
    print('Round {}:'.format(cont))
    time.sleep(1)
    if pokemon['velocidade'] > pokemonadv['velocidade']:
        while True:
            resposta = input('O seu Pokémon ataca primeiro! Deseja continuar? (S/N) ')
            if resposta in 'Nn':
                break
            elif resposta in 'Ss':
                break
            else:
                print('Informe uma resposta válida.')
        if resposta in 'Nn':
            print('\033[32mBatalha encerrada.\033[m')
            break
        time.sleep(1)
        pokemonadv['hp'] = attack.ataque(pokemonadv['hp'], pokemon['ataque'], pokemonadv['defesa'])
        vivo = attack.vidaInimigo(pokemonadv['hp'])
        if not vivo:
            break
        print('O Pokémon inimigo te ataca!')
        time.sleep(1)
        pokemon['hp'] = attack.ataque(pokemon['hp'], pokemonadv['ataque'], pokemon['defesa'])
        vivo = attack.vidaUsuario(pokemon['hp'])
        if not vivo:
            break
    elif pokemonadv['velocidade'] > pokemon['velocidade']:
        print('O Pokémon inimigo ataca primeiro!')
        time.sleep(1)
        pokemon['hp'] = attack.ataque(pokemon['hp'], pokemonadv['ataque'], pokemon['defesa'])
        vivo = attack.vidaUsuario(pokemon['hp'])
        if not vivo:
            break
        while True:
            resposta = input('O seu Pokémon ataca! Deseja continuar? (S/N) ')
            if resposta in 'Nn':
                break
            elif resposta in 'Ss':
                break
            else:
                print('Informe uma resposta válida.')
        if resposta in 'Nn':
            print('\033[32mBatalha encerrada.\033[m')
            break
        pokemonadv['hp'] = attack.ataque(pokemonadv['hp'], pokemon['ataque'], pokemonadv['defesa'])
        vivo = attack.vidaInimigo(pokemonadv['hp'])
        if not vivo:
            break
    elif pokemon['velocidade'] == pokemonadv['velocidade']:
        n = random.randint(1, 2)
        if n == 1:
            while True:
                resposta = input('O seu Pokémon ataca primeiro! Deseja continuar? (S/N) ')
                if resposta in 'Nn':
                    break
                elif resposta in 'Ss':
                    break
                else:
                    print('Informe uma resposta válida.')
            if resposta in 'Nn':
                print('\033[32mBatalha encerrada.\033[m')
                break
            time.sleep(1)
            pokemonadv['hp'] = attack.ataque(pokemonadv['hp'], pokemon['ataque'], pokemonadv['defesa'])
            vivo = attack.vidaInimigo(pokemonadv['hp'])
            if not vivo:
                break
            print('O Pokémon inimigo te ataca!')
            time.sleep(1)
            pokemon['hp'] = attack.ataque(pokemon['hp'], pokemonadv['ataque'], pokemon['defesa'])
            vivo = attack.vidaUsuario(pokemon['hp'])
            if not vivo:
                break
        else:
            print('O Pokémon inimigo ataca primeiro!')
            time.sleep(1)
            pokemon['hp'] = attack.ataque(pokemon['hp'], pokemonadv['ataque'], pokemon['defesa'])
            vivo = attack.vidaUsuario(pokemon['hp'])
            if not vivo:
                break
            while True:
                resposta = input('O seu Pokémon ataca! Deseja continuar? (S/N) ')
                if resposta in 'Nn':
                    break
                elif resposta in 'Ss':
                    break
                else:
                    print('Informe uma resposta válida.')
            if resposta in 'Nn':
                print('\033[32mBatalha encerrada.\033[m')
                break
            pokemonadv['hp'] = attack.ataque(pokemonadv['hp'], pokemon['ataque'], pokemonadv['defesa'])
            vivo = attack.vidaInimigo(pokemonadv['hp'])
            if not vivo:
                break
    cont += 1