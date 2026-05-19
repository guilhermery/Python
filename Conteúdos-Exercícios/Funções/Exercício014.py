def notas(*numeros, sit=False):
    """
    -> Recebe várias notas e a situação e retorna um dicionário com o total de notas, a maior, a menor, a media e a situação caso seja verdadeira
    :param numeros: notas informadas
    :param sit: operador booleano caso deseje se a informação deve ser informada
    :return: retorna um dicionário com todas as informações
    """
    notasAlunos = dict()
    total = 0
    maior = numeros[0]
    menor = numeros[0]
    s = 0
    for v in numeros:
        s += v
        if v > maior:
            maior = v
        elif v < menor:
            menor = v
        total += 1
    notasAlunos['total'] = int(total)
    notasAlunos['maior'] = int(maior)
    notasAlunos['menor'] = int(menor)
    notasAlunos['média'] = float(s/total)
    if sit:
        if s/total >= 7:
            notasAlunos['situação'] = 'BOA'
        elif s/total >= 5:
            notasAlunos['situação'] = 'RAZOÁVEL'
        else:
            notasAlunos['situação'] = 'RUIM'
    return notasAlunos

resp = notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(resp)