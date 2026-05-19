print('Informe o valor do comprimento de três retas')
r1, r2, r3 = float(input()), float(input()), float (input())
if r1+r2 > r3 and r1+r3 > r2 and r2+r3 > r1:
    if r1 == r2 and r1 == r3:
        print('As retas podem formar um triângulo equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('As retas podem formar um triângulo isóceles')
    else:
        print('As retas podem formar um triângulo escaleno')
else:
    print('As retas não formam um triângulo')