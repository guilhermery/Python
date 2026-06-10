# DICIONÁRIOS

## Sobre o conteúdo

Dicionários são estruturas de dados utilizadas para armazenar informações em pares de:
- chave
- valor

Em Python, dicionários utilizam a seguinte estrutura:

```python
dados = {
    'nome': 'Guilherme',
    'idade': 20
}
```

Nesse exemplo:
- `'nome'` e `'idade'` são as chaves
- `'Guilherme'` e `20` são os valores

Durante os exercícios deste conteúdo foram utilizados:
- criação de dicionários
- acesso a chaves e valores
- métodos `.keys()`, `.values()` e `.items()`
- listas com dicionários
- cópia de dicionários com `.copy()`
- estruturas aninhadas
- laços `for`
- funções como `sorted()` e `enumerate()`

Os dicionários são estruturas que permitem armazenar dados de forma organizada por meio de chaves e valores, facilitando o acesso e a manipulação das informações de maneira mais clara e eficiente.

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

---

# Exercício 001

[Ver código](./Exercício001.py)

## Objetivo
Aprender operações básicas com dicionários.

## O que foi utilizado
- Criação de dicionários
- Adição e remoção de dados
- Métodos `.keys()`, `.values()` e `.items()`
- Estrutura `for`

## Explicação
O exercício apresentou:
- como criar dicionários
- adicionar novos dados
- remover informações
- acessar valores pelas chaves

Também foram utilizados:
```python
dados.keys()
dados.values()
dados.items()
```

para exibir:
- apenas chaves
- apenas valores
- ou ambos

Além disso, foi utilizado:
```python
for k, v in pessoas.items():
```

para percorrer simultaneamente:
- chave (`k`)
- valor (`v`)

Esse exercício ajudou no aprendizado da estrutura básica dos dicionários e na manipulação de dados organizados.

---

# Exercício 002

[Ver código](./Exercício002.py)

## Objetivo
Trabalhar com listas contendo dicionários.

## O que foi utilizado
- Listas
- Dicionários
- Acesso a elementos aninhados

## Explicação
O programa cria:
- uma lista chamada `brasil`
- dicionários representando estados

Depois adiciona os dicionários na lista:

```python
brasil += [estado1, estado2]
```

Também foi realizado acesso aninhado:

```python
brasil[0]['uf']
```

onde:
- `brasil[0]` acessa o primeiro dicionário
- `['uf']` acessa o valor da chave

Esse exercício ajudou na compreensão de estruturas compostas, muito utilizadas em aplicações reais.

---

# Exercício 003

[Ver código](./Exercício003.py)

## Objetivo
Cadastrar estados dinamicamente utilizando listas e dicionários.

## O que foi utilizado
- Dicionários
- Listas
- Laços `for`
- Método `.copy()`

## Explicação
O programa solicita:
- unidade federativa
- sigla do estado

Depois adiciona cada estado na lista `brasil`.

Foi utilizado:
```python
estado.copy()
```

porque sem a cópia a lista armazenaria apenas a última alteração do dicionário.

Também foi utilizado:
```python
for k, v in e.items():
```

para percorrer cada dicionário armazenado na lista.

Esse exercício foi importante para:
- compreender referências de memória
- evitar sobrescrita de dados
- manipular estruturas compostas

---

# Exercício 004

[Ver código](./Exercício004.py)

## Objetivo
Cadastrar informações de um aluno e definir sua situação.

## O que foi utilizado
- Dicionários
- Estruturas condicionais
- Comparações numéricas

## Explicação
O programa armazena:
- nome
- média
- situação

Depois verifica:
- se a média é maior ou igual a 60

Caso seja:
- aluno aprovado

Caso contrário:
- aluno reprovado

Esse exercício ajudou no aprendizado de:
- armazenamento de informações relacionadas
- integração entre dicionários e condicionais
- acesso a valores por chave

---

# Exercício 005

[Ver código](./Exercício005.py)

## Objetivo
Simular sorteios de dados e gerar um ranking.

## O que foi utilizado
- Biblioteca `random`
- Dicionários
- Função `sorted()`
- `lambda`
- `enumerate()`

## Explicação
O programa sorteia valores para cada jogador:

```python
random.randint(1, 6)
```

Depois cria um ranking utilizando:

```python
sorted()
```

Foi utilizada:
```python
lambda item: item[1]
```

para ordenar com base no valor sorteado.

Também foi utilizado:
```python
enumerate()
```

para mostrar as posições do ranking.

Esse exercício ajudou no aprendizado de:
- ordenação de dados
- funções anônimas (`lambda`)
- manipulação avançada de dicionários

---

# Exercício 006

[Ver código](./Exercício006.py)

## Objetivo
Cadastrar dados trabalhistas de uma pessoa.

## O que foi utilizado
- Dicionários
- Estruturas condicionais
- Operações matemáticas

## Explicação
O programa armazena:
- nome
- idade
- carteira de trabalho
- salário
- ano de contratação

Caso a pessoa possua carteira assinada:
- calcula aposentadoria
- exibe informações adicionais

Esse exercício trabalhou:
- armazenamento de múltiplos dados relacionados
- cálculos condicionais
- atualização de informações no dicionário

---

# Exercício 007

[Ver código](./Exercício007.py)

## Objetivo
Cadastrar desempenho de um jogador de futebol.

## O que foi utilizado
- Dicionários
- Listas
- Laços `for`
- `enumerate()`

## Explicação
O programa armazena:
- nome do jogador
- gols por partida
- total de gols

Foi utilizada uma lista dentro do dicionário:

```python
jogador['gols'] = list()
```

para armazenar os gols de cada partida.

Também foi utilizado:
```python
enumerate()
```

para exibir:
- número da partida
- quantidade de gols

Esse exercício foi importante para compreender:
- estruturas aninhadas
- listas dentro de dicionários
- organização de dados complexos

---

# Exercício 008

[Ver código](./Exercício008.py)

## Objetivo
Cadastrar várias pessoas e realizar análises estatísticas.

## O que foi utilizado
- Listas
- Dicionários
- Estruturas condicionais
- Laços de repetição
- Validação de entrada

## Explicação
O programa permite cadastrar:
- nome
- sexo
- idade

Depois calcula:
- quantidade de pessoas
- média de idade
- mulheres cadastradas
- pessoas acima da média

Foi utilizado:
```python
galera.append(pessoa.copy())
```

para armazenar corretamente cada pessoa cadastrada.

Também foram utilizadas validações para garantir entradas válidas:
```python
if pessoa['sexo'] in 'MF'
```

Esse exercício ajudou no aprendizado de:
- manipulação de estruturas complexas
- análise de dados
- validação de entradas
- estatísticas simples

Foi um dos exercícios mais completos do conteúdo, reunindo praticamente todos os conceitos estudados sobre dicionários.