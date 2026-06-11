from rich import print, inspect
from classes import Aluno, Professor, Funcionario

def main():    
    a1 = Aluno('Guilherme', 20, 'ADS', '2026.1')
    a1.fazer_matricula()
    a1.fazer_aniversario()
    inspect(a1, methods=True)

    p1 = Professor('Samuel', 37, 'Biologia', 'Mestre')
    p1.dar_aula()

    f1 = Funcionario('Claudia', 27, 'Secretária', 'Secretaria')
    f1.fazer_aniversario()
    f1.bater_ponto()

#Garante que, caso o arquivo seja importado, a main não será executada. 
if __name__ == "__main__":
    main()