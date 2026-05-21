# CORES NO TERMINAL

## Sobre o conteúdo

Python permite utilizar códigos ANSI para alterar:
- cores do texto
- cores de fundo
- estilos da fonte

Esses códigos funcionam principalmente em terminais compatíveis e ajudam a deixar a saída do programa mais organizada e visualmente agradável.

Durante os exercícios deste conteúdo foram utilizados:
- códigos ANSI
- formatação de strings
- dicionários
- método `.format()`

Os códigos ANSI seguem geralmente esta estrutura:

```python
\033[style;text;backgroundm
```

Exemplo:
```python
\033[1;31;43m
```

Onde:
- `1` → negrito
- `31` → texto vermelho
- `43` → fundo amarelo

Para limpar a formatação:
```python
\033[m
```

Esse conteúdo ajudou a compreender como personalizar mensagens no terminal. Porque aparentemente programadores olham para texto puro e pensam “isso precisa urgentemente ficar amarelo fluorescente”.

---

# Índice

- [Exercício001](#exercício001)
- [Exercício002](#exercício002)
- [Exercício003](#exercício003)

---

# Exercício001

[Ver código](./Exercício001.py)

## Objetivo
Exibir textos coloridos e estilizados no terminal.

## O que foi utilizado
- Códigos ANSI
- Estilos de fonte
- Cores de texto
- Cores de fundo

## Explicação
O programa utiliza códigos ANSI diretamente dentro do `print()` para alterar a aparência do texto.

Exemplo:
```python
\033[1;31;43m
```

Esse código aplica:
- negrito
- texto vermelho
- fundo amarelo

Também foi utilizado:
```python
\033[m
```

para resetar as configurações de cor e evitar que o terminal continue colorido após a mensagem.

Esse exercício ajudou no aprendizado de:
- estilização no terminal
- estrutura dos códigos ANSI
- personalização visual

---

# Exercício002

[Ver código](./Exercício002.py)

## Objetivo
Utilizar cores ANSI junto com `.format()`.

## O que foi utilizado
- Método `.format()`
- Códigos ANSI
- Variáveis

## Explicação
O programa insere os códigos ANSI dentro do `.format()` para estilizar apenas partes específicas da frase.

Exemplo:
```python
'{}{}{}'.format(cor, texto, limpar)
```

Nesse caso:
- a cor é aplicada apenas ao nome
- depois a formatação é resetada

Esse exercício ajudou no aprendizado de:
- integração entre formatação e cores
- manipulação de strings
- personalização parcial de textos

---

# Exercício003

[Ver código](./Exercício003.py)

## Objetivo
Organizar códigos ANSI utilizando dicionários.

## O que foi utilizado
- Dicionários
- Códigos ANSI
- Método `.format()`

## Explicação
O programa armazena os códigos ANSI dentro de um dicionário:

```python
cores = {
    'azul':'\033[34m'
}
```

Isso facilita:
- reutilização
- organização
- legibilidade do código

Depois as cores são acessadas pelas chaves do dicionário:

```python
cores['azul']
```

Esse exercício ajudou no aprendizado de:
- organização de códigos repetitivos
- utilização prática de dicionários
- melhoria da legibilidade do programa