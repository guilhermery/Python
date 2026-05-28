#Yield é um iterador, assim como a função map e os generators, pois devolve um objeto que produz os resultados sob demanda

def contador():
    print('Executando...')
    yield 1

    print('Continuando...')
    yield 2

    print('Finalizando...')
    yield 3


gen = contador()

print(next(gen)) #Executa apenas até o primeiro yield da função
print(next(gen)) #Executa após o primeiro yield até o segundo
print(next(gen)) #Executa após o segundo yield até o terceiro