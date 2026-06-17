# POO: HERANÇA E POLIMORFISMO

## Sobre o conteúdo

Herança e polimorfismo expandem os conceitos da Programação Orientada a Objetos, permitindo criar classes mais organizadas, reutilizar código e especializar comportamentos.

A herança permite que uma classe filha aproveite atributos e métodos de uma classe pai, enquanto o polimorfismo possibilita que objetos diferentes respondam à mesma chamada de método de maneiras distintas.

Durante os exercícios deste conteúdo foram utilizados:

- herança
- subclasses e superclasses
- método `super()`
- sobrescrita de métodos
- polimorfismo
- métodos especiais
- encapsulamento
- atributos públicos, protegidos e privados
- getters e setters
- propriedades com `@property`
- classes abstratas
- módulos organizados em múltiplos arquivos
- inspeção de objetos
- classes abstratas (ABC)
- métodos abstratos (@abstractmethod)
- Template Method
- modelagem de sistemas orientados a objetos

Esses exercícios ajudaram a compreender melhor a reutilização de código, a especialização de comportamentos e os mecanismos utilizados para controlar o acesso aos dados dos objetos.

---

# Índice

## Exercícios

- [Exercício 001](#exercício-001)
- [Exercício 002](#exercício-002)
- [Exercício 003](#exercício-003)
- [Exercício 004](#exercício-004)
- [Exercício 005](#exercício-005)
- [Exercício 006](#exercício-006)
- [Exercício 007](#exercício-007)
- [Exercício 008](#exercício-008)

## Desafios

- [Desafio 001](#desafio-001)
- [Desafio 002](#desafio-002)
- [Desafio 003](#desafio-003)
- [Desafio 004](#desafio-004)
- [Desafio 005](#desafio-005)

---

# Exercício 001

[Ver código](./Exercício001.py)

## Objetivo

Praticar herança simples utilizando veículos.

## O que foi utilizado

- Classes
- Herança
- `super()`
- Métodos herdados
- Métodos específicos das subclasses

## Explicação

Foi criada uma classe `Veiculo` contendo atributos e métodos básicos.

As classes `Carro` e `Moto` herdam esses comportamentos através da herança:

```python
class Carro(Veiculo)
```

```python
class Moto(Veiculo)
```

Também foi utilizado:

```python
super().__init__()
```

para reaproveitar o construtor da classe pai.

Esse exercício ajudou no aprendizado de:

- reutilização de código
- herança
- especialização de classes

---

# Exercício 002

[Ver código](./Exercício002.py)

## Objetivo

Compreender o conceito de polimorfismo.

## O que foi utilizado

- Herança
- Sobrescrita de métodos
- Polimorfismo

## Explicação

Cada classe possui sua própria implementação do método:

```python
def exibir_informacoes()
```

Mesmo chamando o mesmo método:

```python
v.exibir_informacoes()
```

cada objeto executa uma versão diferente.

Esse é o conceito de polimorfismo.

O exercício ajudou no aprendizado de:

- sobrescrita de métodos
- comportamento dinâmico
- polimorfismo

---

# Exercício 003

[Ver código](./Exercício003.py)

## Objetivo

Explorar métodos especiais do Python.

## O que foi utilizado

- `__str__`
- `__len__`
- Classes

## Explicação

Foram implementados métodos especiais para que o objeto se comporte como um tipo nativo.

Exemplo:

```python
print(livro_python)
```

executa automaticamente:

```python
__str__()
```

Já:

```python
len(livro_python)
```

executa:

```python
__len__()
```

Esse exercício ajudou a compreender:

- dunder methods
- personalização de objetos
- integração com funções nativas

---

# Exercício 004

[Ver código](./Exercício004)

## Objetivo

Organizar um sistema orientado a objetos utilizando múltiplos arquivos.

## O que foi utilizado

- Herança
- Módulos
- Organização em arquivos
- Classe base

## Explicação

Foi criada uma classe principal:

```python
Pessoa
```

que contém atributos e comportamentos compartilhados.

As classes:

- Aluno
- Professor
- Funcionario

herdam da classe pai e adicionam comportamentos próprios.

O exercício também utilizou:

```python
if __name__ == "__main__":
```

para impedir que a função principal seja executada durante importações.

Esse exercício ajudou no aprendizado de:

- separação de responsabilidades
- organização de projetos
- herança prática

---

# Exercício 005

[Ver código](./Exercício005)

## Objetivo

Aprender sobre classes abstratas.

## O que foi utilizado

- `ABC`
- `abstractmethod`
- Herança
- Polimorfismo

## Explicação

Foi criada uma classe abstrata:

```python
class Pessoa(ABC)
```

contendo um método obrigatório:

```python
@abstractmethod
def estudar()
```

Isso força todas as subclasses a implementarem esse método.

Esse exercício ajudou na compreensão de:

- contratos entre classes
- abstração
- arquitetura orientada a objetos

---

# Exercício 006

[Ver código](./Exercício006)

## Objetivo

Estudar encapsulamento e níveis de acesso.

## O que foi utilizado

- Atributos públicos
- Atributos protegidos
- Atributos privados
- Name Mangling

## Explicação

Foram utilizados três níveis de visibilidade:

```python
self.id
```

Atributo público.

```python
self._titular
```

Atributo protegido.

```python
self.__saldo
```

Atributo privado.

Também foi demonstrado como o Python protege atributos privados através do mecanismo conhecido como Name Mangling.

Esse exercício ajudou no aprendizado de:

- encapsulamento
- segurança de dados
- convenções de acesso

---

# Exercício 007

[Ver código](./Exercício007)

## Objetivo

Criar métodos getters e setters.

## O que foi utilizado

- Encapsulamento
- Métodos acessores
- Validação de dados

## Explicação

Foi criado um atributo protegido:

```python
_nota
```

e métodos para controlar seu acesso:

```python
get_nota()
```

```python
set_nota()
```

O setter valida se a nota está dentro do intervalo permitido.

Esse exercício ajudou no aprendizado de:

- controle de acesso
- validação de atributos
- encapsulamento

---

# Exercício 008

[Ver código](./Exercício008)

## Objetivo

Utilizar propriedades com `@property`.

## O que foi utilizado

- `@property`
- Getter
- Setter
- Deleter

## Explicação

Foi criada uma propriedade chamada:

```python
nota
```

permitindo acessar o atributo como se fosse um atributo comum:

```python
av1.nota = 10
```

mas mantendo toda a lógica de validação internamente.

Também foram utilizados:

```python
@property
```

```python
@nota.setter
```

```python
@nota.deleter
```

Esse exercício ajudou no aprendizado de:

- propriedades
- encapsulamento moderno
- código mais limpo e legível

---

# Desafio 001

[Ver código](./Desafio001.py)

## Objetivo

Praticar herança, abstração e polimorfismo através de figuras geométricas.

## O que foi utilizado

- Classes abstratas
- Herança
- Polimorfismo
- Métodos abstratos
- Cálculo de área
- Cálculo de perímetro

## Explicação

Foi criada uma classe abstrata:

```python
class Poligono(ABC)
```

que define dois comportamentos obrigatórios:

```python
area()
```

```python
perimetro()
```

As classes:

- Quadrado
- Circulo

implementam esses métodos de formas diferentes.

Esse desafio ajudou no aprendizado de:

- abstração
- polimorfismo
- modelagem de objetos
- reutilização de código

---

# Desafio 002

[Ver código](./Desafio002.py)

## Objetivo

Implementar o padrão Template Method utilizando bebidas quentes.

## O que foi utilizado

- Classes abstratas
- Herança
- Métodos abstratos
- Template Method

## Explicação

A classe abstrata:

```python
BebidaQuente
```

define o fluxo geral de preparo:

```python
preparar()
```

Porém delega algumas etapas para as subclasses:

```python
misturar()
```

```python
servir()
```

As classes:

- Cafe
- Leite
- Cha

personalizam apenas as etapas necessárias.

Esse desafio ajudou a compreender:

- reaproveitamento de algoritmos
- abstração
- Template Method

---

# Desafio 003

[Ver código](./Desafio003.py)

## Objetivo

Calcular fretes utilizando diferentes meios de transporte.

## O que foi utilizado

- Classes abstratas
- Herança
- Polimorfismo
- Biblioteca Rich
- Tabelas

## Explicação

Foi criada uma classe abstrata:

```python
Transporte
```

com um método obrigatório:

```python
calc_frete()
```

Cada tipo de transporte possui sua própria regra de cálculo:

- Moto
- Caminhao
- Drone

Apesar da chamada ser a mesma:

```python
calc_frete()
```

cada objeto produz um resultado diferente.

Esse desafio reforçou:

- polimorfismo
- regras específicas por classe
- abstração

---

# Desafio 004

[Ver código](./Desafio004.py)

## Objetivo

Simular o cálculo de salários para diferentes tipos de funcionários.

## O que foi utilizado

- Classes abstratas
- Herança
- Polimorfismo
- Biblioteca Rich
- Painéis

## Explicação

Foi criada uma classe abstrata:

```python
Funcionario
```

responsável por armazenar informações comuns.

As subclasses:

- FuncionarioHorista
- FuncionarioMensalista

implementam formas diferentes de calcular salários.

Após o cálculo, a classe base exibe uma análise salarial utilizando:

```python
analisar_sal()
```

Esse desafio ajudou no aprendizado de:

- herança
- polimorfismo
- compartilhamento de comportamentos
- organização orientada a objetos

---

# Desafio 005

[Ver código](./Desafio005.py)

## Objetivo

Criar um sistema simples de personagens para RPG utilizando herança e polimorfismo.

## O que foi utilizado

- Classes abstratas
- Herança
- Polimorfismo
- Listas
- Biblioteca Random

## Explicação

Foi criada uma classe abstrata:

```python
Personagem
```

contendo comportamentos compartilhados como:

```python
atacar()
```

```python
receber_dano()
```

O método:

```python
curar()
```

foi definido como abstrato.

As subclasses:

- Guerreiro
- Mago

implementam formas diferentes de recuperação de vida e utilizam golpes exclusivos.

Também foram utilizados:

```python
random.choice()
```

```python
random.randint()
```

para gerar golpes e danos aleatórios.

Esse desafio ajudou no aprendizado de:

- abstração
- herança
- polimorfismo
- modelagem de sistemas de combate
- reutilização de código

---