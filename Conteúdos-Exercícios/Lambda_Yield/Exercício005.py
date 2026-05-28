def infinito():
    numero = 1

    while True:
        yield numero
        numero += 1


gen = infinito()

print(next(gen))
print(next(gen))
print(next(gen))