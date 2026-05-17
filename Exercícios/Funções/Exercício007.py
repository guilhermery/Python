#docstrings são strings de documentação como as que são mostradas acima
#colocar parametros opcionais são importantes para o caso de não serem colocados todos os valores na chamada
def contador(i=0, f=0, p=1):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')

def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado.
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    :return: sem retorno
    """
    s = a + b + c
    print(f'A soma vale {s}')

help(contador)
somar(3, 4, 6)
somar(4, 3)