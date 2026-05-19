import time
print('CONTAGEM REGRESSIVA:')
for cont in range(10, -1, -1):
    print(cont)
    if cont == 0:
        break
    else:
        time.sleep(1)
print('FOGOOOOOO!')