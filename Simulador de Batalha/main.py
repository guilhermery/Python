import time
import random

from systems import attack
class Pokemon:
    def __init__(self, nome, ataque, defesa, velocidade, hp):
        self.nome = nome
        self.ataque = ataque
        self.defesa = defesa
        self.velocidade = velocidade
        self.hp = hp

    def copy(self):
        return Pokemon(
            self.nome,
            self.ataque,
            self.defesa,
            self.velocidade,
            self.hp
        )

escolhas = ['Bulbasauro', 'Charmander', 'Squirtle']
Bulbasauro = Pokemon("Bulbasauro", 6, 6, 5, 30.0)
Charmander = Pokemon("Charmander", 9, 3, 7, 25.0)
Squirtle = Pokemon("Squirtle", 4, 9, 3, 40.0)
pokemons = {
    'Charmander': Charmander,
    'Squirtle': Squirtle,
    'Bulbasauro': Bulbasauro
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
    if pokemon in escolhas:
        pokemon = pokemons[pokemon].copy()
        break
    else:
        print('Escolha um Pokémon válido!')
print(espacamento)
pokemonadv = pokemons[random.choice(escolhas)].copy()
print(f'Adversário escolheu {pokemonadv.nome}')
print(espacamento)
print('Início de Batalha')
while True:
    print(f'Round {cont}:')
    time.sleep(1)
    if pokemon.velocidade > pokemonadv.velocidade:
        if not attack.confirmar_ataque('O seu Pokémon ataca primeiro! Deseja continuar? (S/N) '):
            print('\033[32mBatalha encerrada.\033[m')
            break
        time.sleep(1)
        pokemonadv.hp = attack.ataque(pokemonadv.hp, pokemon.ataque, pokemonadv.defesa)
        vivo = attack.vidaInimigo(pokemonadv.hp)
        if not vivo:
            break
        print('O Pokémon inimigo te ataca!')
        time.sleep(1)
        pokemon.hp = attack.ataque(pokemon.hp, pokemonadv.ataque, pokemon.defesa)
        vivo = attack.vidaUsuario(pokemon.hp)
        if not vivo:
            break
    elif pokemonadv.velocidade > pokemon.velocidade:
        print('O Pokémon inimigo ataca primeiro!')
        time.sleep(1)
        pokemon.hp = attack.ataque(pokemon.hp, pokemonadv.ataque, pokemon.defesa)
        vivo = attack.vidaUsuario(pokemon.hp)
        if not vivo:
            break
        if not attack.confirmar_ataque('O seu Pokémon ataca! Deseja continuar? (S/N) '):
            print('\033[32mBatalha encerrada.\033[m')
            break
        pokemonadv.hp = attack.ataque(pokemonadv.hp, pokemon.ataque, pokemonadv.defesa)
        vivo = attack.vidaInimigo(pokemonadv.hp)
        if not vivo:
            break
    elif pokemon.velocidade == pokemonadv.velocidade:
        n = random.randint(1, 2)
        if n == 1:
            if not attack.confirmar_ataque('O seu Pokémon ataca primeiro! Deseja continuar? (S/N) '):
                print('\033[32mBatalha encerrada.\033[m')
                break
            time.sleep(1)
            pokemonadv.hp = attack.ataque(pokemonadv.hp, pokemon.ataque, pokemonadv.defesa)
            vivo = attack.vidaInimigo(pokemonadv.hp)
            if not vivo:
                break
            print('O Pokémon inimigo te ataca!')
            time.sleep(1)
            pokemon.hp = attack.ataque(pokemon.hp, pokemonadv.ataque, pokemon.defesa)
            vivo = attack.vidaUsuario(pokemon.hp)
            if not vivo:
                break
        else:
            print('O Pokémon inimigo ataca primeiro!')
            time.sleep(1)
            pokemon.hp = attack.ataque(pokemon.hp, pokemonadv.ataque, pokemon.defesa)
            vivo = attack.vidaUsuario(pokemon.hp)
            if not vivo:
                break
            if not attack.confirmar_ataque('O seu Pokémon ataca! Deseja continuar? (S/N) '):
                print('\033[32mBatalha encerrada.\033[m')
                break
            pokemonadv.hp = attack.ataque(pokemonadv.hp, pokemon.ataque, pokemonadv.defesa)
            vivo = attack.vidaInimigo(pokemonadv.hp)
            if not vivo:
                break
    cont += 1