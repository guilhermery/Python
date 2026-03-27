import emoji
from math import sqrt #Nesse momento, não usa o math.sqrt, mas apenas o sqrt.
#sqrt é para raiz quadrada. floor é para arredondar para baixo, ceil arredonda para cima, trunc tira as casas decimais.
num = int(input('Informe um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.1f}'.format(num, raiz))
print(emoji.emojize('Olá, mundo :smiling_face_with_sunglasses:'))