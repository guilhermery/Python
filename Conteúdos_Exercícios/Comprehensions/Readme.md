# COMPREHENSIONS

## Sobre o conteúdo

Comprehensions são uma forma mais compacta e legível de criar coleções em Python.

Com elas é possível construir:
- listas
- dicionários
- conjuntos
- geradores (generators)

utilizando uma única expressão.

Esse recurso ajuda a reduzir a quantidade de código, tornando operações de transformação e filtragem de dados mais simples e organizadas.

Durante os exercícios deste conteúdo foram utilizados:
- List Comprehension
- Dictionary Comprehension
- Set Comprehension
- Generator Expression
- Operador condicional (`if` e `else`)
- Estruturas aninhadas
- Conversão entre coleções
- Iteração com `range()`

Esses exercícios ajudaram a compreender formas mais eficientes de criar e manipular estruturas de dados, além de apresentar conceitos importantes relacionados ao desempenho e ao consumo de memória.

---

# Índice

- [Exercício 001](#exercício-001)
- [Exercício 002](#exercício-002)
- [Exercício 003](#exercício-003)
- [Exercício 004](#exercício-004)

---

# Exercício 001

[Ver código](./Exercício001.py)

## Objetivo

Praticar diferentes tipos de comprehensions em Python.

## O que foi utilizado

- List Comprehension
- Dictionary Comprehension
- Set Comprehension
- Generator Expression
- Conversão para tupla

## Explicação

Foram criadas diversas estruturas utilizando comprehensions.

Lista de quadrados:

```python
quadrados = [x ** 2 for x in range(9)]
```

Lista de números pares:

```python
pares = [x for x in range(21) if x % 2 == 0]
```

Dicionário contendo números e seus quadrados:

```python
quadrados_dict = {x: x ** 2 for x in range(6)}
```

Conjunto de quadrados sem valores repetidos:

```python
quadrados_set = {x ** 2 for x in [1, 2, 2, 3, 3, 4, 5]}
```

Também foi utilizado um generator:

```python
gen = (x ** 2 for x in range(6))
```

e uma conversão para tupla:

```python
quadrados_tupla = tuple(x ** 2 for x in range(6))
```

Esse exercício ajudou na prática de:
- criação rápida de coleções
- eliminação de repetições
- compreensão de generators
- transformação de dados

---

# Exercício 002

[Ver código](./Exercício002.py)

## Objetivo

Utilizar operadores condicionais dentro de uma List Comprehension.

## O que foi utilizado

- List Comprehension
- Operador ternário (`if` e `else`)
- Estruturas condicionais

## Explicação

Foi criada uma lista classificando números de 1 a 10.

```python
lista = ['POSITIVO' if x > 5 else 'PEQUENO' for x in range(1, 11)]
```

Para cada valor:

- maior que 5 → `"POSITIVO"`
- menor ou igual a 5 → `"PEQUENO"`

Esse exercício ajudou na prática de:
- condições dentro de comprehensions
- operador ternário
- geração dinâmica de listas

---

# Exercício 003

[Ver código](./Exercício003.py)

## Objetivo

Criar matrizes utilizando comprehensions aninhadas.

## O que foi utilizado

- List Comprehension
- Comprehensions aninhadas
- Estruturas bidimensionais
- Laços de repetição

## Explicação

Foi criada uma matriz contendo coordenadas:

```python
matrizpares = [[(x, y) for y in range(3)] for x in range(3)]
```

Resultado:

```python
[
 [(0,0), (0,1), (0,2)],
 [(1,0), (1,1), (1,2)],
 [(2,0), (2,1), (2,2)]
]
```

Também foi criada uma matriz numérica:

```python
matriz = [[coluna + 1 for coluna in range(3)] for linha in range(3)]
```

Resultado:

```python
[
 [1, 2, 3],
 [1, 2, 3],
 [1, 2, 3]
]
```

Esse exercício ajudou no aprendizado de:
- matrizes em Python
- comprehensions aninhadas
- geração de estruturas bidimensionais
- organização de dados em linhas e colunas

---

# Exercício 004

[Ver código](./Exercício004.py)

## Objetivo

Demonstrar o funcionamento de um Generator Expression.

## O que foi utilizado

- Generator Expression
- Conversão para lista
- Iteração de valores

## Explicação

Foi criado um generator:

```python
gen = (x ** 2 for x in range(5))
```

Generators produzem valores sob demanda, consumindo menos memória do que listas.

Posteriormente os valores foram convertidos para uma lista:

```python
lista = list(gen)
```

Resultado:

```python
[0, 1, 4, 9, 16]
```

Esse exercício ajudou na compreensão de:
- geração preguiçosa de dados (lazy evaluation)
- economia de memória
- diferenças entre listas e generators
- conversão entre estruturas de dados 