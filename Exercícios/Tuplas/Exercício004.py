import random
numeros = (
    random.randint(1,100),
    random.randint(1,100),
    random.randint(1,100),
    random.randint(1,100),
    random.randint(1,100),
)

for num in numeros:
    print(num, end=', ')
print(f'\nO maior número foi {max(numeros)}')
print(f'O menor número foi {min(numeros)}')