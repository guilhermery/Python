import time
def maior(*num):
    maior = 0
    tamanho = len(num)
    print('-='*30)
    print('Analisando os valores passados...')
    for v in num:
        print(v, end=' ')
        time.sleep(0.5)
        if v > maior:
            maior = v
    print(f'Foram informados {tamanho} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()