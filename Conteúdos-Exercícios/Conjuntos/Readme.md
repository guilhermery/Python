# Conjuntos (Sets)

Nesta pasta estão os exercícios relacionados a **conjuntos (sets)** em Python.

Os conjuntos são estruturas de dados utilizadas para armazenar coleções de elementos sem repetição. Diferente das listas e tuplas, a ordem dos elementos não é garantida e não existe acesso por índice.

Esse conteúdo foi importante para entender operações matemáticas entre coleções de dados, algo muito utilizado em comparação de informações, remoção de duplicatas e análise de dados.

---

# O que aprendi

- O que são conjuntos (`set`)
- Como criar conjuntos
- Como adicionar elementos com `add()`
- Como remover elementos com `remove()`
- Diferenças entre conjuntos e listas
- União entre conjuntos
- Interseção entre conjuntos
- Diferença entre conjuntos
- Eliminação automática de elementos repetidos

---
# Índice

- [Exercício 001](#exercício-001)
- [Exercício 002](#exercício-002)
- [Exercício 003](#exercício-003)
---

# Exercício 001

[Ver código](./Exercício001.py)

Primeiro contato com conjuntos.

Conceitos praticados:

- Criação de conjuntos utilizando chaves `{ }`
- Adição de elementos com `add()`
- Remoção de elementos com `remove()`
- Entendimento das características dos conjuntos:
  - Não possuem elementos repetidos
  - Não possuem índices
  - A ordem dos elementos não importa
  - São mutáveis

---

# Exercício 002

[Ver código](./Exercício002.py)

Prática das principais operações entre conjuntos.

Conceitos praticados:

- União de conjuntos utilizando `union()`
- Interseção utilizando `intersection()`
- Diferença utilizando `difference()`

Exemplo estudado:

```python
conj1.union(conj2)
conj1.intersection(conj2)
conj1.difference(conj2)
```
---

# Exercício 003

[Ver código](./Exercício003.py)

Comparação entre dois grupos de pessoas utilizando conjuntos.

Conceitos praticados:

- Identificação de elementos presentes em ambos os conjuntos utilizando `intersection()`
- Identificação de elementos exclusivos de cada conjunto utilizando `difference()`
- União dos conjuntos sem repetição de elementos utilizando `union()`

Exemplo estudado:

```python
Conj1.intersection(Conj2)
Conj1.difference(Conj2)
Conj2.difference(Conj1)
Conj1.union(Conj2)