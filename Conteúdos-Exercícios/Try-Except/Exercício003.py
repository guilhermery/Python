import urllib.request

try:
    site = urllib.request.urlopen('https://www.instagram.com/')
except:
    print('O site Instagram não está acessível no momento.')
else:
    print('Consegui acessar o site Instagram com sucesso!')