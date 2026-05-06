num = []
while True:
    num.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp == 'N':
        break
print(f'Foram digitados {len(num)} números')
num.sort(reverse=True)
print(f'A lista em forma decrescente é {num}')
if 5 in num:
    print(f'O número 5 foi digitado e está na lista')
else:
    print('O número 5 não foi digitado e não está na lista')
