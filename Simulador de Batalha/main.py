import time
import random
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
        ataque1 = 4
        defesa1 = 9
        velocidade1 = 3
        hp1 = 40
        break
    elif pokemon == 'Charmander':
        ataque1 = 9
        defesa1 = 3
        velocidade1 = 7
        hp1 = 25
        break
    elif pokemon == 'Bulbasauro':
        ataque1 = 6
        defesa1 = 6
        velocidade1 = 5
        hp1 = 30
        break
    else:
        print('Escolha um Pokémon válido!')
print(espacamento)
while True:
    pokemonadv = input('Escolha o pokemon adversário: ')
    if pokemonadv == 'Squirtle':
        ataque2 = 4
        defesa2 = 9
        velocidade2 = 3
        hp2 = 40
        break
    elif pokemonadv == 'Charmander':
        ataque2 = 9
        defesa2 = 3
        velocidade2 = 7
        hp2 = 25
        break
    elif pokemonadv == 'Bulbasauro':
        ataque2 = 6
        defesa2 = 6
        velocidade2 = 5
        hp2 = 30
        break
    else:
        print('Escolha um Pokémon válido!')
print(espacamento)
print('Início de Batalha')
while True:
    print('Round {}:'.format(cont))
    time.sleep(1)
    if velocidade1 > velocidade2:
        while True:
            resposta = input('O seu Pokémon ataca primeiro! Deseja continuar? (S/N) ')
            if resposta == 'N':
                break
            elif resposta == 'S':
                break
            else:
                print('Informe uma resposta válida.')
        if resposta == 'N':
            print('\033[32mBatalha encerrada.\033[m')
            break
        time.sleep(1)
        hp2 = hp2 - (ataque1 *(100/(100+defesa2)))
        if hp2 <= 0:
            print('O hp do inimigo desceu para 0.')
            print('O Pokémon inimigo desmaiou! Você venceu. Parabens!!')
            print('\033[32mBatalha encerrada.\033[m')
            break
        else:
            print('O hp do inimigo desceu para {}'.format(int(hp2)))
            time.sleep(1)
        print('O Pokémon inimigo te ataca!')
        time.sleep(1)
        hp1 = hp1 - (ataque2 * (100/(100+defesa1)))
        if hp1 <= 0:
            print('O hp do seu Pokémon desceu para 0.')
            time.sleep(1)
            print('O seu Pokémon desmaiou! Você perdeu.')
            print('\033[32mBatalha encerrada.\033[m')
            break
        else:
            print('O hp do seu Pokémon desceu para {}'.format(int(hp1)))
            time.sleep(1)
    elif velocidade2 > velocidade1:
        print('O Pokémon inimigo ataca primeiro!')
        time.sleep(1)
        hp1 = hp1 - (ataque2*(100/(100+defesa1)))
        if hp1 <= 0:
            print('O hp do seu Pokémon desceu para 0.')
            time.sleep(1)
            print('O seu Pokémon desmaiou! Você perdeu.')
            print('\033[32mBatalha encerrada.\033[m')
            break
        else:
            print('O hp do seu Pokémon desceu para {}'.format(int(hp1)))
            time.sleep(1)
        while True:
            resposta = input('O seu Pokémon ataca! Deseja continuar? (S/N) ')
            if resposta == 'N':
                break
            elif resposta == 'S':
                break
            else:
                print('Informe uma resposta válida.')
        if resposta == 'N':
            print('\033[32mBatalha encerrada.\033[m')
            break
        hp2 = hp2 - (ataque1*(100/(100+defesa2)))
        if hp2 <= 0:
            print('O hp do inimigo desceu para 0.')
            print('O Pokémon inimigo desmaiou! Você venceu. Parabens!!')
            print('\033[32mBatalha encerrada.\033[m')
            break
        else:
            print('O hp do inimigo desceu para {}'.format(int(hp2)))
            time.sleep(1)
    elif velocidade1 == velocidade2:
        n = random.randint(1, 2)
        if n == 1:
            while True:
                resposta = input('O seu Pokémon ataca primeiro! Deseja continuar? (S/N) ')
                if resposta == 'N':
                    break
                elif resposta == 'S':
                    break
                else:
                    print('Informe uma resposta válida.')
            if resposta == 'N':
                print('\033[32mBatalha encerrada.\033[m')
                break
            time.sleep(1)
            hp2 = hp2 - (ataque1 * (100 / (100 + defesa2)))
            if hp2 <= 0:
                print('O hp do inimigo desceu para 0.')
                print('O Pokémon inimigo desmaiou! Você venceu. Parabens!!')
                print('\033[32mBatalha encerrada.\033[m')
                break
            else:
                print('O hp do inimigo desceu para {}'.format(int(hp2)))
                time.sleep(1)
            print('O Pokémon inimigo te ataca!')
            time.sleep(1)
            hp1 = hp1 - (ataque2 * (100 / (100 + defesa1)))
            if hp1 <= 0:
                print('O hp do seu Pokémon desceu para 0.')
                time.sleep(1)
                print('O seu Pokémon desmaiou! Você perdeu.')
                print('\033[32mBatalha encerrada.\033[m')
                break
            else:
                print('O hp do seu Pokémon desceu para {}'.format(int(hp1)))
                time.sleep(1)
        else:
            print('O Pokémon inimigo ataca primeiro!')
            time.sleep(1)
            hp1 = hp1 - (ataque2 * (100 / (100 + defesa1)))
            if hp1 <= 0:
                print('O hp do seu Pokémon desceu para 0.')
                time.sleep(1)
                print('O seu Pokémon desmaiou! Você perdeu.')
                print('\033[32mBatalha encerrada.\033[m')
                break
            else:
                print('O hp do seu Pokémon desceu para {}'.format(int(hp1)))
                time.sleep(1)
            while True:
                resposta = input('O seu Pokémon ataca! Deseja continuar? (S/N) ')
                if resposta == 'N':
                    break
                elif resposta == 'S':
                    break
                else:
                    print('Informe uma resposta válida.')
            if resposta == 'N':
                print('\033[32mBatalha encerrada.\033[m')
                break
            hp2 = hp2 - (ataque1 * (100 / (100 + defesa2)))
            if hp2 <= 0:
                print('O hp do inimigo desceu para 0.')
                print('O Pokémon inimigo desmaiou! Você venceu. Parabens!!')
                print('\033[32mBatalha encerrada.\033[m')
                break
            else:
                print('O hp do inimigo desceu para {}'.format(int(hp2)))
                time.sleep(1)
    cont += 1