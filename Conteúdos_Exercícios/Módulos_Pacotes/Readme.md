# Módulos e Pacotes

## Sobre o conteúdo
Nesta pasta foram estudados módulos e pacotes em Python, aprendendo como separar funções em arquivos diferentes para reutilizar código, organizar projetos e deixar os programas mais estruturados. Também foram trabalhados conceitos de importação, modularização e criação de funções utilitárias.

Essa etapa foi importante para entender como organizar projetos em módulos e pacotes, tornando o código mais estruturado, reutilizável e fácil de manter em aplicações maiores.

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

[Ver código](./Exercício001/Exercício001.py)

## Objetivo
Aprender a importar módulos personalizados.

## O que foi utilizado
- módulos
- funções
- `import`

## Explicação
Foi criado o módulo:
```python
uteis001
```

com funções reutilizáveis:
- `fatorial()`
- `dobro()`
- `triplo()`

Depois o programa utilizou:
```python
from uteis001 import numeros
```

para acessar essas funções em outro arquivo.

Esse exercício ajudou no aprendizado de:
- modularização
- reutilização de código
- importação de módulos

---

# Exercício 002

[Ver código](./Exercício002/Exercício002.py)

## Objetivo
Criar um módulo para cálculos monetários.

## O que foi utilizado
- funções
- módulos personalizados
- porcentagem

## Explicação
Foi criado o módulo:
```python
moeda
```

contendo funções para:
- aumentar preço
- diminuir preço
- calcular metade
- calcular dobro

O programa importa o módulo e utiliza:
```python
moeda.metade()
```

e outras funções diretamente.

Esse exercício ajudou no aprendizado de:
- organização de funções
- módulos personalizados
- reutilização de lógica

---

# Exercício 003

[Ver código](./Exercício003/Exercício003.py)

## Objetivo
Formatar valores monetários.

## O que foi utilizado
- formatação de strings
- módulos
- funções

## Explicação
Foi adicionada ao módulo a função:
```python
moeda()
```

que transforma valores numéricos em formato monetário:
```python
R$10,50
```

Também foi utilizado:
```python
.replace('.', ',')
```

para adaptar o padrão brasileiro.

Esse exercício ajudou no aprendizado de:
- formatação de valores
- reutilização de funções
- manipulação de strings

---

# Exercício 004

[Ver código](./Exercício004/Exercício004.py)

## Objetivo
Utilizar parâmetros opcionais em funções.

## O que foi utilizado
- parâmetros booleanos
- funções
- modularização

## Explicação
As funções passaram a receber:
```python
formatado=False
```

permitindo escolher entre:
- retornar número puro
- retornar valor formatado em moeda

Exemplo:
```python
dobro(preco, True)
```

Esse exercício ajudou no aprendizado de:
- parâmetros opcionais
- flexibilidade de funções
- reutilização de código

---

# Exercício 005

[Ver código](./Exercício005/Exercício005.py)

## Objetivo
Criar um resumo financeiro completo.

## O que foi utilizado
- funções
- modularização
- exibição formatada

## Explicação
Foi criada a função:
```python
resumo()
```

que reúne:
- preço original
- dobro
- metade
- aumento
- redução

Tudo organizado em uma única saída formatada.

Esse exercício ajudou no aprendizado de:
- centralização de funcionalidades
- organização de saída
- criação de funções mais completas

---

# Exercício 006

[Ver código](./Exercício006/Exercício006.py)

## Objetivo
Trabalhar com pacotes em Python.

## O que foi utilizado
- pacotes
- submódulos
- validação de entrada

## Explicação
Foi utilizado o pacote:
```python
utilidadesCeV
```

contendo:
- módulo `dado`
- módulo `moeda`

O módulo `dado` possui:
```python
leiaDinheiro()
```

que valida entradas monetárias do usuário.

Já o módulo `moeda` ficou responsável pelos cálculos e formatações.

Esse exercício ajudou no aprendizado de:
- pacotes
- separação de responsabilidades
- validação de dados
- organização profissional de projetos

Foi uma etapa importante porque mostrou como dividir sistemas em partes menores e organizadas. Programadores eventualmente descobrem que manter tudo em um único arquivo é uma experiência espiritual negativa.