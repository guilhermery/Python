a = float(input("Informe o valor do coeficiente a: "))
b = float(input("Informe o valor do coeficiente b: "))
c = float(input("Informe o valor do coeficiente c: "))
delta = b**2 - (4*a*c)
if a == 0:
    print("É impossível realizar essa operação")
elif delta < 0:
    print("É impossível realizar essa operação")
else:
    x1 = (-b + (delta**0.5))/(2*a)
    x2 = (-b - (delta**0.5))/(2*a)
    print(f"O valor de x1 é igual a {x1} e o valor de x2 é igual a {x2}")
    if delta == 0:
        print("As raízes são reais e iguais")
    else:
        print("As raízes são reais e diferentes de zero")