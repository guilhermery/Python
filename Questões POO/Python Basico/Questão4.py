nome = input("Informe o nome do produto: ")
quant = int(input("Informe a quantidade do produto: "))
preco = float(input("Informe o preço unitário do produto: "))
total = quant*preco
if quant <= 5:
    desconto = (total*2)/100
    total = total - desconto
elif quant <= 10:
    desconto = (total*3)/100
    total = total - desconto
else: 
    desconto = (total*5)/100
    total = total - desconto
print(f"O valor a ser pago por {quant} {nome} é de R${total}")