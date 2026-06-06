import time
import random

from systems import battle
from systems.pokemon import Pokemon

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
    if pokemon in pokemons:
        pokemon = pokemons[pokemon].copy()
        break
    else:
        print('Escolha um Pokémon válido!')
print(espacamento)
pokemonadv = pokemons[random.choice(list(pokemons.keys()))].copy()
print(f'Adversário escolheu {pokemonadv.nome}')
print(espacamento)
print('Início de Batalha')
while True:
    print(f'Round {cont}:')
    time.sleep(1)
    if pokemon.velocidade > pokemonadv.velocidade:
        vivo = battle.turno_usuario_primeiro(pokemon, pokemonadv)
    elif pokemonadv.velocidade > pokemon.velocidade:
        vivo = battle.turno_adversario_primeiro(pokemon, pokemonadv)
    elif pokemon.velocidade == pokemonadv.velocidade:
        vivo = battle.turno_velocidades_iguais(pokemon, pokemonadv)
    if not vivo:
        break
    cont += 1