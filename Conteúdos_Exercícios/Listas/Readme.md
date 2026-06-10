# LISTAS

## Sobre o conteúdo

Listas são estruturas de dados utilizadas para armazenar múltiplos valores em uma única variável.

Em Python, listas são definidas utilizando colchetes:

```python
lista = [1, 2, 3]
```

Diferente das tuplas, listas são:
- mutáveis

Ou seja:
- podem ser alteradas durante a execução do programa

Durante os exercícios deste conteúdo foram utilizados:
- criação de listas
- métodos como `append()`, `insert()`, `remove()` e `pop()`
- ordenação com `sort()`
- listas compostas
- listas aninhadas
- matrizes
- validação de dados
- estruturas de repetição
- manipulação de posições
- cópias de listas

As listas são uma das estruturas mais importantes do Python, já que facilitam o armazenamento e manipulação de vários dados em uma única variável. Grande parte da programação acaba envolvendo coleções de informações de algum jeito.

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

---

# Exercício 001

[Ver código](./Exercício001.py)

## Objetivo
Aprender operações básicas com listas.

## O que foi utilizado
- Métodos de listas
- Estrutura `for`
- `enumerate()`

## Explicação
O programa realizou diversas operações com listas:
- alteração de valores:
```python
num[2] = 6
```

- adição de elementos:
```python
num.append(7)
```

- inserção em posição específica:
```python
num.insert(2, 0)
```

- remoção de elementos:
```python
num.pop(2)
```

Também foram utilizadas:
```python
sort()
```

e:
```python
sort(reverse=True)
```

para ordenação crescente e decrescente.

Além disso:
```python
enumerate(num)
```

foi utilizado para acessar:
- posição
- valor

Esse exercício ajudou no aprendizado das principais operações com listas.

---

# Exercício 002

[Ver código](./Exercício002.py)

## Objetivo
Identificar maior e menor valor de uma lista.

## O que foi utilizado
- Listas
- `append()`
- `max()`
- `min()`
- `enumerate()`

## Explicação
O programa solicita cinco valores e os armazena em uma lista.

Depois utiliza:
```python
max(num)
```

e:
```python
min(num)
```

para identificar:
- maior valor
- menor valor

Também utiliza:
```python
enumerate()
```

para mostrar as posições dos valores encontrados.

Esse exercício ajudou no aprendizado de:
- análise de listas
- busca de valores
- percorrer elementos com índice

---

# Exercício 003

[Ver código](./Exercício003.py)

## Objetivo
Criar uma lista sem valores duplicados.

## O que foi utilizado
- Listas
- Estrutura `while`
- Operador `not in`

## Explicação
O programa solicita números ao usuário e verifica:

```python
if valor not in num
```

para impedir valores repetidos.

Caso o número não exista:
- ele é adicionado na lista

Depois a lista é ordenada com:
```python
num.sort()
```

Esse exercício ajudou no aprendizado de:
- validação de dados
- prevenção de duplicidade
- manipulação de listas dinâmicas

---

# Exercício 004

[Ver código](./Exercício004.py)

## Objetivo
Inserir valores já em ordem crescente.

## O que foi utilizado
- Listas
- `insert()`
- Estrutura `while`

## Explicação
O programa insere cada número diretamente na posição correta da lista.

Foi utilizada:
```python
numeros.insert(pos, n)
```

para inserir o valor na posição adequada.

Esse exercício ajudou no aprendizado de:
- ordenação manual
- manipulação de índices
- lógica de inserção ordenada

Foi um exercício importante para desenvolver raciocínio algorítmico.

---

# Exercício 005

[Ver código](./Exercício005.py)

## Objetivo
Analisar números digitados pelo usuário.

## O que foi utilizado
- Listas
- `sort()`
- Operador `in`

## Explicação
O programa:
- conta quantos números foram digitados
- mostra a lista em ordem decrescente
- verifica se o número 5 foi informado

Foi utilizada:
```python
num.sort(reverse=True)
```

para ordenar a lista em ordem decrescente.

Esse exercício ajudou no aprendizado de:
- ordenação
- busca em listas
- análise de dados

---

# Exercício 006

[Ver código](./Exercício006.py)

## Objetivo
Separar números pares e ímpares em listas diferentes.

## O que foi utilizado
- Listas
- Estruturas condicionais
- Operador módulo `%`

## Explicação
O programa armazena todos os números em uma lista principal.

Depois percorre a lista e separa:
- números pares
- números ímpares

utilizando:
```python
c % 2 == 0
```

Esse exercício ajudou no aprendizado de:
- filtragem de dados
- múltiplas listas
- classificação de valores

---

# Exercício 007

[Ver código](./Exercício007.py)

## Objetivo
Validar expressões matemáticas utilizando pilha.

## O que foi utilizado
- Listas como pilha
- `append()`
- `pop()`
- Estrutura `for`

## Explicação
O programa verifica se os parênteses da expressão estão corretos.

Funcionamento:
- ao encontrar `(` → adiciona na pilha
- ao encontrar `)` → remove um elemento da pilha

Caso a pilha fique inconsistente:
- a expressão é inválida

Esse exercício ajudou no aprendizado de:
- estrutura de pilha
- validação sintática
- controle lógico com listas

Foi um dos exercícios mais importantes do conteúdo por introduzir um conceito muito utilizado em compiladores e interpretadores.

---

# Exercício 008

[Ver código](./Exercício008.py)

## Objetivo
Trabalhar com listas compostas.

## O que foi utilizado
- Listas dentro de listas
- Cópias com `[:]`
- `clear()`

## Explicação
O programa cria listas compostas para armazenar:
- nome
- idade

Foi utilizada:
```python
pessoal.append(dado[:])
```

para criar uma cópia da lista atual.

Também foi utilizado:
```python
dado.clear()
```

para limpar a lista temporária após a cópia.

Esse exercício ajudou no aprendizado de:
- listas aninhadas
- cópia de listas
- referência de memória

---

# Exercício 009

[Ver código](./Exercício009.py)

## Objetivo
Cadastrar pessoas e analisar pesos.

## O que foi utilizado
- Listas compostas
- Estruturas condicionais
- Busca de maior e menor valor

## Explicação
O programa armazena:
- nome
- peso

Depois identifica:
- maior peso
- menor peso
- pessoas correspondentes

Esse exercício ajudou no aprendizado de:
- análise de dados
- listas compostas
- comparação de valores

---

# Exercício 010

[Ver código](./Exercício010.py)

## Objetivo
Separar números pares e ímpares em listas internas.

## O que foi utilizado
- Listas aninhadas
- Operador módulo `%`
- `sort()`

## Explicação
O programa utiliza:
```python
numeros = [[], []]
```

para armazenar:
- pares
- ímpares

Depois ordena ambas as listas.

Esse exercício ajudou no aprendizado de:
- listas multidimensionais
- organização de dados
- separação lógica de informações

---

# Exercício 011

[Ver código](./Exercício011.py)

## Objetivo
Criar e analisar uma matriz 3x3.

## O que foi utilizado
- Matrizes
- Listas aninhadas
- Estruturas `for`
- Operações matemáticas

## Explicação
O programa cria uma matriz 3x3 utilizando listas dentro de listas.

Depois realiza:
- soma dos valores pares
- soma da terceira coluna
- busca do maior valor da segunda linha

Esse exercício ajudou no aprendizado de:
- matrizes
- acesso bidimensional
- análise matemática de estruturas

Foi um exercício importante para compreender estruturas mais avançadas.

---

# Exercício 012

[Ver código](./Exercício012.py)

## Objetivo
Gerar jogos aleatórios da Mega Sena.

## O que foi utilizado
- Biblioteca `random`
- Listas compostas
- Estruturas `for`

## Explicação
O programa gera vários jogos contendo números aleatórios.

Foi utilizada:
```python
random.randint(1, 60)
```

para gerar os números.

Cada jogo é armazenado em uma lista, e depois adicionado na lista principal:

```python
totjogos.append(jogo[:])
```

Esse exercício ajudou no aprendizado de:
- geração aleatória
- listas compostas
- armazenamento de múltiplos conjuntos de dados

Também serviu como prática de estruturas mais complexas utilizando listas.