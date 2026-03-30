n = input('Informe um número: ').zfill(4) #Essa função coloca 0 a esquerda quando não tiver nada
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))
