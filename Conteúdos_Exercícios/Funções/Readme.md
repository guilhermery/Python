# FUNÇÕES

## Sobre o conteúdo

Funções são blocos de código reutilizáveis criados para executar tarefas específicas.

Em Python, funções são definidas utilizando:

```python
def nome():
```

Elas ajudam a:
- organizar o código
- evitar repetição
- facilitar manutenção
- melhorar legibilidade

Durante os exercícios deste conteúdo foram utilizados:
- criação de funções
- parâmetros
- retorno com `return`
- parâmetros opcionais
- empacotamento com `*args`
- escopo de variáveis
- docstrings
- funções com listas
- funções com dicionários
- funções booleanas

As funções são fundamentais na programação, pois permitem reutilizar código, organizar melhor os programas e evitar repetições desnecessárias. Além disso, ajudam na manutenção e tornam o código mais limpo, modular e fácil de entender.

---

# Índice

- [Exercício001](#exercício-001)
- [Exercício002](#exercício-002)
- [Exercício003](#exercício-003)
- [Exercício004](#exercício-004)
- [Exercício005](#exercício-005)
- [Exercício006](#exercício-006)
- [Exercício007](#exercício-007)
- [Exercício008](#exercício-008)
- [Exercício009](#exercício-009)
- [Exercício010](#exercício-010)
- [Exercício011](#exercício-011)
- [Exercício012](#exercício-012)
- [Exercício013](#exercício-013)
- [Exercício014](#exercício-014)
- [Exercício015](#exercício-015)

---

# Exercício 001

[Ver código](./Exercício001.py)

## Objetivo
Aprender conceitos básicos sobre funções.

## O que foi utilizado
- Criação de funções
- Parâmetros
- `*args`
- Listas
- Escopo local

## Explicação
O exercício apresentou várias funções diferentes:
- `mensagem()`
- `soma()`
- `contador()`
- `dobra()`

Foi utilizado:
```python
def soma(a, b):
```

para criar funções com parâmetros.

Também foi utilizado:
```python
*num
```

para empacotar vários valores em uma tupla.

A função:
```python
dobra(lista)
```

modifica diretamente os elementos da lista recebida.

Esse exercício ajudou no aprendizado de:
- estrutura básica de funções
- passagem de parâmetros
- manipulação de listas dentro de funções

---

# Exercício 002

[Ver código](./Exercício002.py)

## Objetivo
Calcular a área de um terreno utilizando função.

## O que foi utilizado
- Funções
- Parâmetros
- Operações matemáticas

## Explicação
A função:
```python
def área(largura, comprimento):
```

recebe:
- largura
- comprimento

Depois calcula:
```python
area = largura * comprimento
```

Esse exercício ajudou no aprendizado de:
- reutilização de cálculos
- separação de responsabilidades
- funções matemáticas simples

---

# Exercício 003

[Ver código](./Exercício003.py)

## Objetivo
Criar textos personalizados dinamicamente.

## O que foi utilizado
- Funções
- `len()`
- Multiplicação de strings

## Explicação
O programa cria molduras automáticas ao redor das mensagens.

Foi utilizado:
```python
len(msg)
```

para calcular o tamanho do texto.

Depois:
```python
'-' * (tamanho + 2)
```

gera linhas proporcionais ao tamanho da frase.

Esse exercício ajudou no aprendizado de:
- personalização dinâmica
- manipulação de strings
- funções reutilizáveis

---

# Exercício 004

[Ver código](./Exercício004.py)

## Objetivo
Criar um sistema de contagem personalizado.

## O que foi utilizado
- Funções
- Estrutura `for`
- Biblioteca `time`
- Validação de dados

## Explicação
A função:
```python
contador(inicio, fim, passo)
```

realiza contagens:
- crescentes
- decrescentes

Foi utilizado:
```python
time.sleep(0.5)
```

para criar pausas entre os números.

Também houve validação para:
- passo zero
- passo negativo

Esse exercício ajudou no aprendizado de:
- controle de contagens
- funções mais completas
- validação de parâmetros

---

# Exercício 005

[Ver código](./Exercício005.py)

## Objetivo
Identificar o maior valor entre vários números.

## O que foi utilizado
- `*args`
- `len()`
- Estrutura `for`

## Explicação
A função:
```python
def maior(*num):
```

recebe vários números de quantidade indefinida.

Foi utilizado:
```python
len(num)
```

para descobrir quantos valores foram informados.

Depois o programa percorre os números para identificar o maior valor.

Esse exercício ajudou no aprendizado de:
- empacotamento de parâmetros
- análise de dados
- funções flexíveis

---

# Exercício 006

[Ver código](./Exercício006.py)

## Objetivo
Sortear números e somar os pares.

## O que foi utilizado
- Funções
- Biblioteca `random`
- Listas
- Operador módulo `%`

## Explicação
A função:
```python
sorteia()
```

gera números aleatórios.

Depois:
```python
somaPar()
```

analisa a lista e soma apenas os valores pares.

Esse exercício ajudou no aprendizado de:
- integração entre funções
- listas em funções
- filtragem de dados

---

# Exercício 007

[Ver código](./Exercício007.py)

## Objetivo
Aprender docstrings e parâmetros opcionais.

## O que foi utilizado
- Docstrings
- Parâmetros opcionais
- `help()`

## Explicação
O programa utiliza:
```python
"""
"""
```

para criar documentação interna da função.

Também foram utilizados parâmetros opcionais:

```python
def contador(i=0, f=0, p=1):
```

Isso permite chamar a função mesmo sem informar todos os valores.

Foi utilizado:
```python
help(contador)
```

para exibir automaticamente a documentação da função.

Esse exercício ajudou no aprendizado de:
- documentação de código
- criação de funções mais flexíveis
- boas práticas de programação

---

# Exercício 008

[Ver código](./Exercício008.py)

## Objetivo
Entender escopo local e global.

## O que foi utilizado
- Variáveis globais
- Variáveis locais
- Palavra-chave `global`

## Explicação
O programa demonstra diferença entre:
- escopo local
- escopo global

Foi utilizado:
```python
global a
```

para permitir que a função modifique a variável global.

Esse exercício ajudou no aprendizado de:
- funcionamento da memória
- escopo de variáveis
- comportamento interno das funções

Foi um conteúdo importante porque erros de escopo conseguem destruir a sanidade de muita gente em projetos grandes.

---

# Exercício 009

[Ver código](./Exercício009.py)

## Objetivo
Criar funções com retorno.

## O que foi utilizado
- `return`
- Funções booleanas
- Estruturas condicionais

## Explicação
A função:
```python
fatorial()
```

retorna o resultado do cálculo.

Já a função:
```python
par()
```

retorna:
- `True`
- ou `False`

dependendo do número informado.

Esse exercício ajudou no aprendizado de:
- retorno de valores
- funções booleanas
- reutilização de resultados

---

# Exercício 010

[Ver código](./Exercício010.py)

## Objetivo
Verificar situação eleitoral de uma pessoa.

## O que foi utilizado
- Funções
- `return`
- Estruturas condicionais

## Explicação
A função calcula a idade da pessoa e retorna:
- NÃO VOTA
- VOTO OPCIONAL
- VOTO OBRIGATÓRIO

Esse exercício ajudou no aprendizado de:
- retorno literal
- regras condicionais
- funções de validação

---

# Exercício 011

[Ver código](./Exercício011.py)

## Objetivo
Exibir cálculo fatorial opcionalmente detalhado.

## O que foi utilizado
- Parâmetros opcionais
- Estrutura `for`
- `return`

## Explicação
Foi utilizado:
```python
show=False
```

para decidir se o cálculo será exibido passo a passo.

Quando:
```python
show=True
```

o programa mostra toda a multiplicação do fatorial.

Esse exercício ajudou no aprendizado de:
- parâmetros booleanos
- funções configuráveis
- controle de exibição

---

# Exercício 012

[Ver código](./Exercício012.py)

## Objetivo
Cadastrar informações de jogador utilizando parâmetros opcionais.

## O que foi utilizado
- Parâmetros opcionais
- Condicionais
- Conversão de tipos

## Explicação
A função:
```python
ficha()
```

possui valores padrão para:
- nome
- gols

Isso evita erros caso o usuário não informe dados.

Esse exercício ajudou no aprendizado de:
- tratamento de ausência de dados
- parâmetros padrão
- validação de entrada

---

# Exercício 013

[Ver código](./Exercício013.py)

## Objetivo
Validar números inteiros utilizando função.

## O que foi utilizado
- Funções
- Estrutura `while`
- Método `.isdigit()`

## Explicação
O programa solicita um número até que o usuário informe um valor inteiro válido.

Foi utilizado:
```python
num.isdigit()
```

para validar se a entrada contém apenas números.

Esse exercício ajudou no aprendizado de:
- validação de entradas
- reutilização de funções
- tratamento de dados

---

# Exercício 014

[Ver código](./Exercício014.py)

## Objetivo
Analisar notas utilizando dicionários.

## O que foi utilizado
- `*args`
- Dicionários
- `return`
- Estruturas condicionais

## Explicação
A função recebe várias notas e retorna um dicionário contendo:
- total
- maior nota
- menor nota
- média
- situação

Foi utilizado:
```python
notasAlunos = dict()
```

para organizar as informações.

Esse exercício ajudou no aprendizado de:
- funções avançadas
- retorno estruturado
- análise de dados

Foi um exercício bastante completo por unir funções e dicionários.

---

# Exercício 015

[Ver código](./Exercício015.py)

## Objetivo
Criar um mini sistema de ajuda interativo.

## O que foi utilizado
- Funções
- `help()`
- Entrada de dados

## Explicação
O programa solicita uma função ou biblioteca e exibe automaticamente sua documentação utilizando:

```python
help(funcao)
```

Esse exercício ajudou no aprendizado de:
- introspecção em Python
- documentação interna
- criação de sistemas interativos

Também mostrou como Python possui ferramentas próprias para consulta de documentação diretamente pelo terminal.