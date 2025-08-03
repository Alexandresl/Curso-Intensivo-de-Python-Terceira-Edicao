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
    - [O que realmente ocorre quando executamos o *hello\_world.py*](#o-que-realmente-ocorre-quando-executamos-o-hello_worldpy)
    - [Variáveis](#variáveis)
    - [Faça você mesmo](#faça-você-mesmo-1)
    - [Strings](#strings)
    - [Alterando letras maiúsculas e minúsculas em uma string](#alterando-letras-maiúsculas-e-minúsculas-em-uma-string)
    - [Usando variáveis em String](#usando-variáveis-em-string)
    - [Adicionando espaço em branco a strings com tabs ou quebras de linhas](#adicionando-espaço-em-branco-a-strings-com-tabs-ou-quebras-de-linhas)
    - [Removendo espaços em branco com strip()](#removendo-espaços-em-branco-com-strip)
    - [Removendo prefixos](#removendo-prefixos)
    - [Evitando erros de sintaxe com strings](#evitando-erros-de-sintaxe-com-strings)
    - [Faça você mesmo](#faça-você-mesmo-2)
    - [Números](#números)
    - [Inteiros](#inteiros)
    - [Floats](#floats)
    - [Inteiros e floats](#inteiros-e-floats)
    - [Underscores em números](#underscores-em-números)
    - [Atribuição múltipla](#atribuição-múltipla)
    - [Constantes](#constantes)
    - [Faça você mesmo](#faça-você-mesmo-3)
    - [Como escrever comentários?](#como-escrever-comentários)
    - [Faça você mesmo](#faça-você-mesmo-4)
    - [Zen do Python](#zen-do-python)
    - [Faça você mesmo](#faça-você-mesmo-5)
  - [Capítulo 3 - Introdução às listas](#capítulo-3---introdução-às-listas)

## Parte 1 - Noções Básicas

## Capítulo 1 - Primeiros passos

[Exemplos](./capitulo_01/)

### Faça você mesmo

**1.1 python.org**: Explore a página inicial do Python ([https://www.python.org/](https://www.python.org/)) para encontrar tópicos de seu interesse. A medida que se familiarizar com o Python, diferentes partes do site serão mais proveitosas para você.

___

**1.2 Erros de digitação do Hello World**: Abra o arquivo *hell_world.py* que acabou de criar. Cometa de propósito um erro de digitação em algum lugar da linha e execute o programa novamente. Você consegue cometer um erro de digitação que gera um erro? Consegue entender a mensagem de erro? Consegue cometer um erro de digitação que não gere um erro? Por que você acha que não gerou erro?

___

**1.3 Habilidades infinitas** Caso tivesse habilidades infinitas de programação, o que você desenvolveria? Você está prestes a aprender a programar. Caso tenha um objetivo final em mente, você usará imediatamente suas habilidades; agora é um ótimo momento para descrever de forma sucinta o que você deseja criar. É um bom hábito manter um caderno de "ideias" que você possa consultar sempre que quiser começar um projeto novo. Agora, reserve alguns minutos para registrar três programas que deseja criar.

___

## Capítulo 2 - Variáveis e tipos de dados simples

[Exemplos](./capitulo_02/)

### O que realmente ocorre quando executamos o *hello_world.py*

> ___
> Ao executarmos o arquivo *hello_world.py*, o final `.py` indica que o arquivo é um programa Python. Assim, o editor passa o programa ao *interpretador Python*, que lê o programa e verifica o que cada palavra significa.
>
> [Arquivo: hello_world.py](./capitulo_02/hello_world.py)
>
> ```python
> print("Hello Python world!")
> ```
>
> **Saída:**
>
> ```bash
> Hello Python world!
> ```
>
> ___

&nbsp;

### Variáveis

> ___
> Usando uma variável com o *hello_world.py*. Adicione uma nova linha no início do arquivo e modifique a segunda linha.
>
> [Arquivo: hello_world_2.py](./capitulo_02/hello_world_2.py.py)
>
> ```python
> 
> message = "Hello Python world!"
> print(message)
> ```
>
> **Saída:**
>
>```bash
> Hello Python world!
>```
>
> ___

&nbsp;

> ___
> Podemos atribuir outro valor a variável *message*.
>
> [Arquivo: hello_world_3.py](./capitulo_02/hello_world_3.py)
>
> ```python
> message = "Hello Python world!"
> print(message)
> 
> message = "Hello Python Crash Course world!"
> print(message)
> ```
>
> **Saída:**
>
> ```bash
> Hello Python world!
> Hello Python Crash Course world!
> ```
>
> ___

### Faça você mesmo

Escreva um programa separado para cada um desses exercícios. Salve cada programa com um nome de arquivo que siga as convenções padrão do Python, usando letras minúsculas e underscores, como *simple_message.py* e *simple_messages.py*.

**2.1 Simple Message:** Atribua uma mensagem a uma variável e exiba cada mensagem.

[Solução](./capitulo_02/Exercícios/simple_message.py)

___

**2.2 Simple Messages:** Atribua uma mensagem a uma variável e exiba essa mensagem. Em seguida, mude o valor da variável para uma nova mensagem e mostra a nova mensagem.

[Solução](./capitulo_02/Exercícios/simple_messages.py)

___

### Strings

### Alterando letras maiúsculas e minúsculas em uma string

> ___
> O método `title()` altera a primeira letra de cada palavra para maiúscula.
>
> [Arquivo: name.py](./capitulo_02/name.py)
>
> ```python
> name = "ada lovelace"
> print(name.title())
> ```
>
> Saída:
>
> ```bash
> Ada Lovelace
> ```
>
> ___

&nbsp;

> ___
> O método `upper()` imprime todas as letras em maiúscula.
>
> O método `lower()` imprime todas as letras em minúsculas. Este método é bastante útil para armazenar dados, principalmente àqueles fornecidos por usuários, que não respeitarão uma padrão específico.
>
> [Arquivo: name_2.py](./capitulo_02/name_2.py)
>
> ```python
> 
> name = "Ada Lovelace"
> print(name.upper())
> print(name.lower())
> ```
>
> **Saída:**
>
> ```bash
> ADA LOVELACE
> ada lovelace
> ```
>
> ___

### Usando variáveis em String

> ___
> Usando o valor de variáveis dentro de Strings
>
> Essas strings se chamam *f-strings*. O *f* é de *formato*, pois o Python formata a string substituindo o nome de qualquer variável entre chaves por seu valor.
>
> [Arquivo: full_name.py](./capitulo_02/full_name.py)
>
> ```python
> 
> first_name = "Ada"
> last_name = "lovelace"
> 
> full_name = f"{first_name} {last_name}"
> print(full_name)
> ```
>
> **Saída:**
>
> ```bash
> ada lovelace
> ```
>
> ___

&nbsp;

> ___
> Usando *f-string* para compor mensagens completas usando as informações associadas a uma variável.
>
> [Arquivo: full_name_2.py](./capitulo_02/full_name_2.py)
>
> ```python
> first_name = "ada"
> last_name = "lovelace"
> full_name = f"{first_name} {last_name}"
> print(f"Hello, {full_name.title()}")
> ```
>
> **Saída**
>
> ```bash
> Hello, Ada Lovelace
> ```
>
> ___

&nbsp;

> ___
> É possível também usar *f-strings* para compor uma mensagem e, em seguida, atribuir a mensagem inteira a uma variável:
>
> [Arquivo: full_name_3.py]
>
> ```python
> first_name = "ada"
> last_name = "lovelace"
> full_name = f"{first_name} {last_name}"
> message = f"Hello, {full_name.title()}"
> print(message)
> ```
>
> **Saída:**
>
> ```bash
> Hello, Ada Lovelace
> ```
>
> ___

### Adicionando espaço em branco a strings com tabs ou quebras de linhas

> ___
> Para adicionar uma tabulação podemos utilizar a combinação de caracteres `\t`.
>
> ```python
> print("\tPython")
> ```
>
> **Saída:**
>
> ```bash
>   Python
> ```
>
> ___

&nbsp;

> ___
> Para adicionar uma quebra de linha usamos a combinação `\n`.
>
> ```python
> print("Languages:\nPython\nC\nJavascript")
> ```
>
> **Saída:**
>
> ```bash
> Languages:
> Python
> C
> JavaScript
> ```
>
> ___

&nbsp;

> ___
> É possível também combinar tabulações `\t` e quebras de linha `\n`.
>
> ```python
> print("Languages:\n\nPython\n\tC\n\tJavascript")
> ```
>
> **Saída:**
>
> ```bash
> Languages:
>     Python
>     C
>     JavaScript
> ```

### Removendo espaços em branco com strip()

> ___
> A fim de garantir que não tenha nenhum espaço em branco no lado direito de uma string, use o método `rstrip()`. Conforme é possível perceber no exemplo a seguir, a função `rstrip()` não altera o valor da string na variável *favorite_language* apenas formata sua saída:
>
> ```python
> favorite_language = 'python '
> favorite_language # saída: 'python '
> 
> favorite_language.rstrip() # Saída: 'python'
> 
> favorite_language # saída: 'python '
> ```
>
> ___

&nbsp;

> ___
> Para remover o espaço em branco da string de forma definitiva, é necessário associar o valor removido ao nome da variável.
>
> ```python
> favorite_language = 'python '
> favorite_language = favorite_language.rstrip()
> favorite_language # Saída: 'python'
> ```
>
> ___

&nbsp;

> ___
> Podemos também remover o espaço em branco do lado esquerdo de uma string com o método `lstrip()`, ou de ambos os lados ao mesmo tempo usando o `strip()`.
>
> ```python
> favorite_language = ' python '
> favorite_language.rstrip() # Saída: ' python'
> favorite_language.lstrip() # Saída: 'python '
> favorite_language.strip() # Saída: 'python'
> ```
>
>___

### Removendo prefixos

> ___
> Uma tarefa comum quanto trabalhamos com strings é a remoção de prefixos. Por exemplo, o *`https://`* na URL de um site. Para isso, utilizamos o método `removeprefix()`.
>
> ```python
> nostarch_url = 'https://nostarch.com'
> nostarch_url.removeprefix('https://') # Saída: 'nostarch.com'
> ```
>
> ___

&nbsp;

> ___
> Assim como os métodos de remover espaços em branco, o removeprefix() mantém a string original inalterada. Caso queira manter o valor com o prefixo removido, reatribua-o à variável original ou a outra variável:
>
> ```python
> simple_url = nostarch_url.removeprefix('https://')
> ```
>
> ___

### Evitando erros de sintaxe com strings

> ___
> Para evitar erros de sintaxe em strings que usam apóstrofo você deverá usar aspas duplas `""`.
>
> [Arquivo: apostrophe.py](./capitulo_02/apostrophe.py)
>
> ```python
> message = "One of Python's strengths is its diverse community."
> print(message)
> ```
>
> **Saída:**
>
> ```bash
> One of Python's strengths is its diverse community.
> ```
>
> ___

&nbsp;

> ___
> Contudo, se utilizarmos aspas simples, o Python nã conseguirá identificar onde a string deve terminar.
>
> ```python
> message = 'One of Python's strengths is its diverse community.'
> print(message)
> ```
>
> **Saída:**
>
> ```bash
> File "<stdin>", line 1
>     message = 'One of Python's strengths is its diverse community.'
>                              ^
> SyntaxError: invalid syntax
> ```
>
> ___

### Faça você mesmo

Salve cada um dos exercícios a seguir em um arquivo separado, com um nome como *mame_cases.py*. Se ficar empacado, faça um pausa ou confira as sugestões no *Apêndice C*.

**2.3 Mensagem Pessoal:** Use uma variável para representar o nome de uma pessoa e exiba uma mensagem para essa pessoa. Sua mensagem deve ser simples, como "Olá Eric", gostaria de aprender um pouco de Python hoje?"

[Solução](./capitulo_02/Exercícios/mensagem_pessoal.py)

___

**2.4 Maiúsculas e minúsculas:** Use uma varável para representar o nome de um apessoa e, em seguida, exiba o nome dessa pessoa em letras minúsculas, maiúsculas e as primeiras letras maiúsculas.

[Solução](./capitulo_02/Exercícios/maiusculas_minusculas.py)

___

**2.5 Citação famosa:** Encontre uma citação de uma pessoa famosa que você admira. Exiba a citação e o nome do autor. Sua saída deve se parecer com a seguinte, incluindo as aspas:

```text
Albert Einstein disse uma vez: "Uma pessoa que nunca cometeu um erro nunca tentou nada novo."
```

[Solução](./capitulo_02/Exercícios/citacao_famosa.py)

___

**2.6 Citação famosa 2:** Repita o Exercício 2.5, mas desta vez represente o nome da pessoa famosa usando uma variável chamada *famous_person*. Depois, escreva sua mensagem e a represente com uma nova variável chamada *message*. Printe sua mensagem.

[Solução](./capitulo_02/Exercícios/citacao_famosa_2.py)

___

**2.7 Removendo nomes:** Use uma variável para representar o nome de uma pessoa e inclua alguns caracteres de espaço em branco no início e no final do nome. Lembre-se de usar cada combinação de caracteres, "`\t`" e "`\n`", pelo menos uma vez.

Exiba o nome uma vez para o espaço em branco ao redor do nome seja mostrado. Em seguida, printe o nome usando cada uma das três funções de remoção, `lstrip()`, `rstrip()` e `strip()`.

[Solução](./capitulo_02/Exercícios/removendo_nomes.py)

___

**2.8 Extensões de arquivo:** O Python tem um método *removesuffix()* que funciona exatamente como *removeprefix()*. Atribua o valor *'python_notes.txt'* a uma variável chamada *filename*. Depois utilize o método *removesuffix()* para exibir o nome do arquivo sem a extensão do arquivo, como alguns navegadores de arquivos fazem.

[Solução](./capitulo_02/Exercícios/extensoes_arquivos.py)

### Números

### Inteiros

> ___
> No Python é possível somar (+), subtrair (-), multiplicar (*) e dividir (/) números inteiros
>
> ```python
> 2 + 3 # Saída: 5
> 
> 3 - 2 # Saída: 1
> 
> 2 * 3 # Saída: 6
> 
> 3 / 2 # Saída: 1.5
> ```
>
> ___

&nbsp;

> ___
> O Python usa dois símbolos de multiplicação para representar expoentes.
>
> ```python
> 3 ** 2 # Saída: 9
> 
> 3 ** 3 # Saída: 27
> 
> 10 ** 6 # Saída: 1000000
> ```
>
> ___

&nbsp;

> ___
> Python também suporta a ordem de precedência das operações. Podemos também utilizar parênteses para modificar a ordem das operações.
>
> ```python
> 2 + 3 * 4 # Saída: 14
> 
> (2 + 3) * 4 # Saída: 20
> ```
>
> ___

### Floats

> ___
> Na maioria dos casos podemos utilizar floats sem nos preocuparmos como se comportam. Basta digitar os números que quer usar, e o Python provavelmente fará o que você espera:
>
> ```python
> 0.1 + 0.1 # Saída: 0.2
> 
> 0.2 + 0.2 # Saída: 0.4
> 
> 2 * 0.1 # Saída: 0.2
> 
> 2 * 0.2 # Saída: 0.4
> ```
>
> ___

&nbsp;

> ___
> No entanto, fique atento de que às vezes você pode obter um número arbitrários de casas decimais como resposta:
>
> ```python
> 0.2 + 0.1 # Saída: 0.30000000000000004
> ```
>
> ___
>

### Inteiros e floats

> ___
> Ao realizara divisão de dois números inteiros quaisquer, mesmo que sejam inteiros que resultem em um número inteiro, sempre obteremos um float
>
> [Nome do arquivo](Caminho do arquivo)
>
> ```python
> 4 / 2 # Saída: 2.0
> ```
>
> ___

&nbsp;

> ___
> Caso misture um inteiro e um float em qualquer outra operação, você também obterá um float.
>
> ```python
> 1 + 2.0 # Saída: 3.0
> 
> 2 * 3.0 # Saída: 6.0
>
> 3.0 ** 2 # Saída: 9.0
> ```
>
> ___

### Underscores em números

> ___
> Ao escrever números grandes, é possível agrupar dígitos usando underscores para tornar os números grandes mais legíveis.
>
> ```python
> universe_age = 14_000_000_000
> print(universe_age)
> ```
>
> **Saída:**
>
> ```bash
> 14000000000
> ```
>
> ___

&nbsp;

### Atribuição múltipla

> ___
> Podemos atribuir valores a mais de uma variável usando somente uma única linha de código.
>
> ```python
> x, y, z = 0, 0, 0
> ```
>
> ___

&nbsp;

### Constantes

> ___
> Uma *constante* é uma variável cujo valor permanece o mesmo durante a vida de um programa. O Python não tem tipos de constantes built-in, mas os programadores Python usam letras maiúsculas para indicar que uma variável deve ser tratada como uma constante e nunca ser alterada.
>
> ```python
> MAX_CONNECTIONS = 5000
> ```
>
> ___

&nbsp;

### Faça você mesmo

**2.9 Número oito:** Escreva operações de adição, subtração, multiplicação e divisão que resultem cada uma no número 8. Não se esqueça de incluir suas operações um print() para conferir os resultados. Você deve criar quatro linhas mais ou menos assim:

```python
print(5 + 3)
```

Sua saída saída deve ter quatro linhas, com o número 8 aparecendo uma vaz em cada linha.

[Solução](./capitulo_02/Exercícios/numero_oito.py)

___

**2.10 Número favorito:** Use uma variável para representar seu número favorito. Em seguida, usando essa variável, crie uma mensagem que revele seu número favorito. Printe essa mensagem.

[Solução](./capitulo_02/Exercícios/numero_favorito.py)

### Como escrever comentários?

> ___
> Em Python, a marca de hash (`#`) indica um comentário.
>
> [Arquivo](./capitulo_02/Exercícios/comment.py)
>
> ```python
> # Diga olá a todos
> print("Hello Python people!")
> ```
>
> **Saída:**
>
> ```bash
> Hello Python people!
> ```
>
> ___

&nbsp;

### Faça você mesmo

**2.11 Adicionando comentários:** Escolha dois dos programas que você escreveu e adicione pelo menos um comentário a cada um. Caso não tenha nada específico para escrever porque até agora seus programas são muito simples, basta acrescentar seu nome e a data atual no início de cada arquivo do programa. Em seguida, escreva uma frase descrevendo o que o programa faz.

[Solução 1](./capitulo_02/Exercícios/citacao_famosa.py)

[Solução 2](./capitulo_02/Exercícios/extensoes_arquivos.py)

### Zen do Python

Programadores Python experientes o incentivarão a evitar a complexidade e buscar a simplicidade sempre que possível. A filosofia da comunidade Python está no "Zen do Python" de **Tim Petters**. Você pode acessar esse breve conjunto de princípios para escrever um bom código Python digitando `import this` em seu interpretador.

```text
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

Tradução em português

```text
O Zen do Python, por Tim Peters

Bonito é melhor que feio.
Explícito é melhor que implícito.
Simples é melhor que complexo.
Complexo é melhor que complicado.
Linear é melhor do que aninhado.
Esparso é melhor que denso.
Legibilidade conta.
Casos especiais não são especiais o bastante para quebrar as regras.
Ainda que praticidade vença a pureza.
Erros nunca devem passar silenciosamente.
A menos que sejam explicitamente silenciados.
Diante da ambiguidade, recuse a tentação de adivinhar.
Dever haver um — e preferencialmente apenas um — modo óbvio para fazer algo.
Embora esse modo possa não ser óbvio a princípio a menos que você seja holandês.
Agora é melhor que nunca.
Apesar de que nunca normalmente é melhor do que *exatamente* agora
Se a implementação é difícil de explicar, é uma má ideia
Se a implementação é fácil de explicar, pode ser uma boa ideia
Namespaces são uma grande ideia -- vamos ter mais dessas!
```

### Faça você mesmo

**2.12 Zen do Python** Digite `import this` em uma sessão do terminal Python e leia rapidamente os princípios adicionais.

___

## Capítulo 3 - Introdução às listas