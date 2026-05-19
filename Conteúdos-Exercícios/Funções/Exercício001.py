def mensagem(msg):
    print('-'*30)
    print(msg)
    print('-'*30)
def soma(a, b):
    s = a + b
    print(s)
def contador(*num):
    #Cria uma Tupla desempacotando os valores
    print(num)
    for valor in num:
        print(f'{valor} ', end='')
def dobra(lista):
    pos = 0
    while pos<len(lista):
        lista[pos] *= 2
        pos += 1
valores = [2, 4, 6, 7, 8, 10]
dobra(valores)
print(valores)
mensagem('      SISTEMA DE ALUNOS      ')
soma(b=4, a=5)
contador(2, 4, 6, 5)