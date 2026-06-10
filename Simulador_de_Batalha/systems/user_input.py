def continuar(frase):
    resposta = input(frase)
    if resposta in 'Nn':
        return False
    elif resposta in 'Ss':
        return True
    else:
        return None

def confirmar_ataque(frase):
    while True:
        continua = continuar(frase)
        if continua in [True, False]:
            return continua
        else:
            print('Informe uma resposta válida.')