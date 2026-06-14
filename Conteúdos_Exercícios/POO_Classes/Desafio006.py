from rich import print

class Caneta:
    cores = {"azul": "blue", "vermelho": "red", "verde": "green"}
    def __init__(self, cor):
        self.tampada = True
        #Para garantir que, ao digitar uma cor que não existe, por padrão será branco
        #Para garantir que seja uma string ao transformar em lower, utiliza a função str
        self.cor = self.cores.get(str(cor).lower(), "white")

    def destampar(self):
        self.tampada = False

    def escrever(self, mensagem):
        if self.tampada == True:
            print(f":no_entry_sign:  A [{self.cor}]caneta[/] está tampada!")
        else: 
            print(f"[{self.cor}]{mensagem}[/]", end='')
    
    def quebrar_linha(self, linhas):
        print("\n"*linhas)

c1 = Caneta("azul")
c2 = Caneta("vermelho")
c3 = Caneta("verde")

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá, tudo bem? ")
c1.quebrar_linha(2)
c2.escrever("Olá, Guilherme! ")
c3.escrever("Vamos exercitar!")