print('Informe os valores de x e y, respectivamente:')
x, y = int(input()), int(input())

if x == 0 or y == 0:
    print('O ponto está sobre o Eixo ou na Origem')
elif x > 0 and y > 0:
    print('O ponto pertence ao 1° Quadrante')
elif x < 0 < y:
    print('O ponto pertence ao 2° Quadrante')
elif x < 0 and y < 0:
    print('O ponto pertence ao 3° Quadrante')
elif y < 0 < x:
    print('O ponto pertence ao 4° Quadrante')