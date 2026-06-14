from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

class Funcionario(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.sal_bruto = 0
        self.salario = 0
        self.sal_min = 1612
        self.inss = 7.5
    
    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        conteudo = f"O salário de [blue]{self.nome}[/] ([purple]{type(self).__name__}[/]) é de [green]R${self.salario:.2f}[/] e corresponde a [yellow]{self.salario/self.sal_min:.1f} salários minimos[/]."
        print(Panel(conteudo, title="Análise de Salário", width=55))

class FuncionarioHorista(Funcionario):
    def __init__(self, nome, valor_hora, qtd_horas):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.qtd_horas = qtd_horas

    def calc_sal(self):
        self.sal_bruto = self.valor_hora*self.qtd_horas
        self.salario = self.sal_bruto - self.sal_bruto*(self.inss/100)
        return self.salario

class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, salario_bruto):
        super().__init__(nome)
        self.sal_bruto = salario_bruto

    def calc_sal(self):
        self.salario = self.sal_bruto - self.sal_bruto*(self.inss/100)

f1 = FuncionarioHorista("Paulo", 12, 200)
f1.calc_sal()
f1.analisar_sal()

f2 = FuncionarioMensalista("Maria", 9500)
f2.calc_sal()
f2.analisar_sal()