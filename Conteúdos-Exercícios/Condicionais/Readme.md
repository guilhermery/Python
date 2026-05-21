# CONDICIONAIS

## Sobre o conteúdo

Condicionais são estruturas utilizadas para permitir que o programa tome decisões com base em determinadas condições.

Em Python, as principais estruturas condicionais são:

- `if`
- `elif`
- `else`

Essas estruturas trabalham com expressões booleanas, ou seja, condições que resultam em:
- `True`
- `False`

Durante os exercícios deste conteúdo foram utilizados:
- operadores relacionais (`>`, `<`, `>=`, `<=`, `==`)
- operadores lógicos (`and`, `or`)
- condicionais aninhadas
- comparações numéricas
- cálculos condicionais

---

# Índice

- [Exercício 001](#exercício-001)
- [Exercício 002](#exercício-002)
- [Exercício 003](#exercício-003)
- [Exercício 004](#exercício-004)
- [Exercício 005](#exercício-005)
- [Exercício 006](#exercício-006)
- [Exercício 007](#exercício-007)
- [Exercício 008](#exercício-008)
- [Exercício 009](#exercício-009)

---

# Exercício 001

[Ver código](./Exercício001.py)

## Objetivo
Classificar uma pessoa em categorias com base na idade e no peso.

## O que foi utilizado
- Estruturas `if` e `else`
- Condicionais aninhadas
- Operadores relacionais
- Operador lógico `and`

## Explicação
O programa verifica:
- se a pessoa possui idade mínima
- se pertence à categoria juvenil
- se pertence à categoria adulto leve ou pesado

Esse exercício ajudou na prática de:
- múltiplas decisões
- hierarquia de condições
- combinação de condições

---

# Exercício 002

[Ver código](./Exercício002.py)

## Objetivo
Calcular imposto e salário líquido com base no salário bruto.

## O que foi utilizado
- Estruturas condicionais
- Operações matemáticas
- Variáveis
- Formatação de valores monetários

## Explicação
O programa verifica em qual faixa salarial o usuário se encontra e aplica diferentes porcentagens de imposto.

Após calcular o imposto:
- o valor é descontado do salário bruto
- o salário líquido é exibido

Esse exercício ajudou no aprendizado de:
- cálculos condicionais
- lógica baseada em faixas salariais
- reutilização de variáveis

---

# Exercício 003

[Ver código](./Exercício003.py)

## Objetivo
Identificar em qual quadrante um ponto cartesiano está localizado.

## O que foi utilizado
- Operadores lógicos
- Estruturas `if` e `elif`
- Coordenadas cartesianas

## Explicação
O programa recebe os valores de `x` e `y` e identifica:
- se o ponto está sobre os eixos
- em qual quadrante ele pertence

Esse exercício trabalhou:
- lógica matemática
- múltiplas comparações
- operadores lógicos

---

# Exercício 004

[Ver código](./Exercício004.py)

## Objetivo
Criar um jogo simples de adivinhação.

## O que foi utilizado
- Biblioteca `random`
- Comparação de valores
- Estruturas condicionais

## Explicação
O programa gera um número aleatório entre 0 e 5 e o usuário tenta adivinhar.

Foi utilizado:
```python
random.randint(0, 5)
```

Esse exercício introduziu:
- geração de números aleatórios
- comparação de dados
- interação com o usuário

---

# Exercício 005

[Ver código](./Exercício005.py)

## Objetivo
Calcular multa por excesso de velocidade.

## O que foi utilizado
- Comparação numérica
- Operações matemáticas
- Estrutura `if`

## Explicação
O programa verifica se a velocidade ultrapassa 80 km/h.

Caso ultrapasse:
- calcula uma multa de R$7 por km excedido

Esse exercício ajudou na prática de:
- cálculos condicionais
- fórmulas matemáticas
- validações simples

---

# Exercício 006

[Ver código](./Exercício006.py)

## Objetivo
Calcular o valor de uma viagem com base na distância.

## O que foi utilizado
- Estrutura `if/else`
- Operações matemáticas

## Explicação
O programa aplica:
- R$0,50 por km para viagens até 200 km
- R$0,45 por km para viagens acima de 200 km

Esse exercício trabalhou:
- tomada de decisão
- cálculos proporcionais
- condições simples

---

# Exercício 007

[Ver código](./Exercício007.py)

## Objetivo
Identificar o maior e o menor valor entre três números.

## O que foi utilizado
- Condicionais aninhadas
- Comparações múltiplas
- Variáveis auxiliares

## Explicação
O programa compara três números inteiros para descobrir:
- qual é o maior
- qual é o menor

Esse exercício ajudou no desenvolvimento de:
- raciocínio lógico
- análise de múltiplas possibilidades
- fluxo de decisões complexas

---

# Exercício 008

[Ver código](./Exercício008.py)

## Objetivo
Calcular aumento salarial.

## O que foi utilizado
- Estrutura condicional
- Operações matemáticas
- Porcentagem

## Explicação
O programa verifica o salário do funcionário e aplica:
- aumento de 10%
- ou aumento de 15%

Esse exercício reforçou:
- cálculos percentuais
- atualização de variáveis
- decisões baseadas em valores

---

# Exercício 009

[Ver código](./Exercício009.py)

## Objetivo
Verificar se três retas formam um triângulo e identificar seu tipo.

## O que foi utilizado
- Operadores lógicos
- Condicionais compostas
- Comparações entre valores

## Explicação
Primeiramente o programa verifica se as retas podem formar um triângulo.

Depois identifica:
- equilátero
- isósceles
- escaleno

Esse exercício trabalhou:
- lógica matemática
- validação de condições
- classificação baseada em características