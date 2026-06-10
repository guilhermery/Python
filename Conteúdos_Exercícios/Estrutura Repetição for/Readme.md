# ESTRUTURA DE REPETIÇÃO FOR

## Sobre o conteúdo

A estrutura de repetição `for` é utilizada para executar blocos de código várias vezes de forma controlada.

Em Python, ela é muito utilizada junto com:
- `range()`
- listas
- strings
- dicionários

Estrutura básica:

```python
for variável in sequência:
    comando
```

Exemplo:
```python
for c in range(1, 6):
    print(c)
```

Durante os exercícios deste conteúdo foram utilizados:
- laços `for`
- função `range()`
- operadores matemáticos
- condicionais
- acumuladores
- contadores
- cálculos matemáticos

Os laços de repetição são fundamentais para automatizar tarefas repetitivas e evitar a duplicação desnecessária de código. Eles permitem executar comandos várias vezes de forma mais prática e eficiente.

---

# Índice

- [Exercício001](#exercício-001)
- [Exercício002](#exercício-002)
- [Exercício003](#exercício-003)
- [Exercício004](#exercício-004)
- [Exercício005](#exercício-005)
- [Exercício006](#exercício-006)
- [Exercício007](#exercício-007)

---

# Exercício 001

[Ver código](./Exercício001.py)

## Objetivo
Criar uma contagem regressiva.

## O que foi utilizado
- Estrutura `for`
- Função `range()`
- Biblioteca `time`
- Função `sleep()`

## Explicação
O programa realiza uma contagem regressiva de 10 até 0 utilizando:

```python
range(10, -1, -1)
```

Onde:
- `10` → início
- `-1` → limite final
- `-1` → decremento

Também foi utilizado:
```python
time.sleep(1)
```

para criar uma pausa de 1 segundo entre cada número.

Esse exercício ajudou no aprendizado de:
- contagens decrescentes
- controle de repetições
- utilização de bibliotecas externas

---

# Exercício 002

[Ver código](./Exercício002.py)

## Objetivo
Mostrar números pares entre 1 e 50.

## O que foi utilizado
- Estrutura `for`
- Operador módulo `%`
- Estrutura condicional

## Explicação
O programa percorre os números de 1 até 49 e verifica:

```python
c % 2 == 0
```

para identificar números pares.

Quando a condição é verdadeira:
- o número é exibido

Esse exercício ajudou na prática de:
- repetições numéricas
- identificação de números pares
- combinação entre `for` e `if`

---

# Exercício 003

[Ver código](./Exercício003.py)

## Objetivo
Somar números ímpares múltiplos de 3.

## O que foi utilizado
- Estrutura `for`
- Operadores matemáticos
- Variável acumuladora
- Condicionais

## Explicação
O programa percorre números entre 1 e 499 e verifica:
- se o número é ímpar
- se é múltiplo de 3

Caso ambas as condições sejam verdadeiras:
- o valor é somado na variável `soma`

Foi utilizado:
```python
soma += c
```

para acumular os valores encontrados.

Esse exercício trabalhou:
- múltiplas condições
- acumuladores
- lógica matemática

---

# Exercício 004

[Ver código](./Exercício004.py)

## Objetivo
Gerar a tabuada de um número.

## O que foi utilizado
- Estrutura `for`
- Operações matemáticas
- Entrada de dados

## Explicação
O programa solicita um número e exibe sua tabuada de 1 até 10.

Foi utilizado:
```python
c * n
```

para calcular os resultados da multiplicação.

Esse exercício ajudou na prática de:
- repetições controladas
- cálculos matemáticos
- exibição organizada de resultados

---

# Exercício 005

[Ver código](./Exercício005.py)

## Objetivo
Somar apenas os números pares informados pelo usuário.

## O que foi utilizado
- Estrutura `for`
- Condicionais
- Variável acumuladora

## Explicação
O programa solicita seis números ao usuário.

A cada número informado:
- verifica se é par
- caso seja, soma o valor na variável `soma`

Esse exercício ajudou no aprendizado de:
- filtragem de dados
- uso de acumuladores
- integração entre repetição e condição

---

# Exercício 006

[Ver código](./Exercício006.py)

## Objetivo
Gerar os termos de uma progressão aritmética.

## O que foi utilizado
- Estrutura `for`
- Operações matemáticas
- Progressão aritmética

## Explicação
O programa solicita:
- primeiro termo
- razão

Depois exibe os 10 primeiros termos da progressão.

A cada repetição:
```python
a1 += razao
```

é utilizado para atualizar o valor do próximo termo.

Esse exercício ajudou na compreensão de:
- sequências matemáticas
- atualização de variáveis
- repetições progressivas

---

# Exercício 007

[Ver código](./Exercício007.py)

## Objetivo
Verificar se um número é primo.

## O que foi utilizado
- Estrutura `for`
- Operador módulo `%`
- Variável contadora
- Estruturas condicionais

## Explicação
O programa verifica quantas vezes o número pode ser dividido exatamente.

Foi utilizado:
```python
n % c == 0
```

para identificar divisões exatas.

A variável `cont` conta quantos divisores o número possui.

Se possuir:
- mais de dois divisores → não é primo
- exatamente dois divisores → é primo

Esse exercício foi importante para:
- desenvolver raciocínio lógico
- trabalhar contadores
- compreender números primos
- utilizar repetições para análise matemática

Foi um exercício mais avançado do conteúdo devido à lógica necessária para validar corretamente os divisores.