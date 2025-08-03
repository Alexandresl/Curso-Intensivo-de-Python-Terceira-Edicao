# Curso Intensivo de Python - Terceira Edição

**Eric Matthes**

Extração de pontos-chave, exemplos e projetos do livro

Repositório do livro:

* [https://github.com/ehmatthes/pcc_3e](https://github.com/ehmatthes/pcc_3e)
* [https://ehmatthes.github.io/pcc_3e/](https://ehmatthes.github.io/pcc_3e/)

**Sumário:**

- [Curso Intensivo de Python - Terceira Edição](#curso-intensivo-de-python---terceira-edição)
  - [Parte 1 - Noções Básicas](#parte-1---noções-básicas)
  - [Capítulo 1 - Primeiros passos](#capítulo-1---primeiros-passos)
    - [Faça você mesmo](#faça-você-mesmo)
  - [Capítulo 2 - Variáveis e tipos de dados simples](#capítulo-2---variáveis-e-tipos-de-dados-simples)
    - [Variáveis](#variáveis)
    - [Faça você mesmo](#faça-você-mesmo-1)
    - [Alterando letras maiúsculas e minúsculas em uma string](#alterando-letras-maiúsculas-e-minúsculas-em-uma-string)
    - [Usando variáveis em String](#usando-variáveis-em-string)
    - [Adicionando espaço em branco a strings com tabs ou quebras de linhas](#adicionando-espaço-em-branco-a-strings-com-tabs-ou-quebras-de-linhas)
    - [Removendo espaços em branco com strip()](#removendo-espaços-em-branco-com-strip)
    - [Removendo prefixos](#removendo-prefixos)
    - [Evitando erros de sintaxe com strings](#evitando-erros-de-sintaxe-com-strings)
    - [Faça você mesmo](#faça-você-mesmo-2)

## Parte 1 - Noções Básicas

## Capítulo 1 - Primeiros passos

[Exemplos](./capitulo_01/)

### Faça você mesmo

**1.1 python.org**: Explore a página inicial do Python ([https://www.python.org/](https://www.python.org/)) para encontrar tópicos de seu interesse. A medida que se familiarizar com o Python, diferentes partes do site serão mais proveitosas para você.

**1.2 Erros de digitação do Hello World**: Abra o arquivo *hell_world.py* que acabou de criar. Cometa de propósito um erro de digitação em algum lugar da linha e execute o programa novamente. Você consegue cometer um erro de digitação que gera um erro? Consegue entender a mensagem de erro? Consegue cometer um erro de digitação que não gere um erro? Por que você acha que não gerou erro?

**1.3 Habilidades infinitas** Caso tivesse habilidades infinitas de programação, o que você desenvolveria? Você está prestes a aprender a programar. Caso tenha um objetivo final em mente, você usará imediatamente suas habilidades; agora é um ótimo momento para descrever de forma sucinta o que você deseja criar. É um bom hábito manter um caderno de "ideias" que você possa consultar sempre que quiser começar um projeto novo. Agora, reserve alguns minutos para registrar três programas que deseja criar.

## Capítulo 2 - Variáveis e tipos de dados simples

[Exemplos](./capitulo_02/)

### Variáveis

> Usando uma variável com o *hello_world.py*. Adicione uma nova linha no início do arquivo e modifique a segunda linha.

```python:hello_world.py
message = "Hello Python world!"
print(message)
```

```python title="simple_message.py"
msg = "I love learning to use Python."
print(msg)
```

**Saída:**

```bash
Hello Python world!
```

[Código Fonte](./capitulo_02/hello_world.py)

> Podemos atribuir outro valor a variável *message*.

```python
message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course world!"
print(message)
```

**Saída:**

```bash
Hello Python world!
Hello Python Crash Course world!
```

[Código Fonte](./capitulo_02/hello_world_2.py)

### Faça você mesmo

Escreva um programa separado para cada um desses exercícios. Salve cada programa com um nome de arquivo que siga as convenções padrão do Python, usando letras minúsculas e underscores, como *simple_message.py* e *simple_messages.py*.

**2.1 Simple Message:** Atribua uma mensagem a uma variável e exiba cada mensagem.

[Solução](./capitulo_02/Exercícios/simple_message.py)

**2.2 Simple Messages:** Atribua uma mensagem a uma variável e exiba essa mensagem. Em seguida, mude o valor da variável para uma nova mensagem e mostra a nova mensagem.

[Solução](./capitulo_02/Exercícios/simple_messages.py)

### Alterando letras maiúsculas e minúsculas em uma string

> O método `title()` altera a primeira letra de cada palavra para maiúscula.

```python
name = "ada lovelace"
print(name.title())
```

Saída:

```bash
Ada Lovelace
```

[Código Fonte](./capitulo_02/name.py)

> O método `upper()` imprime todas as letras em maiúscula.
>
> O método `lower()` imprime todas as letras em minúsculas. Este método é bastante útil para armazenar dados, principalmente àqueles fornecidos por usuários, que não respeitarão uma padrão específico.

```python
# name_2.py

name = "Ada Lovelace"
print(name.upper())
print(name.lower())
```

**Saída:**

```bash
ADA LOVELACE
ada lovelace
```

[Código Fonte](./capitulo_02/name_2.py)

### Usando variáveis em String

> Usando o valor de variáveis dentro de Strings
>
> Essas strings se chamam *f-strings*. O *f* é de *formato*, pois o Python formata a string substituindo o nome de qualquer variável entre chaves por seu valor.

```python
# full_name.py

first_name = "Ada"
last_name = "lovelace"

full_name = f"{first_name} {last_name}"
print(full_name)
```

**Saída:**

```bash
ada lovelace
```

[Código Fonte](./capitulo_02/full_name.py)

> Usando *f-string* para compor mensagens completas usando as informações associadas a uma variável.

```python
# full_name_2.py

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}")
```

**Saída**

```bash
Hello, Ada Lovelace
```

> É possível também usar *f-strings* para compor uma mensagem e, em seguida, atribuir a mensagem inteira a uma variável:

```python
# full_name_3.py

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}"
print(message)
```

**Saída:**

```bash
Hello, Ada Lovelace
```

### Adicionando espaço em branco a strings com tabs ou quebras de linhas

> Para adicionar uma tabulação podemos utilizar a combinação de caracteres `\t`.

```python
print("\tPython")
```

**Saída:**

```bash
    Python
```

> Para adicionar uma quebra de linha usamos a combinação `\n`.

```python
print("Languages:\nPython\nC\nJavascript")
```

**Saída:**

```bash
Languages:
Python
C
JavaScript
```

> É possível também combinar tabulações `\t` e quebras de linha `\n`.

```python
print("Languages:\n\nPython\n\tC\n\tJavascript")
```

**Saída:**

```bash
Languages:
    Python
    C
    JavaScript
```

### Removendo espaços em branco com strip()

> A fim de garantir que não tenha nenhum espaço em branco no lado direito de uma string, use o método `rstrip()`. Conforme é possível perceber no exemplo a seguir, a função `rstrip()` não altera o valor da string na variável *favorite_language* apenas formata sua saída:

```python
favorite_language = 'python '
favorite_language # saída: 'python '

favorite_language.rstrip() # Saída: 'python'

favorite_language # saída: 'python '
```

> Para remover o espaço em branco da string de forma definitiva, é necessário associar o valor removido ao nome da variável.

```python
favorite_language = 'python '
favorite_language = favorite_language.rstrip()
favorite_language # Saída: 'python'
```

> Podemos também remover o espaço em branco do lado esquerdo de uma string com o método `lstrip()`, ou de ambos os lados ao mesmo tempo usando o `strip()`.

```python
favorite_language = ' python '
favorite_language.rstrip() # Saída: ' python'
favorite_language.lstrip() # Saída: 'python '
favorite_language.strip() # Saída: 'python'
```

### Removendo prefixos

> Uma tarefa comum quanto trabalhamos com strings é a remoção de prefixos. Por exemplo, o *`https://`* na URL de um site. Para isso, utilizamos o método `removeprefix()`.

```python
nostarch_url = 'https://nostarch.com'
nostarch_url.removeprefix('https://') # Saída: 'nostarch.com'
```

> Assim como os métodos de remover espaços em branco, o removeprefix() mantém a string original inalterada. Caso queira manter o valor com o prefixo removido, reatribua-o à variável original ou a outra variável:

```python
simple_url = nostarch_url.removeprefix('https://')
```

### Evitando erros de sintaxe com strings

> Para evitar erros de sintaxe em strings que usam apóstrofo você deverá usar aspas duplas `""`.

```python
# apostrophe.py

message = "One of Python's strengths is its diverse community."
print(message)
```

**Saída:**

```bash
One of Python's strengths is its diverse community.
```

[Código Fonte](./capitulo_02/apostrophe.py)

> Contudo, se utilizarmos aspas simples, o Python nã conseguirá identificar onde a string deve terminar.

```python
message = 'One of Python's strengths is its diverse community.'
print(message)
```

**Saída:**

```bash
File "<stdin>", line 1
    message = 'One of Python's strengths is its diverse community.'
                             ^
SyntaxError: invalid syntax
```

### Faça você mesmo

Salve cada um dos exercícios a seguir em um arquivo separado, com um nome como *mame_cases.py*. Se ficar empacado, faça um pausa ou confira as sugestões no *Apêndice C*.

**2.3 Mensagem Pessoal:** Use uma variável para representar o nome de uma pessoa e exiba uma mensagem para essa pessoa. Sua mensagem deve ser simples, como "Olá Eric", gostaria de aprender um pouco de Python hoje?"

[Solução](./capitulo_02/Exercícios/mensagem_pessoal.py)

**2.4 Maiúsculas e minúsculas:** Use uma varável para representar o nome de um apessoa e, em seguida, exiba o nome dessa pessoa em letras minúsculas, maiúsculas e as primeiras letras maiúsculas.

[Solução](./capitulo_02/Exercícios/maiusculas_minusculas.py)

**2.5 Citação famosa:** Encontre uma citação de uma pessoa famosa que você admira. Exiba a citação e o nome do autor. Sua saída deve se parecer com a seguinte, incluindo as aspas:

```text
Albert Einstein disse uma vez: "Uma pessoa que nunca cometeu um erro nunca tentou nada novo."
```

[Solução](./capitulo_02/Exercícios/citacao_famosa.py)

**2.6 Citação famosa 2:** Repita o Exercício 2.5, mas desta vez represente o nome da pessoa famosa usando uma variável chamada *famous_person*. Depois, escreva sua mensagem e a represente com uma nova variável chamada *message*. Printe sua mensagem.

[Solução](./capitulo_02/Exercícios/citacao_famosa_2.py)

**2.7 Removendo nomes:** Use uma variável para representar o nome de uma pessoa e inclua alguns caracteres de espaço em branco no início e no final do nome. Lembre-se de usar cada combinação de caracteres, "`\t`" e "`\n`", pelo menos uma vez.

Exiba o nome uma vez para o espaço em branco ao redor do nome seja mostrado. Em seguida, printe o nome usando cada uma das três funções de remoção, `lstrip()`, `rstrip()` e `strip()`.