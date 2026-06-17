# LAMBDA E YIELD

## Sobre o conteúdo

Lambda e Yield são recursos do Python utilizados para tornar o código mais flexível e eficiente.

As funções `lambda` permitem criar funções anônimas de forma rápida e compacta, sendo muito utilizadas em conjunto com funções como:
- `map()`
- `filter()`
- `sorted()`

Já o `yield` é utilizado para criar geradores (generators), permitindo produzir valores sob demanda sem armazenar todos eles na memória ao mesmo tempo.

Durante os exercícios deste conteúdo foram utilizados:
- Funções Lambda
- Funções anônimas
- `map()`
- `filter()`
- `yield`
- Geradores (Generators)
- Iteradores
- Laços de repetição
- Manipulação de listas

Esses exercícios ajudaram a compreender formas mais modernas de manipular dados, além de introduzir conceitos importantes relacionados à programação funcional e otimização de memória.

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

Criar e utilizar uma função anônima com `lambda`.

## O que foi utilizado

- Função `lambda`
- Parâmetros
- Operações matemáticas

## Explicação

Foi criada uma função anônima responsável por calcular o dobro de um número:

```python
dobro = lambda x: x * 2
```

Essa expressão funciona de forma semelhante a:

```python
def dobro(x):
    return x * 2
```

Depois a função foi utilizada para calcular o dobro de um valor:

```python
print(f'O dobro de 5 é: {dobro(5)}')
```

Esse exercício ajudou na prática de:

- criação de funções anônimas
- sintaxe da palavra-chave `lambda`
- operações matemáticas simples
- programação funcional básica

---

# Exercício 002

[Ver código](./Exercício002.py)

## Objetivo

Utilizar funções lambda em conjunto com `map()` e `filter()`.

## O que foi utilizado

- Funções Lambda
- `map()`
- `filter()`
- List Comprehension
- Manipulação de listas

## Explicação

Primeiramente foi criada uma lista de números:

```python
numeros = [x for x in range(1, 6)]
```

Em seguida foi utilizado:

```python
quadrados = list(map(lambda x: x ** 2, numeros))
```

A função `map()` aplica a função lambda a cada elemento da lista, gerando os quadrados dos números.

Depois foi utilizado:

```python
quadrados_pares = list(filter(lambda x: x % 2 == 0, quadrados))
```

A função `filter()` mantém apenas os elementos que satisfazem a condição definida pela lambda.

O resultado final contém apenas os quadrados pares.

Esse exercício ajudou no aprendizado de:

- transformação de dados com `map()`
- filtragem de dados com `filter()`
- utilização prática de funções lambda
- manipulação eficiente de listas

---

# Exercício 003

[Ver código](./Exercício003.py)

## Objetivo

Compreender o funcionamento básico da instrução `yield`.

## O que foi utilizado

- Funções geradoras
- `yield`
- `next()`
- Iteradores

## Explicação

Foi criada uma função geradora:

```python
def contador():
    yield 1
    yield 2
    yield 3
```

Diferente do `return`, o `yield` pausa a execução da função e guarda seu estado atual.

A cada chamada de:

```python
next(gen)
```

a execução continua exatamente do ponto onde havia parado anteriormente.

Isso permite produzir valores sob demanda sem executar toda a função de uma única vez.

Esse exercício ajudou no aprendizado de:

- funcionamento do `yield`
- geração de valores sob demanda
- controle da execução de funções
- conceito de iteradores

---

# Exercício 004

[Ver código](./Exercício004.py)

## Objetivo

Simular um processo executado em etapas utilizando `yield`.

## O que foi utilizado

- Funções geradoras
- `yield`
- `next()`
- Fluxo de execução

## Explicação

Foi criada uma função que representa um carregamento:

```python
def carregando():
    print('25%')
    yield

    print('50%')
    yield

    print('75%')
    yield

    print('100%')
```

Cada chamada de:

```python
next(gen)
```

faz a função avançar para a próxima etapa.

Esse comportamento é útil para processos que precisam executar tarefas gradualmente ou produzir resultados ao longo do tempo.

Esse exercício ajudou na compreensão de:

- pausas controladas na execução
- funcionamento interno dos generators
- execução passo a passo de funções

---

# Exercício 005

[Ver código](./Exercício005.py)

## Objetivo

Criar um gerador infinito utilizando `yield`.

## O que foi utilizado

- `yield`
- Laço `while`
- Iteradores
- Generator Functions

## Explicação

Foi criada uma função geradora infinita:

```python
def infinito():
    numero = 1

    while True:
        yield numero
        numero += 1
```

A cada chamada:

```python
next(gen)
```

o próximo número é produzido.

Como o laço utiliza:

```python
while True
```

o gerador nunca termina naturalmente.

Esse tipo de estrutura é muito utilizada quando se deseja gerar valores continuamente sem armazenar grandes quantidades de dados na memória.

Esse exercício ajudou no aprendizado de:

- generators infinitos
- produção contínua de dados
- economia de memória
- utilização avançada de `yield`