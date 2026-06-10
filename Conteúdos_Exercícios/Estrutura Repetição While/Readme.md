# ESTRUTURA DE REPETIÇÃO WHILE

## Sobre o conteúdo

A estrutura de repetição `while` é utilizada para repetir um bloco de código enquanto uma condição for verdadeira.

Estrutura básica:

```python
while condição:
    comando
```

Diferente do `for`, o `while` é mais utilizado quando:
- não se sabe exatamente quantas repetições serão necessárias
- a repetição depende de uma condição dinâmica
- o programa precisa continuar até que o usuário decida parar

Durante os exercícios deste conteúdo foram utilizados:
- laços `while`
- validação de entrada
- acumuladores
- contadores
- condicionais
- menus interativos
- laços infinitos com `while True`
- comando `break`

O `while` é extremamente importante porque permite criar programas mais interativos e flexíveis. Basicamente ele continua funcionando até que alguma condição finalmente convença o programa a parar de insistir.

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
Validar a entrada do sexo do usuário.

## O que foi utilizado
- Estrutura `while`
- Operadores lógicos
- Método `.upper()`

## Explicação
O programa solicita o sexo do usuário até que seja informado:
- `F`
- ou `M`

Foi utilizado:
```python
.upper()
```

para transformar a entrada em maiúscula e facilitar a validação.

A repetição continua enquanto a condição for verdadeira:

```python
while sexo != 'F' and sexo != 'M'
```

Esse exercício ajudou no aprendizado de:
- validação de entradas
- repetições condicionais
- operadores lógicos

---

# Exercício 002

[Ver código](./Exercício002.py)

## Objetivo
Criar um jogo de adivinhação com contagem de tentativas.

## O que foi utilizado
- Biblioteca `random`
- Estrutura `while`
- Variável contadora

## Explicação
O programa gera um número aleatório entre 0 e 10:

```python
random.randint(0,10)
```

Depois o usuário continua tentando adivinhar até acertar.

A variável `cont` é utilizada para contar quantas tentativas foram necessárias.

Esse exercício ajudou no aprendizado de:
- repetições baseadas em acerto
- contadores
- interação com usuário

---

# Exercício 003

[Ver código](./Exercício003.py)

## Objetivo
Criar um menu interativo de operações matemáticas.

## O que foi utilizado
- Estrutura `while`
- Condicionais
- Menu interativo
- Operações matemáticas

## Explicação
O programa apresenta opções para:
- somar
- multiplicar
- verificar maior valor
- informar novos números
- sair do programa

O laço continua funcionando até que o usuário escolha a opção:
```python
5
```

Esse exercício foi importante para:
- desenvolvimento de menus
- controle de fluxo
- programas interativos
- múltiplas decisões

---

# Exercício 004

[Ver código](./Exercício004.py)

## Objetivo
Calcular o fatorial de um número.

## O que foi utilizado
- Estrutura `while`
- Operações matemáticas
- Variáveis auxiliares

## Explicação
O programa calcula o fatorial utilizando multiplicações sucessivas.

Exemplo:
```python
fat = fat * n1
```

A cada repetição:
- o número é multiplicado pelo anterior
- o contador é decrementado

Esse exercício ajudou no aprendizado de:
- cálculos matemáticos
- decremento de variáveis
- lógica de repetição

---

# Exercício 005

[Ver código](./Exercício005.py)

## Objetivo
Gerar os 10 primeiros termos de uma progressão aritmética.

## O que foi utilizado
- Estrutura `while`
- Contador
- Operações matemáticas

## Explicação
O programa solicita:
- primeiro termo
- razão

Depois exibe os 10 primeiros termos da progressão.

Foi utilizada:
```python
a1 = a1 + razao
```

para atualizar o próximo termo da sequência.

Esse exercício trabalhou:
- controle de repetições
- sequências matemáticas
- atualização de variáveis

---

# Exercício 006

[Ver código](./Exercício006.py)

## Objetivo
Gerar a sequência de Fibonacci.

## O que foi utilizado
- Estrutura `while`
- Variáveis auxiliares
- Operações matemáticas

## Explicação
O programa gera os termos da sequência de Fibonacci.

Na sequência:
- cada número é a soma dos dois anteriores

Foi utilizado:
```python
a3 = a1 + a2
```

para calcular o próximo termo.

Depois as variáveis são atualizadas para continuar a sequência.

Esse exercício ajudou no aprendizado de:
- sequências matemáticas
- atualização simultânea de variáveis
- lógica algorítmica

Foi um exercício importante para desenvolver raciocínio lógico mais avançado.

---

# Exercício 007

[Ver código](./Exercício007.py)

## Objetivo
Somar números até que seja digitado um valor de parada.

## O que foi utilizado
- `while True`
- Comando `break`
- Acumulador
- Contador

## Explicação
O programa solicita números indefinidamente.

Quando o usuário digita:
```python
999
```

o laço é encerrado utilizando:
```python
break
```

Enquanto isso:
- os números são somados
- a quantidade de números é contada

Esse exercício ajudou no aprendizado de:
- laços infinitos controlados
- valores sentinela
- utilização do `break`
- acumuladores e contadores

Foi um exercício muito importante para compreender estruturas de repetição mais flexíveis.