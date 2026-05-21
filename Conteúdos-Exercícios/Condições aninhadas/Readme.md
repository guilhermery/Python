# CONDIÇÕES ANINHADAS

## Sobre o conteúdo

Condições aninhadas são estruturas condicionais colocadas dentro de outras estruturas condicionais.

Em Python, isso geralmente acontece utilizando:
- `if`
- `elif`
- `else`

Esse tipo de estrutura permite criar programas com múltiplos caminhos de decisão, tornando a lógica mais complexa e organizada.

Durante os exercícios deste conteúdo foram utilizados:
- condicionais aninhadas
- múltiplas verificações
- operadores lógicos
- funções
- dicionários
- laços de repetição
- conversão numérica
- formatação com cores ANSI

Esses exercícios ajudaram no desenvolvimento da lógica de decisão em cenários mais complexos, onde o programa precisa analisar várias possibilidades diferentes antes de chegar ao resultado final. Em algum momento toda aplicação vira uma sequência gigantesca de “e se isso acontecer?”. Programação é essencialmente ansiedade automatizada.

---

# Índice

- [Exercício 001](#exercício-001)
- [Exercício 002](#exercício-002)
- [Exercício 003](#exercício-003)
- [Exercício 004](#exercício-004)
- [Exercício 005](#exercício-005)
- [Exercício 006](#exercício-006)

---

# Exercício 001

[Ver código](./Exercício001.py)

## Objetivo
Exibir mensagens diferentes dependendo do nome informado pelo usuário.

## O que foi utilizado
- Estruturas `if`, `elif` e `else`
- Operador `in`
- Comparação entre strings

## Explicação
O programa verifica:
- se o nome é "Guilherme"
- se o nome é "Demogorgon"
- se o nome pertence a uma lista de nomes femininos

Foi utilizado:
```python
nome in 'Ana Claudia Jessica Juliana'
```

para verificar se o nome informado corresponde a algum dos nomes definidos.

Esse exercício ajudou na prática de:
- comparação de textos
- múltiplas decisões
- uso do operador `in`

---

# Exercício 002

[Ver código](./Exercício002.py)

## Objetivo
Simular a aprovação ou reprovação de um empréstimo bancário.

## O que foi utilizado
- Estruturas condicionais
- Operações matemáticas
- Dicionários
- Cores ANSI

## Explicação
O programa calcula o valor da prestação mensal do empréstimo:

```python
prestacao = vCasa / (tempo * 12)
```

Depois verifica se a prestação ultrapassa 30% do salário do comprador.

Caso ultrapasse:
- empréstimo negado

Caso contrário:
- empréstimo aprovado

Também foram utilizadas cores ANSI para estilizar a saída no terminal utilizando um dicionário.

Esse exercício ajudou no aprendizado de:
- cálculos financeiros
- organização de códigos com dicionários
- personalização visual no terminal

---

# Exercício 003

[Ver código](./Exercício003.py)

## Objetivo
Converter números inteiros para:
- binário
- octal
- hexadecimal

## O que foi utilizado
- Estruturas condicionais
- Laços `while`
- Divisão inteira
- Operador módulo `%`
- Manipulação de strings

## Explicação
O programa solicita:
- um número inteiro
- o tipo de conversão desejada

As conversões foram feitas manualmente utilizando:
- resto da divisão
- divisão inteira

Exemplo:
```python
n % 2
```

para obter os dígitos binários.

Ao final:
```python
traducao[::-1]
```

foi utilizado para inverter a string, já que os restos são obtidos na ordem inversa.

Esse exercício foi importante para:
- compreender sistemas numéricos
- praticar laços de repetição
- desenvolver lógica matemática

---

# Exercício 004

[Ver código](./Exercício004.py)

## Objetivo
Comparar dois números inteiros e identificar qual é maior.

## O que foi utilizado
- Estruturas condicionais
- Funções
- Dicionários
- Tuplas
- Desempacotamento com `*`

## Explicação
O programa compara dois números:
- primeiro maior
- segundo maior
- ou iguais

Foi criada uma função para evitar repetição de código:

```python
def padrao_cores(c):
```

A função retorna uma tupla contendo as cores utilizadas nas mensagens.

Também foi utilizado:
```python
*padrao_cores(color)
```

para desempacotar os valores da tupla dentro do `.format()`.

Esse exercício ajudou no aprendizado de:
- reutilização de código
- criação de funções
- desempacotamento de tuplas
- organização lógica

---

# Exercício 005

[Ver código](./Exercício005.py)

## Objetivo
Verificar a situação do alistamento militar com base na idade.

## O que foi utilizado
- Estruturas condicionais
- Operações matemáticas
- Formatação com cores ANSI

## Explicação
O programa calcula a idade do usuário utilizando o ano atual:

```python
2026 - nasc
```

Depois verifica:
- se está na idade de alistamento
- se ainda vai se alistar
- ou se já passou do prazo

Esse exercício trabalhou:
- cálculos de idade
- múltiplas verificações
- comparação numérica

---

# Exercício 006

[Ver código](./Exercício006.py)

## Objetivo
Classificar atletas de acordo com a idade.

## O que foi utilizado
- Estruturas `if` e `elif`
- Operações matemáticas
- Comparações numéricas

## Explicação
O programa calcula a idade do usuário e define a categoria:
- Mirim
- Infantil
- Junior
- Senior
- Master

Cada categoria possui uma faixa etária específica.

Esse exercício ajudou no aprendizado de:
- classificações por faixa de idade
- múltiplas condições
- organização lógica com `elif`