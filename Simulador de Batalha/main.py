import time
import random
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
        pokemonadv['hp'] = pokemonadv['hp'] - (pokemon['ataque'] * (100/(100+pokemonadv['defesa'])))
        if pokemonadv['hp'] <= 0:
            print('O hp do inimigo desceu para 0.')
            print('O Pokémon inimigo desmaiou! Você venceu. Parabens!!')
            print('\033[32mBatalha encerrada.\033[m')
            break
        else:
            print('O hp do inimigo desceu para {}'.format(int(pokemonadv['hp'])))
            time.sleep(1)
        print('O Pokémon inimigo te ataca!')
        time.sleep(1)
        pokemon['hp'] = pokemon['hp'] - (pokemonadv['ataque'] *(100/(100+pokemon['defesa'])))
        if pokemon['hp'] <= 0:
            print('O hp do seu Pokémon desceu para 0.')
            time.sleep(1)
            print('O seu Pokémon desmaiou! Você perdeu.')
            print('\033[32mBatalha encerrada.\033[m')
            break
        else:
            print('O hp do seu Pokémon desceu para {}'.format(int(pokemon['hp'])))
            time.sleep(1)
    elif pokemonadv['velocidade'] > pokemon['velocidade']:
        print('O Pokémon inimigo ataca primeiro!')
        time.sleep(1)
        pokemon['hp'] = pokemon['hp'] - (pokemonadv['ataque'] *(100/(100+pokemon['defesa'])))
        if pokemon['hp'] <= 0:
            print('O hp do seu Pokémon desceu para 0.')
            time.sleep(1)
            print('O seu Pokémon desmaiou! Você perdeu.')
            print('\033[32mBatalha encerrada.\033[m')
            break
        else:
            print('O hp do seu Pokémon desceu para {}'.format(int(pokemon['hp'])))
            time.sleep(1)
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
        pokemonadv['hp'] = pokemonadv['hp'] - (pokemon['ataque'] * (100/(100+pokemonadv['defesa'])))
        if pokemonadv['hp'] <= 0:
            print('O hp do inimigo desceu para 0.')
            print('O Pokémon inimigo desmaiou! Você venceu. Parabens!!')
            print('\033[32mBatalha encerrada.\033[m')
            break
        else:
            print('O hp do inimigo desceu para {}'.format(int(pokemonadv['hp'])))
            time.sleep(1)
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
            pokemonadv['hp'] = pokemonadv['hp'] - (pokemon['ataque']*(100/(100+pokemonadv['defesa'])))
            if pokemonadv['hp'] <= 0:
                print('O hp do inimigo desceu para 0.')
                print('O Pokémon inimigo desmaiou! Você venceu. Parabens!!')
                print('\033[32mBatalha encerrada.\033[m')
                break
            else:
                print('O hp do inimigo desceu para {}'.format(int(pokemonadv['hp'])))
                time.sleep(1)
            print('O Pokémon inimigo te ataca!')
            time.sleep(1)
            pokemon['hp'] = pokemon['hp'] - (pokemonadv['ataque']*(100/(100+pokemon['defesa'])))
            if pokemon['hp'] <= 0:
                print('O hp do seu Pokémon desceu para 0.')
                time.sleep(1)
                print('O seu Pokémon desmaiou! Você perdeu.')
                print('\033[32mBatalha encerrada.\033[m')
                break
            else:
                print('O hp do seu Pokémon desceu para {}'.format(int(pokemon['hp'])))
                time.sleep(1)
        else:
            print('O Pokémon inimigo ataca primeiro!')
            time.sleep(1)
            pokemon['hp'] = pokemon['hp'] - (pokemonadv['ataque']*(100/(100+pokemon['defesa'])))
            if pokemon['hp'] <= 0:
                print('O hp do seu Pokémon desceu para 0.')
                time.sleep(1)
                print('O seu Pokémon desmaiou! Você perdeu.')
                print('\033[32mBatalha encerrada.\033[m')
                break
            else:
                print('O hp do seu Pokémon desceu para {}'.format(int(pokemon['hp'])))
                time.sleep(1)
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
            pokemonadv['hp'] = pokemonadv['hp'] - (pokemon['ataque']*(100/(100+pokemonadv['defesa'])))
            if pokemonadv['hp'] <= 0:
                print('O hp do inimigo desceu para 0.')
                print('O Pokémon inimigo desmaiou! Você venceu. Parabens!!')
                print('\033[32mBatalha encerrada.\033[m')
                break
            else:
                print('O hp do inimigo desceu para {}'.format(int(pokemonadv['hp'])))
                time.sleep(1)
    cont += 1