def teste(b):
    global a #serve para que a função utilize a variável gobal em vez de criar uma local
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')
#As variáveis declaradas dentro de teste, são variáveis locais, possuem escopo local.
#A variável a criada fora de teste, é uma variável global e possui escopo global.
#A variável a criada em teste, é uma variável local, e não modifica a global.