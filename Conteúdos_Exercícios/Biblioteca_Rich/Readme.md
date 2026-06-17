# BIBLIOTECA RICH

## Sobre o conteúdo

A biblioteca Rich é utilizada para criar saídas mais bonitas e organizadas no terminal.

Ela permite adicionar:
- cores
- estilos de texto
- emojis
- tabelas
- painéis
- barras de progresso
- inspeção de objetos
- mensagens de erro aprimoradas

Tudo isso sem precisar utilizar códigos ANSI manualmente.

Durante os exercícios deste conteúdo foram utilizados:
- `print()` da biblioteca Rich
- Emojis
- Painéis (`Panel`)
- Tabelas (`Table`)
- Inspeção de objetos (`inspect`)
- Tratamento visual de erros (`traceback`)
- Classes e objetos

Esses exercícios ajudaram a compreender como melhorar a experiência visual de aplicações executadas no terminal, tornando as informações mais organizadas, legíveis e profissionais.

---

# Índice

- [Exercício 001](#exercício-001)
- [Exercício 002](#exercício-002)
- [Exercício 003](#exercício-003)
- [Exercício 004](#exercício-004)
- [Exercício 005](#exercício-005)

---

# Exercício 001

[Ver código](./Exercício001.py)

## Objetivo

Exibir textos coloridos e emojis utilizando a biblioteca Rich.

## O que foi utilizado

- `rich.print`
- Tags de estilização
- Emojis

## Explicação

Foi utilizado o método:

```python
from rich import print
```

para substituir o `print()` padrão do Python.

Exemplos:

```python
print('Olá, [red]Mundo[/]!')
```

```python
print('Olá, [bold blue on white]Guilherme[/]')
```

Também foram utilizados emojis:

```python
:earth_americas:
:+1:
```

Esse exercício ajudou no aprendizado de:

- estilização de textos
- utilização de emojis
- formatação visual no terminal

---

# Exercício 002

[Ver código](./Exercício002.py)

## Objetivo

Criar caixas de informação utilizando painéis.

## O que foi utilizado

- `Panel`
- Estilização visual
- Títulos personalizados

## Explicação

Foi criado um painel utilizando:

```python
from rich.panel import Panel
```

Exemplo:

```python
caixa = Panel(
    "[white]Esse é um painel de exemplo[/]",
    title='Mensagem',
    style='Red'
)
```

O painel organiza informações dentro de uma caixa estilizada no terminal.

Esse exercício ajudou no aprendizado de:

- exibição organizada de informações
- personalização visual
- utilização de componentes da biblioteca Rich

---

# Exercício 003

[Ver código](./Exercício003.py)

## Objetivo

Criar tabelas formatadas no terminal.

## O que foi utilizado

- `Table`
- Colunas
- Linhas
- Alinhamento de texto

## Explicação

Foi criada uma tabela de preços utilizando:

```python
from rich.table import Table
```

Adicionando colunas:

```python
tabela.add_column('Nome')
tabela.add_column('Preço')
```

E linhas:

```python
tabela.add_row("Lapis", "R$1,50")
```

O resultado é uma tabela organizada e muito mais legível do que uma simples sequência de prints.

Esse exercício ajudou na prática de:

- exibição tabular de dados
- organização visual
- construção de interfaces simples para terminal

---

# Exercício 004

[Ver código](./Exercício004.py)

## Objetivo

Utilizar o recurso de inspeção de objetos da biblioteca Rich.

## O que foi utilizado

- Classes
- Objetos
- Métodos
- `inspect`
- Método especial `__str__`

## Explicação

Foi criada uma classe chamada:

```python
class ContaBancaria:
```

com métodos para:

- depósito
- saque
- exibição de saldo

Também foi implementado:

```python
def __str__(self):
```

para personalizar a exibição do objeto.

Em seguida foi utilizado:

```python
inspect(c1)
```

para visualizar informações detalhadas do objeto.

E:

```python
inspect(ContaBancaria, all=True)
```

para exibir todos os detalhes da classe.

Esse exercício ajudou no aprendizado de:

- Programação Orientada a Objetos
- inspeção de classes
- análise de atributos e métodos
- depuração de código

---

# Exercício 005

[Ver código](./Exercício005.py)

## Objetivo

Melhorar a visualização de erros no terminal.

## O que foi utilizado

- `rich.traceback`
- Exceções
- Tratamento visual de erros

## Explicação

Foi utilizado:

```python
from rich.traceback import install
install()
```

Esse recurso substitui o traceback padrão do Python por uma versão mais organizada e fácil de entender.

O erro foi gerado propositalmente:

```python
return x / y
```

com:

```python
print(divisao(50, 0))
```

resultando em uma divisão por zero.

A biblioteca Rich destaca visualmente:
- o local do erro
- a linha problemática
- a pilha de execução

Esse exercício ajudou na prática de:

- depuração de programas
- identificação de erros
- utilização de ferramentas profissionais para desenvolvimento