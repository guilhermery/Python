import uteis
from rich import print
from rich.panel import Panel

def main():
    while True:
        print("Olá. Tudo bem? O que deseja?")
        print("\n")
        print(Panel("1 - Cadastrar Produto\n2 - Listar Produtos\n3 - Buscar Produtos\n4 - Atualizar Preço\n5 - Sair", title="Opções", width=40))
        print("\n")
        escolha = input("Opção: ")
        
        if escolha == "5":
            print("Encerrando o sistema...")
            break
        
        elif escolha == "1":
            nome = input("Nome do produto: ")
            try:
                preco = float(input("Preço: "))
                estoque = int(input("Estoque: "))
            except:
                print("Digite valores númericos válidos!")
                print("\n")
                continue
            uteis.cadastrar_produto(nome, preco, estoque)
            print(f"Produto [blue]{nome}[/] cadastrado com [green]sucesso[/]!!")
            print("\n")
        
        elif escolha == "2":
            uteis.listar_produtos()
            print("\n")
        
        elif escolha == "3":
            nome = input("Nome do produto: ")
            uteis.buscar_produtos(nome)
            print("\n")
        
        elif escolha == "4":
            nome = input("Nome do produto: ")
            try:
                preco = float(input("Preço atualizado: "))
            except:
                print("Digite valores númericos válidos!")
                print("\n")
                continue
            uteis.atualizar_preco(nome, preco)
            print("Preço atualizado com [green]sucesso[/]!")
            print("\n")

        else:
            print("Escolha uma opção válida.")
            print("\n")

    

if __name__ == "__main__":
    main()