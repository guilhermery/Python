from rich import print
from rich.panel import Panel
import os

class ControleRemoto:
    canais = [1, 2, 3, 4, 5]
    volume = [1, 2, 3, 4, 5]
    def __init__(self):
        self.ligado = False
        self.volume = 1
        self.canal = 1

    def mudar_canal(self, escolha):
        if self.ligado:
            if escolha == '<':
                if self.canal == 1:
                    self.canal = 5
                else:
                    self.canal -= 1
            elif escolha == '>':
                if self.canal == 5:
                    self.canal = 1
                else:
                    self.canal += 1
        
    
    def mudar_volume(self, escolha):
        if self.ligado:
            if escolha == '+':
                if self.volume < 5:
                    self.volume += 1
            elif escolha == '-':
                if self.volume > 1:
                    self.volume -= 1
    
    def ligar_desligar(self):
        self.ligado = not self.ligado

    def apresentar_tv(self):
        os.system("cls") #Limpa o terminal a cada apresentação
        if self.ligado:
            conteudo = "CANAL = "
            for i in range(1, 6):
                if i == self.canal:
                    conteudo += f'[white on yellow]{i}[/] '
                else:
                    conteudo += f'[bold]{i}[/] '
            conteudo += '\nVOLUME = '
            for i in range(1, 6):
                if i <= self.volume:
                    conteudo += f'[black on blue] [/]'
                else:
                    conteudo += f'[black on grey30] [/]'
        else:
            conteudo = ":no_entry_sign:  [red]A TV está desligada[/]"
        print(Panel(conteudo, title='[ TV ]', width=40))
            
    def iniciar_programa(self):
        while True:
            self.apresentar_tv()
            escolha = input(f'< CH1 >  - VOL{self.volume} + ').strip()
            if escolha == '0':
                break
            elif escolha == "@":
                self.ligar_desligar()
            elif escolha in "<>":
                self.mudar_canal(escolha)
            elif escolha in "+-":
                self.mudar_volume(escolha)


controle = ControleRemoto()
controle.iniciar_programa()