# TRY / EXCEPT

## Sobre o conteúdo

O bloco `try/except` é utilizado para tratar erros durante a execução do programa.

Isso permite evitar que o programa seja encerrado inesperadamente quando ocorre uma exceção.

Estrutura básica:

```python
try:
    comando
except:
    tratamento_do_erro
```

Também podem ser utilizados:
- `else`
- `finally`

Onde:
- `else` executa caso nenhum erro aconteça
- `finally` executa independentemente de ocorrer erro ou não

Durante os exercícios deste conteúdo foram utilizados:
- tratamento de exceções
- validação de entrada
- múltiplos tipos de erro
- funções
- laços `while`
- bibliotecas externas
- acesso a sites

O tratamento de erros é essencial para evitar falhas no programa quando entradas inválidas ou inesperadas forem informadas pelo usuário. Ele ajuda a tornar o sistema mais seguro, estável e confiável.

---

# Índice

- [Exercício001](#exercício-001)
- [Exercício002](#exercício-002)
- [Exercício003](#exercício-003)

---

# Exercício 001

[Ver código](./Exercício001.py)

## Objetivo
Realizar uma divisão com tratamento de possíveis erros.

## O que foi utilizado
- `try`
- `except`
- `else`
- `finally`
- Tratamento de exceções específicas

## Explicação
O programa solicita:
- numerador
- denominador

Depois realiza a divisão:

```python
r = a / b
```

Foram tratados diferentes tipos de erro:

### `ValueError` e `TypeError`
Ocorrem quando o usuário informa valores inválidos para conversão.

### `ZeroDivisionError`
Ocorre quando se tenta dividir um número por zero.

### `KeyboardInterrupt`
Ocorre quando o usuário interrompe a execução manualmente.

### `Exception`
Captura qualquer outro erro não tratado anteriormente.

Também foi utilizado:
```python
erro.__class__
```

para mostrar a classe do erro encontrado.

Além disso:
- `else` executa caso não ocorra erro
- `finally` executa sempre ao final do programa

Esse exercício ajudou no aprendizado de:
- tratamento de exceções
- prevenção de falhas
- organização de tratamento de erros
- múltiplos tipos de exceção

---

# Exercício 002

[Ver código](./Exercício002.py)

## Objetivo
Criar funções para validar números inteiros e reais.

## O que foi utilizado
- Funções
- Estrutura `while`
- `try/except`
- Validação de entrada
- `KeyboardInterrupt`

## Explicação
O programa cria duas funções:
- `leiaInt()`
- `leiaFloat()`

Essas funções continuam solicitando valores até que o usuário informe um valor válido.

Foi utilizado:
```python
int(num)
```

e:
```python
float(num)
```

para validar os dados digitados.

Caso ocorra erro:
- o programa exibe uma mensagem personalizada
- solicita novamente a entrada

Também foi tratado:
```python
KeyboardInterrupt
```

caso o usuário interrompa a entrada de dados.

Esse exercício ajudou no aprendizado de:
- reutilização de código com funções
- validação robusta de entradas
- tratamento de erros em funções
- criação de entradas mais seguras

Foi um exercício importante porque simulou situações comuns em sistemas reais.

---

# Exercício 003

[Ver código](./Exercício003.py)

## Objetivo
Verificar se um site está acessível utilizando Python.

## O que foi utilizado
- Biblioteca `urllib.request`
- `try/except`
- Acesso a URLs

## Explicação
O programa tenta acessar o site do Instagram utilizando:

```python
urllib.request.urlopen()
```

Caso o acesso funcione:
- o programa informa sucesso

Caso ocorra erro:
- informa que o site não está acessível

Esse exercício ajudou no aprendizado de:
- acesso a recursos da internet
- utilização de bibliotecas externas
- tratamento de falhas de conexão
- aplicações práticas do `try/except`

Foi um exercício interessante porque mostrou como Python pode interagir diretamente com serviços online.