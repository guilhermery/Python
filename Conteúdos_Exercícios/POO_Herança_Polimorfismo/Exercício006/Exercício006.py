from classes import ContaBancaria
#Atributos de visibilidade pública pode ser acessada na classe raiz, filhas e main +
#Atributos de visibilidade protegida só pode ser acessada pela classe raiz e filhas #
#Atributos de visibilidade privada só pode ser acessada pela classe raiz -

def main():
    c1 = ContaBancaria(111, "Maria", 5000)
    c1.depositar(-500)
    c1.sacar(-100)
    c1.saldo = 0 #Cria um novo atributo/variavel saldo, mas não altera o original pois é privado

    print(c1)

if __name__ == "__main__":
    main()