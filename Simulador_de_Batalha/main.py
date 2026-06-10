import random

from systems import battle
from systems.pokemon import Pokemon

bulbasauro = Pokemon("Bulbasauro", 6, 6, 5, 30.0)
charmander = Pokemon("Charmander", 9, 3, 7, 25.0)
squirtle = Pokemon("Squirtle", 4, 9, 3, 40.0)
pokemons = {
    'Charmander': charmander,
    'Squirtle': squirtle,
    'Bulbasauro': bulbasauro
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
battle.batalhar(pokemon, pokemonadv)