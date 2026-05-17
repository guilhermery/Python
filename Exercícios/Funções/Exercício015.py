import time
def interativo(funcao):
    print('==========================================')
    print(f'Acessando o manual do comando {funcao}')
    print('==========================================')
    help(funcao)

print('=============================')
print(' SISTEMA DE AJUDA PYHELP ')
print('=============================')
resp = input('Função ou Biblioteca > ')
interativo(help)