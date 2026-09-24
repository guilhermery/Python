while True:
    L = int(input("Informe um valor maior que 0: "))
    if L < 0:
        input("O valor deve ser positivo")
    else:
        break
t1 = 1
t2 = 1
result = t1+t2
print(f"{t1}, {t2}, ", end="")
for i in range(L):
    print("{result}, ", end="")
