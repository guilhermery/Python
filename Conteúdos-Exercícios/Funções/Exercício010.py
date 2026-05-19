def voto(nasc):
    """
    -> Calcula a idade de uma pessoa e retorna se o voto é obrigatorio, opcional ou negado
    :param ano: data de nascimento
    :return: valor literal: NEGADO, OPCIONAL, OBRIGATORIO
    """
    global idade
    idade = 2026 - nasc
    if idade < 18:
        return 'NÃO VOTA'
    elif idade > 65:
        return 'VOTO OPCIONAL'
    else:
        return 'VOTO OBRIGATÓRIO'

idade = int(input('Em que ano você nasceu? '))
voto = voto(idade)
print(f'Com {idade} anos: {voto}')