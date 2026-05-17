def leiaInt(frase):
    while True:
        num = input(frase)
        if num.isdigit():
            break
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
    return num

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')