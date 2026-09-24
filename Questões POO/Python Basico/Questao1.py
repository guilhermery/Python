n1 = float(input("Informe a nota do primeiro bimestre: "))
n2 = float(input("Informe a nota do segundo bimestre: "))
mp = (2*n1 + 3*n2)/5

if mp >= 60:
    print("Aluno aprovado.")
elif mp < 20:
    print("Aluno reprovado.")
else:
    print("Aluno em prova final.")