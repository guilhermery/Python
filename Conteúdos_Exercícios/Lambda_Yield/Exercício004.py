def carregando():
    print('25%')
    yield

    print('50%')
    yield

    print('75%')
    yield

    print('100%')


gen = carregando()

next(gen)
next(gen)
next(gen)
next(gen)