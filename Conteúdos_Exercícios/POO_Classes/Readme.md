# POO - CLASSES

## Sobre o conteúdo

Programação Orientada a Objetos (POO) é um paradigma que organiza o código em objetos, que representam entidades do mundo real através de atributos e métodos.

Em Python, as classes funcionam como moldes para criar objetos, permitindo reutilização de código, encapsulamento e melhor organização dos programas.

Durante os exercícios deste conteúdo foram utilizados:

- Classes
- Objetos (instâncias)
- Métodos
- Construtores (`__init__`)
- Atributos
- Encapsulamento
- Métodos especiais
- Docstrings
- Listas
- Condicionais
- Biblioteca Rich
- Manipulação de estado dos objetos

Esses exercícios ajudaram no entendimento dos conceitos fundamentais da Programação Orientada a Objetos, mostrando como modelar situações reais através de classes e objetos, além de praticar organização e reutilização de código.

---

# Índice

## Exercícios

- [Exercício 001](#exercício-001)
- [Exercício 002](#exercício-002)
- [Exercício 003](#exercício-003)
- [Exercício 004](#exercício-004)
- [Exercício 005](#exercício-005)

## Desafios

- [Desafio 001](#desafio-001)
- [Desafio 002](#desafio-002)
- [Desafio 003](#desafio-003)
- [Desafio 004](#desafio-004)
- [Desafio 005](#desafio-005)
- [Desafio 006](#desafio-006)
- [Desafio 007](#desafio-007)

---

# Exercício 001

[Ver código](./Exercício001.py)

## Objetivo

Criar uma classe representando carros e manipular seus atributos e métodos.

## O que foi utilizado

- Classes
- Objetos
- Construtor `__init__`
- Métodos
- Atributos
- Booleanos
- Função `isinstance()`

## Explicação

Foi criada uma classe `Carro` contendo:

- marca
- modelo
- ano
- estado ligado/desligado

Cada objeto possui seus próprios dados e comportamentos.

Também foram criados métodos para:

- ligar
- desligar
- exibir informações

O exercício ajudou a compreender:

- criação de classes
- criação de objetos
- utilização de atributos
- utilização de métodos

---

# Exercício 002

[Ver código](./Exercício002.py)

## Objetivo

Criar um pet virtual simples utilizando Programação Orientada a Objetos.

## O que foi utilizado

- Classes
- Objetos
- Métodos
- Atributos
- Funções `max()` e `min()`

## Explicação

Foi criada uma classe `Pet` contendo:

- nome
- fome
- felicidade

Os métodos permitiam:

- alimentar
- brincar
- visualizar status

Também foi utilizada lógica para limitar valores máximos e mínimos dos atributos.

Esse exercício ajudou a praticar:

- alteração do estado interno dos objetos
- encapsulamento básico
- modelagem de entidades simples

---

# Exercício 003

[Ver código](./Exercício003.py)

## Objetivo

Praticar encapsulamento e controle de acesso aos atributos.

## O que foi utilizado

- Classes
- Encapsulamento
- Métodos getters
- Atributos protegidos
- Atributos privados

## Explicação

A classe `Carro` foi utilizada para demonstrar:

```python
_velocidade
```

como atributo protegido e:

```python
__horsepower
```

como atributo privado.

Também foram criados métodos para:

- acelerar
- frear
- obter velocidade

O exercício ajudou a compreender:

- encapsulamento
- proteção de dados
- boas práticas de acesso aos atributos

---

# Exercício 004

[Ver código](./Exercício004.py)

## Objetivo

Explorar métodos especiais e recursos internos dos objetos.

## O que foi utilizado

- Classes
- Docstrings
- Métodos especiais
- Atributos internos

## Explicação

Foi criada uma classe `Digimon` contendo:

- nome
- vida
- força

Além dos métodos comuns, foram utilizados:

```python
__str__()
```

para personalizar a exibição do objeto.

```python
__getstate__()
```

para retornar informações específicas do estado do objeto.

Também foram explorados:

```python
__dict__
```

```python
__class__
```

```python
__doc__
```

Esse exercício ajudou no entendimento da estrutura interna dos objetos Python.

---

# Exercício 005

[Ver código](./Exercício005.py)

## Objetivo

Simular uma conta bancária utilizando POO.

## O que foi utilizado

- Classes
- Métodos
- Condicionais
- Métodos especiais

## Explicação

Foi criada uma classe `ContaBancaria` contendo:

- número da conta
- titular
- saldo

Os métodos permitiam:

- depositar
- sacar
- visualizar informações da conta

O método:

```python
__str__()
```

foi utilizado para personalizar a exibição do objeto.

Esse exercício ajudou a praticar:

- modelagem de sistemas reais
- alteração de estado dos objetos
- validações através de métodos

---

# Desafio 001

[Ver código](./Desafio001.py)

## Objetivo

Criar uma classe para representar funcionários de uma empresa.

## O que foi utilizado

- Classes
- Objetos
- Biblioteca Rich

## Explicação

Cada funcionário possui:

- nome
- setor
- cargo
- empresa

Foi criado um método responsável por gerar uma apresentação personalizada utilizando recursos visuais da biblioteca Rich.

---

# Desafio 002

[Ver código](./Desafio002.py)

## Objetivo

Criar etiquetas de produtos utilizando objetos.

## O que foi utilizado

- Classes
- Biblioteca Rich
- Painéis (`Panel`)

## Explicação

Foi criada uma classe `Produto` contendo:

- nome
- preço

O método `etiqueta()` gera automaticamente uma apresentação formatada para exibição no terminal.

---

# Desafio 003

[Ver código](./Desafio003.py)

## Objetivo

Calcular os custos de um churrasco com base na quantidade de convidados.

## O que foi utilizado

- Classes
- Operações matemáticas
- Biblioteca Rich

## Explicação

A classe recebe:

- nome do evento
- quantidade de participantes

O programa calcula:

- quantidade de carne necessária
- custo total
- valor por participante

---

# Desafio 004

[Ver código](./Desafio004.py)

## Objetivo

Simular a leitura de um livro.

## O que foi utilizado

- Classes
- Laços de repetição
- Biblioteca Rich
- Biblioteca Time

## Explicação

A classe controla:

- título
- total de páginas
- página atual

Foi implementada a navegação pelas páginas até o final do livro.

Esse desafio ajudou a praticar gerenciamento de estado dos objetos.

---

# Desafio 005

[Ver código](./Desafio005.py)

## Objetivo

Criar uma ficha de jogador com lista de jogos favoritos.

## O que foi utilizado

- Classes
- Listas
- Biblioteca Rich
- Painéis

## Explicação

Cada objeto armazena:

- nome
- nickname
- jogos favoritos

Foi criado um método para exibir uma ficha formatada contendo todas as informações cadastradas.

---

# Desafio 006

[Ver código](./Desafio006.py)

## Objetivo

Simular o funcionamento de canetas coloridas.

## O que foi utilizado

- Classes
- Dicionários
- Biblioteca Rich
- Métodos

## Explicação

Cada caneta possui:

- cor
- estado tampada/destampada

Os métodos permitem:

- destampar
- escrever
- quebrar linhas

Também foi utilizado um dicionário para mapear nomes de cores para as cores aceitas pela Rich.

---

# Desafio 007

[Ver código](./Desafio007.py)

## Objetivo

Criar um simulador de controle remoto para televisão.

## O que foi utilizado

- Classes
- Condicionais
- Loops
- Biblioteca Rich
- Painéis
- Manipulação de estado
- Biblioteca OS

## Explicação

Foi criada uma classe `ControleRemoto` capaz de controlar:

- ligar/desligar TV
- mudar canais
- alterar volume

O sistema exibe uma interface visual no terminal utilizando a biblioteca Rich.

Esse desafio reuniu diversos conceitos estudados ao longo do conteúdo, servindo como uma aplicação prática de Programação Orientada a Objetos.