sBruto = float(input('Digite o valor do salário bruto: '))
if sBruto <= 2259:
    print('O salário bruto é de R${:.2f}, o valor do imposto é 0, logo o salário líquido é de R${:.2f} '.format(
    sBruto, sBruto))
else:
    if sBruto <= 3751:
        imposto = sBruto * 0.075
        sLiquido = sBruto - imposto
        print('O salário bruto é de R${:.2f}, o valor do imposto é R${:.2f}, logo o salário líquido é de R${:.2f} '.format(
        sBruto, imposto, sLiquido))
    else:
        if sBruto <= 4664:
            imposto = sBruto * 0.15
            sLiquido = sBruto - imposto
            print('O salário bruto é de R${:.2f}, o valor do imposto é R${:.2f}, logo o salário líquido é de R${:.2f} '.format(
            sBruto, imposto, sLiquido))
        else:
            imposto = sBruto * 0.225
            sLiquido = sBruto - imposto
            print('O salário bruto é de R${:.2f}, o valor do imposto é R${:.2f}, logo o salário líquido é de R${:.2f} '.format(
            sBruto, imposto, sLiquido))