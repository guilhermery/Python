import random
n = random.randint(0, 5)
n1 = int(input('Tente adivinhar o número escolhido na faixa de 0 a 5: '))
if n1 == n:
    print('Parabens!! Você venceu.')
else:
    print('Poxa!! Você perdeu, o número era {}'.format(n))

