matrizpares = [[(x, y) for y in range(3)] for x in range(3)]

print(matrizpares)
for coordenadas in matrizpares:
    print(coordenadas)

print('')
matriz = [[coluna+1 for coluna in range(3)] for linha in range(3)]

print(matriz)
for linhas in matriz:
    print(linhas)