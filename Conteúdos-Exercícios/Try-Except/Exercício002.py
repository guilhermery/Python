def leiaInt(frase):
    while True:
        try:
            num = input(frase)
            int(num)
            return num
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não informar os dados!\033[m')
            num = 0
            return num
        except:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')

def leiaFloat(frase):
    while True:
        try:
            num = input(frase)
            float(num)
            return num
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não informar os dados!\033[m')
            num = 0
            return num
        except:
            print('\033[31mERRO! Digite um número real válido.\033[m')

nint = leiaInt('Digite um número inteiro: ')
rint = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {nint} e o real foi {rint}')