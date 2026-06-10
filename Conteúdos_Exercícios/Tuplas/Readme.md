# TUPLAS

## Sobre o conteúdo

Tuplas são estruturas de dados utilizadas para armazenar múltiplos valores em uma única variável.

Em Python, as tuplas são definidas utilizando parênteses:

```python
tupla = ('a', 'b', 'c')
```

A principal característica das tuplas é que elas são:
- imutáveis

Ou seja:
- seus valores não podem ser alterados após a criação

Durante os exercícios deste conteúdo foram utilizados:
- criação de tuplas
- fatiamento
- laços `for`
- funções como `len()`, `sorted()`, `max()` e `min()`
- métodos `.count()` e `.index()`
- `enumerate()`
- tuplas com diferentes tipos de dados

As tuplas são utilizadas para armazenar conjuntos de dados de forma organizada, com a diferença de que seus valores não podem ser alterados após a criação. São úteis quando as informações devem permanecer fixas durante a execução do programa.

---

# Índice

- [Exercicio001](#exercicio-001)
- [Exercício002](#exercício-002)
- [Exercício003](#exercício-003)
- [Exercício004](#exercício-004)
- [Exercício005](#exercício-005)
- [Exercício006](#exercício-006)
- [Exercício007](#exercício-007)

---

# Exercicio 001

[Ver código](./Exercicio001.py)

## Objetivo
Aprender operações básicas com tuplas.

## O que foi utilizado
- Criação de tuplas
- Índices
- Índices negativos
- Funções `len()` e `sorted()`
- Estrutura `for`

## Explicação
O programa cria uma tupla contendo alimentos:

```python
lanches = (
    'hamburguer',
    'suco',
    'pastel',
    'pudim'
)
```

Também foram utilizadas:
- índices negativos:
```python
lanches[-1]
```

- função:
```python
len(lanches)
```

para obter o tamanho da tupla

- função:
```python
sorted(lanches)
```

para exibir os elementos em ordem alfabética

Além disso, foi utilizado:
```python
for comida in lanches
```

para percorrer todos os elementos da tupla.

Esse exercício ajudou no aprendizado de:
- acesso a elementos
- percorrer tuplas
- funções básicas relacionadas a tuplas

---

# Exercício 002

[Ver código](./Exercício002.py)

## Objetivo
Mostrar o número por extenso utilizando tuplas.

## O que foi utilizado
- Tuplas
- Estrutura `while`
- Índices

## Explicação
O programa armazena os números por extenso dentro de uma tupla:

```python
numeros = ('zero', 'um', 'dois', ...)
```

Depois solicita um número entre:
- 0
- 20

e utiliza o índice informado para acessar o valor correspondente:

```python
numeros[n]
```

Esse exercício ajudou no aprendizado de:
- associação entre índices e valores
- utilização prática de tuplas
- validação de entrada

---

# Exercício 003

[Ver código](./Exercício003.py)

## Objetivo
Manipular informações de uma tabela de times.

## O que foi utilizado
- Tuplas
- Fatiamento
- Função `sorted()`
- Estrutura `for`

## Explicação
O programa utiliza uma tupla contendo nomes de times.

Foram utilizados:
- fatiamentos:
```python
times[:5]
```

e:
```python
times[16:]
```

para mostrar partes específicas da tupla.

Também foi utilizada:
```python
sorted(times)
```

para ordenar os times alfabeticamente.

Além disso, um laço `for` percorre a tupla para localizar a posição da Chapecoense.

Esse exercício ajudou no aprendizado de:
- fatiamento
- busca de elementos
- ordenação de dados

---

# Exercício 004

[Ver código](./Exercício004.py)

## Objetivo
Gerar números aleatórios e identificar o maior e o menor.

## O que foi utilizado
- Biblioteca `random`
- Tuplas
- Funções `max()` e `min()`

## Explicação
O programa cria uma tupla com números aleatórios:

```python
random.randint(1,100)
```

Depois utiliza:
```python
max(numeros)
```

e:
```python
min(numeros)
```

para identificar:
- maior valor
- menor valor

Esse exercício ajudou no aprendizado de:
- geração de números aleatórios
- análise de valores
- utilização de funções matemáticas

---

# Exercício 005

[Ver código](./Exercício005.py)

## Objetivo
Analisar números digitados pelo usuário.

## O que foi utilizado
- Tuplas
- Métodos `.count()` e `.index()`
- Estrutura `for`

## Explicação
O programa solicita quatro números e os armazena em uma tupla.

Depois:
- conta quantas vezes o número 9 apareceu:
```python
num.count(9)
```

- verifica a posição do número 3:
```python
num.index(3)
```

Também percorre os números para identificar os valores pares.

Esse exercício ajudou no aprendizado de:
- métodos específicos de tuplas
- análise de dados
- percorrer elementos

---

# Exercício 006

[Ver código](./Exercício006.py)

## Objetivo
Criar uma listagem de preços formatada.

## O que foi utilizado
- Tuplas
- Estrutura `for`
- Formatação de strings

## Explicação
O programa utiliza uma tupla contendo:
- nomes de produtos
- preços

Os elementos foram organizados alternando:
- produto
- valor

Foi utilizado:
```python
if pos % 2 == 0
```

para identificar:
- posições de produtos
- posições de preços

Também foi utilizada formatação:

```python
{:<30}
```

e:
```python
{:>6.2f}
```

para alinhar os textos e valores.

Esse exercício ajudou no aprendizado de:
- manipulação de posições
- formatação avançada
- organização visual de dados

---

# Exercício 007

[Ver código](./Exercício007.py)

## Objetivo
Identificar vogais dentro de palavras.

## O que foi utilizado
- Tuplas
- Estruturas `for`
- Método `.lower()`

## Explicação
O programa percorre uma tupla contendo palavras e identifica as vogais presentes em cada uma.

Foi utilizada:
```python
letra.lower()
```

para transformar letras em minúsculas antes da comparação.

Depois verifica:
```python
if letra.lower() in vogais
```

para identificar vogais.

Esse exercício ajudou no aprendizado de:
- laços aninhados
- manipulação de caracteres
- comparação de strings
- análise de palavras