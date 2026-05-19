frase = 'Curso em Vídeo Python'
print(frase[:13]) #Dá print do início até o 12 (o 13 nao pega).
print(frase[3:]) #Dá print do 3 até o final da string.
print(frase[2:15:2]) #vai mostrando do 2 até o 15 pulando de 2 em 2.
print(frase[::2]) #Mostra tudo desde o início ao fim pulando de 2 em 2.
print(frase.count('o'))
print(frase.upper().count('O')) #Transformei tudo em letra maiuscula e contei quantos O maiusculo tem
print(len(frase)) #Conta quantos caracteres tem.
print(frase.replace('Python', 'Android')) #Replace troca a frase python para android.
print('Vídeo' in frase) #retorna boolean, verdadeiro ou falso.
print(frase.find('Curso')) #retorna o primeiro número dessa palavra vídeo.
dividido = frase.split() #Atribui uma lista das palavras da frase a variavel dividido.
print(dividido[0][2]) #Pega a palavra curso e mostra o terceiro caractere.


