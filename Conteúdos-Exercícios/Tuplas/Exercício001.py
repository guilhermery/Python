#Tuplas são um tipo de variável composta e funcionam como se fossem strings
lanches = (
    'hamburguer',
    'suco',
    'pastel',
    'pudim'
)
print(lanches[-1])
print(len(lanches))
print(sorted(lanches)) #Mostra a tupla em ordem
for comida in lanches:
    print(f'Eu vou comer {comida}')
#for comida in range(0, len(lanches):
    #Coloca utilizando metodo range com a len(tamanho) da tupla
#for posicao, comida in enumerate(lanches):
    #Serve justamente para ter a posição do indice e o item da tupla