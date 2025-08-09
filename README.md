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
    - [O que é uma lista?](#o-que-é-uma-lista)
    - [Acessando os elementos em uma lista](#acessando-os-elementos-em-uma-lista)
    - [As posições do índice começam em 0, não em 1](#as-posições-do-índice-começam-em-0-não-em-1)
    - [Usando valores individuais de uma lista](#usando-valores-individuais-de-uma-lista)
    - [Faça você mesmo](#faça-você-mesmo-6)
    - [Modificando elementos em uma lista](#modificando-elementos-em-uma-lista)
    - [Anexando elementos ao final de uma lista](#anexando-elementos-ao-final-de-uma-lista)
    - [Inserindo elementos em uma lista](#inserindo-elementos-em-uma-lista)
    - [Removendo elementos usando na instrução del](#removendo-elementos-usando-na-instrução-del)
    - [Removendo um elemento com o método pop()](#removendo-um-elemento-com-o-método-pop)
    - [Removendo elementos de qualquer posição em uma lista](#removendo-elementos-de-qualquer-posição-em-uma-lista)
    - [Removendo um elemento por valor](#removendo-um-elemento-por-valor)
    - [Faça você mesmo](#faça-você-mesmo-7)
    - [Ordenando uma lista permanentemente com o método `sort()`](#ordenando-uma-lista-permanentemente-com-o-método-sort)
    - [Ordenando uma lista temporariamente com a função `sorted()`](#ordenando-uma-lista-temporariamente-com-a-função-sorted)
    - [Exibindo uma lista em ordem inversa](#exibindo-uma-lista-em-ordem-inversa)
    - [Identificando o tamanho da lista](#identificando-o-tamanho-da-lista)
    - [Faça você mesmo](#faça-você-mesmo-8)
    - [Evitando erros de índice ao trabalhar com listas](#evitando-erros-de-índice-ao-trabalhar-com-listas)
    - [Faça você mesmo](#faça-você-mesmo-9)

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

### O que é uma lista?

> ___
> Uma lista é uma coleção de itens em uma ordem específica. Os itens de uma lista não precisam estar relacionados de nenhuma forma especial.
>
> Via de regra, como as listas irão conter mais de um elemento, é uma boa ideia nomeá-las no plural.
>
> No Python, *colchetes* (`[]`) designam uma lista, e os elementos individualmente são separados por vírgulas.
>
> [Arquivo: bicycles.py](./capitulo_03/bicyles.py)
>
> ```python
> bicycles = ['trek', 'cannondale', 'redline', 'specialized']
> print(bicycles)
> ```
>
> **Saída:**
>
> ```bash
> ['trek', 'cannondale', 'redline', 'specialized']
> ```
>
> ___

&nbsp;

### Acessando os elementos em uma lista

> ___
> Listas são coleções ordenadas, ou seja, podemos acessar qualquer elemento em uma lista informando a posição ou *índice* do item desejado ao Python. Para acessar um elemento em uma lista, escreva o nome dela seguido do índice do item entre colchetes.
>
> [Arquivo: bicycles_2.py](./capitulo_03/bicycles_2.py)
>
> ```python
> bicycles = ['trek', 'cannondale', 'redline', 'specialized']
> print(bicycles[0])
> ```
>
> **Saída:**
>
> ```bash
> trek
> ```
>
> ___

&nbsp;

> ___
> Podemos utilizar os métodos string em qualquer elemento da lista. Por exemplo, podemos formatar o elemento 'trek' para parecer mais apresentável usando o método `title()`.
>
> [Arquivo: bicycles_3.py](./capitulo_03/bicycles_3.py)
>
> ```python
> bicycles = ['trek', 'cannondale', 'redline', 'specialized']
> print(bicycles[0].title())
> ```
>
> **Saída:**
>
> ```bash
> Trek
> ```
>
> ___

&nbsp;

### As posições do índice começam em 0, não em 1

> ___
> O Python considera que o primeiro item de uma lista está na posição 0. Assim, podemos acessar qualquer elemento de uma lista subtraindo um da sua posição na lista.
>
> O código a seguir consulta as bicicletas nos índices 1 e 3.
>
> [Arquivo: bicycles_4.py](./capitulo_03/bicycles_4.py)
>
> ```python
> bicycles = ['trek', 'cannondale', 'redline', 'specialized']
> print(bicycles[1])
> print(bicycles[3])
> ```
>
> **Saída:**
>
> ```bash
> cannondale
> specialized
> ```
>
> ___

&nbsp;

> ___
> O Python tem uma sintaxe singular para acessar o último elemento de uma lista. Se pedirmos o elemento no índice -1, sempre retorno o último elemento da lista.
>
> [Arquivo: bicycles_5.py](./capitulo_03/bicycles_5.py)
>
> ```python
> bicycles = ['trek', 'cannondale', 'redline', 'specialized']
> print(bicycles[-1])
> ```
>
> **Saída:**
>
> ```bash
> specialized
> ```
>
> Essa sintaxe é prática, pois muitas vezes queremos acessar o último item de uma lista sem saber exatamente qual é o tamanho dela. Essa convenção se aplica também aos outros elementos. O índice -2 retorna o segundo elemento do final da lista, etc.
> ___

&nbsp;

### Usando valores individuais de uma lista

> ___
> Você pode utilizar *f-string* para criar uma mensagem com base em um valor de uma lista.
>
> Vamos tentar acessar a primeira bicicleta da lista e compor uma mensagem utilizando este valor:
>
> ```python
> bicycles = ['trek', 'cannondale', 'redline', 'specialized']
> message = f"My first bicycle was a {bicycles[0].title()}."
> print(message)
> ```
>
> **Saída:**
>
> ```bash
> My first bicycle was a Trek.
> ```
>
> ___

&nbsp;

### Faça você mesmo

Tente criar os seguintes programas curso a fim de adquirir um pouco de experiência pessoal com as listas do Python. Talvez você queira criar uma nova pasta para os exercícios de cada capítulo, assim pode mantê-los organizados.

**3.1 Nomes:** Armazene o nome de alguns de seus amigos em uma lista chamada *names*. Exiba o nome de cada pessoa acessando cada elemento da lista, um de cada vez.

[Solução](./capitulo_03/Exercícios/nomes.py)

___

**3.2 Cumprimentos:** Comece com a lista usada no Exercício 3.1, mas em vez de apenas exibir o nome de cada pessoa, exiba também uma mensagem para elas. O texto de cada mensagem deve ser o mesmo, porém, cada mensagem deve ser personalizada com o nome de cada pessoa.

[Solução](./capitulo_03/Exercícios/cumprimentos.py)

___

**3.3 Sua própria lista:** Pense em seu meio de transporte favorito, como uma moto ou um carro, e crie uma lista que armazene diversos exemplos. Use sua lista para exibir uma série de declarações sobre esses itens, como "Gostaria de ter uma moto da Honda".

[Solução](./capitulo_03/Exercícios/sua_propria_lista.py)

___

### Modificando elementos em uma lista

> ___
> A sintaxe para modificar um elemento se assemelha à sintaxe para acessar um elemento em uma lista. Para alterar um elemento, use o nome da lista seguido pelo índice do elemento que queira alterar e forneça o valor novo que quer que esse elemento tenha.
>
> [motorcycles.py](./capitulo_03/motorcycles.py)
>
> ```python
> motorcycles = ['Honda', 'Yamaha', 'Suzuki']
> print(motorcycles)
> 
> motorcycles[0] = 'Ducati'
> print(motorcycles)
> ```
>
> **Saída:**
>
> ```bash
> ['Honda', 'Yamaha', 'Suzuki']
> ['Ducati', 'Yamaha', 'Suzuki']
> ```
>
> ___

&nbsp;

### Anexando elementos ao final de uma lista

> ___
> A forma mais simples de adicionar um elemento novo a uma lista é *anexar* o elemento nela. Ao anexar um elemento a uma lista, esse elemento novo é adicionado ao final dela. Usando a mesma lista do exemplo anterior, adicionaremos o elemento novo '*Ducati*' ao final dela
>
> [motorcycles_2.py](./capitulo_03/motorcycles_2.py)
>
> ```python
> motorcycles = ['Honda', 'Yamaha', 'Suzuki']
> print(motorcycles)
> 
> motorcycles.append('Ducati')
> print(motorcycles)
> ```
>
> **Saída:**
>
> ```bash
> ['Honda', 'Yamaha', 'Suzuki']
> ['Honda', 'Yamaha', 'Suzuki', 'Ducati']
> ```
>
> ___

&nbsp;

> ___
> Com o método `append()` também é possível criar listas dinamicamente. Por exemplo, é possível começar com uma lista vazia e depois adicionar elementos nela usando uma série de métodos `append()`. Em uma lista vazia adicionaremos os elementos 'Honda', 'Yamaha' e 'Suzuki' nela.
>
> [motorcycles_3.py](./capitulo_03/motorcycles_3.py)
>
> ```python
> motorcycles = []
> 
> motorcycles.append('Honda')
> motorcycles.append('Yamaha')
> motorcycles.append('Suzuki')
> 
> print(motorcycles)
> ```
>
> **Saída:**
>
> ```bash
> ['Honda', 'Yamaha', 'Suzuki']
> ```
>
> ___

&nbsp;

### Inserindo elementos em uma lista

> ___
> Podemos adicionar um elemento novo em qualquer posição em sua lista usando o método `insert()`. Faremos isso especificando o índice do elemento novo e o valor do elemento novo.
>
> [motorcycles_4.py](./capitulo_03/motorcycles_4.py)
>
> ```python
> motorcycles = ['Honda', 'Yamaha', 'Suzuki']
> motorcycles.insert(0, 'Ducati')
> 
> print(motorcycles)
> ```
>
> **Saída:**
>
> ```bash
> ['Ducati', 'Honda', 'Yamaha', 'Suzuki']
> ```
>
> ___

&nbsp;

### Removendo elementos usando na instrução del

> ___
> Caso saiba a posição do elemento que deseja remover de uma lista, você pode usar a instrução `del`.
>
> [motorcycles_5.py](./capitulo_03/motorcycles_5.py)
>
> ```python
> motorcycles = ['Honda', 'Yamaha', 'Suzuki']
> print(motorcycles)
> 
> del motorcycles[0]
> print(motorcycles)
> ```
>
> **Saída:**
>
> ```bash
> ['Honda', 'Yamaha', 'Suzuki']
> ['Yamaha', 'Suzuki']
> ```
>
> **Obs.**: Não podemos mais acessar o valor que foi removido da lista após usarmos a instrução `del`.
> ___

&nbsp;

### Removendo um elemento com o método pop()

> ___
> O método `pop()` remove o último elemento de uma lista, mas possibilita que você trabalhe com esse elemento após removê-lo. O termo *pop* se origina da ideia de considerar uma lista como uma pilha de itens, removendo um item do topo da pilha. Analogicamente, o topo de uma pilha corresponde ao final de uma lista.
>
> [motorcycles_6.py](./capitulo_03/motorcycles_6.py)
>
> ```python
> motorcycles = ['Honda', 'Yamaha', 'Suzuki']
> print(motorcycles)
> 
> popped_motorcycles = motorcycles.pop()
> print(motorcycles)
> print(popped_motorcycles)
> ```
>
> **Saída:**
>
> ```bash
> ['Honda', 'Yamaha', 'Suzuki']
> ['Honda', 'Yamaha']
> Suzuki
> ```
>
> ___

&nbsp;

### Removendo elementos de qualquer posição em uma lista

> ___
> É possível usar o `pop()`para remover um elemento de qualquer posição em uma lista, incluindo o índice do elemento que queira remover entre parênteses.
>
> [motorcycles_7.py](./capitulo_03/motorcycles_7.py)
>
> ```python
> motorcycles = ['Honda', 'Yamaha', 'Suzuki']
> 
> first_owned = motorcycles.pop(0)
> print(f"The first motorcycle I owned was a {first_owned.title()}.")
> ```
>
> **Saída:**
>
> ```bash
> The first motorcycle I owned was a Honda.
> ```
>
> ___

&nbsp;

### Removendo um elemento por valor

> ___
> Em alguns casos não sabemos a posição do valor que queremos remover de uma lista. Se souber apenas o valor do elemento que quer remover, é possível usar o método `remove()`.
>
> [motorcycles_8.py](./capitulo_03/motorcycles_8.py)
>
> ```python
> motorcycles = ['Honda', 'Yamaha', 'Suzuki', 'Ducati']
> print(motorcycles)
> 
> motorcycles.remove('Ducati')
> print(motorcycles)
> ```
>
> **Saída:**
>
> ```bash
> ['Honda', 'Yamaha', 'Suzuki', 'Ducati']
> ['Honda', 'Yamaha', 'Suzuki']
> ```
>
> ___

&nbsp;

> ___
> Podemos também utilizar o método `remove()` para trabalhar com um valor que está sendo removido de uma lista. Removeremos o valor 'Ducati' e exibiremos a justificativa para removê-lo da lista:
>
> [motorcycles_9.py](./capitulo_03/motorcycles_9.py)
>
> ```python
> motorcycles = ['Honda', 'Yamaha', 'Suzuki', 'Ducati']
> print(motorcycles)
> 
> too_expensive = 'Ducati'
> motorcycles.remove(too_expensive)
> print(motorcycles)
> print(f"\nA {too_expensive.title()} is too expensive for me.")
> ```
>
> **Saída:**
>
> ```bash
> ['Honda', 'Yamaha', 'Suzuki', 'Ducati']
> ['Honda', 'Yamaha', 'Suzuki']
> 
> A Ducati is too expensive for me.
> ```
>
> ___
> **Obs.:** *O método `remove()` deleta somente a primeira ocorrência do valor especificado. Se existir a possibilidade de o valor aparecer mais de uma vez na lista, é necessário usar um loop a fim de garantir que todas as ocorrências do valor sejam removidas. Aprenderemos como fazer iso no Capítulo 7.*
> ___

&nbsp;

### Faça você mesmo

Os exercícios seguintes são uma pouco mais complexos do que os do Capítulo 2, mas lhe possibilitam usar as listas de todas as formas descritas.

**3.4 Lista de convidados:** Se pudesse convidar qualquer pessoa, viva ou falecida, para um jantar, quem você convidaria? Crie uma lista que tenha pelo menos três pessoas que gostaria de convidar para um jantar. em seguida, use sua lista a fim de exibir uma mensagem para cada pessoa, convidando-a para o jantar.

[Solução](./capitulo_03/Exercícios/lista_de_convidados.py)

___

**3.5 Mudando a lista de convidados:** Você acabou de ficar sabendo que um dos convidados não conseguirá ir ao jantar, assim precisa enviar um conjunto novo de convites. É necessário convidar outra pessoa.

* Comece com o programa do Exercício 3.4. No final do programa, adicione um `print()`, informando o nome do convidado que não rá ao jantar.
* Modifique sua lista substituindo o nome do convidado que não pode comparecer pelo nome da pessoa nova que você está convidando.
* Exiba um segundo conjunto de mensagens de convite, uma para cada pessoa que ainda não consta em sua lista.

[Solução](./capitulo_03/Exercícios/mudando_a_lista_de_convidados.py)

___

**3.6 Mais convidados:** Você acabou de encontrar uma mesa maior de jantar, agora há mais espaço disponível. Convide mais três pessoas para o jantar.

* Comece com o programa do Exercício 3.4 ou 3.5. No final do programa, adicione um `print()`, informando às pessoas que encontrou uma mesa maior.
* Use um `insert()` para adicionar um convidado novo ao início de sua lista.
* Use um `insert()` para adicionar um convidado novo no meio da sua lista.
* Use um `append()` para adicionar um convidado novo no final de sua lista.
* Exiba um conjunto novo de mensagens de convite, um para cada pessoa em sua lista.

[Solução](./capitulo_03/Exercícios/mais_convidados.py)

___

**3.7 Reduzindo a lista de convidados** Você acabou de descobrir que sua mesa nova de jantar não chegará a tempo e agora tem espaço somente para dois convidados.

* Comece com o programa do exercício 3.6. Adiciona uma linha nova que exiba uma mensagem que você pode convidar apenas duas pessoas para o jantar.
* Use o `pop()` para remover convidados de sua lista, um de cada vez, até que restem somente dois nomes nela. Sempre que remover um nome de sua lista, exiba uma mensagem para essa pessoa informando que lamenta por não poder convidar para o jantar.
* Exiba uma mensagem para cada uma das duas pessoas que ainda estão na sua lista, informando que ainda estão convidadas.
* Use o `del` para remover os dois últimos nomes de sua lista, para que ela fique vazia. Exiba sua lista para ter certeza de que você realmente tem uma lista vazia no final do seu programa.

[Solução](./capitulo_03/Exercícios/reduzindo_a_lista_de_convidados.py)

### Ordenando uma lista permanentemente com o método `sort()`

> ___
> O método `sort()`do Python facilita relativamente a ordenação de uma lista. Imagine que temos uma lista de carros e queremos mudar sua ordem para armazena-los em ordem alfabética. Simplificando as coisas: vamos supor que todos os valores da lista estejam em letras minúsculas.
>
> [cars.py](./capitulo_03/Exercícios/cars.py)
>
> ```python
> cars = ['bmw', 'audi', 'toyota', 'subaru']
> cars.sort()
> print(cars)
> ```
>
> **Saída:**
>
> ```bash
> ['audi', 'bmw', 'subaru', 'toyota']
> ```
>
> O método `sort()` altera **permanentemente** a ordem da lista. Agora, os carros estão em ordem alfabética, e nunca poderemos reverter para a ordem original
>
> ___

&nbsp;

___

> ___
> Podemos também ordenar essa lista em ordem alfabética reversa passando o argumento `reverse=True` para o método `sort()`. O exemplo a seguir ordena a lista de carros em ordem alfabética reversa:
>
> [cars_2.py](./capitulo_03/Exercícios/cars_2.py)
>
> ```python
> cars = ['bmw', 'audi', 'toyota', 'subaru']
> cars.sort(reverse=True)
> print(cars)
> ```
>
> **Saída:**
>
> ```bash
> ['toyota', 'subaru', 'bmw', 'audi']
> ```
>
> ___

&nbsp;

### Ordenando uma lista temporariamente com a função `sorted()`

> ___
> A fim de conservar a ordem original de uma lista, mas apresentá-la em ordem ordenada, podemos utilizar a função `sorted()`. A função `sorted()` possibilita exibir sua lista em uma ordem específica, porém, não afeta a ordem original da lista.
>
> [cars_3.py](./capitulo_03/Exercícios/cars_3.py)
>
> ```python
> cars = ['bmw', 'audi', 'toyota', 'subaru']
> 
> print('Here is the original list:')
> print(cars)
> 
> print('\nHere is the sorted list:')
> print(sorted(cars))
> 
> print('\nHere is the original list again:')
> print(cars)
> ```
>
> **Saída:**
>
> ```bash
> Here is the original list:
> ['bmw', 'audi', 'toyota', 'subaru']
> 
> Here is the sorted list:
> ['audi', 'bmw', 'subaru', 'toyota']
> 
> Here is the original list again:
> ['bmw', 'audi', 'toyota', 'subaru']
> ```
>
> A função `sorted()` também pode aceitar um argumento `reverse=True` caso queira exibir uma lista em ordem alfabética reversa.
>
> ___

&nbsp;

> [!note]
> Ordenar uma lista em ordem alfabética é um pouco mais complicado quando todos os valores não estão em letras minúsculas. Ao definir uma sequência de ordenação, temos diversas formas de interpretar letras maiúsculas. No entanto, especificar a ordem exata pode ser mais complexo do que queremos lidar neste momento. Apesar disso, a maioria das abordagens de ordenação terá como base o que você aprendeu nesta seção.

### Exibindo uma lista em ordem inversa

> ___
> Para reverter a ordem original de uma lista, podemos utilizar o método `reverse()`. Originalmente, se armazenamos a lista de carros na ordem cronológica de compra, poderíamos facilmente reordenar a lista em ordem cronológica inversa.
>
> [cars_4.py](./capitulo_03/Exercícios/cars_4.py)
>
> ```python
> cars = ['bmw', 'audi', 'toyota', 'subaru']
> print(cars)
> 
> cars.reverse()
> print(cars)
> ```
>
> **Saída:**
>
> ```bash
> ['bmw', 'audi', 'toyota', 'subaru']
> ['subaru', 'toyota', 'audi', 'bmw']
> ```
>
> ___

&nbsp;

### Identificando o tamanho da lista

> ___
> É possível encontrar rapidamente o tamanho de uma lista usando a função `len()`. Neste exemplo, a lista tem quatro elementos, logo seu tamanho é 4.
>
> [cars_5.py](./capitulo_03/Exercícios/cars_5.py)
>
> ```python
> cars = ['bmw', 'audi', 'toyota', 'subaru']
> print(len(cars))
> ```
>
> **Saída:**
>
> ```bash
> 4
> ```
>
> ___

&nbsp;

> [!Note]
> O Python calcula os itens em uma lista começando com um. Logo, você não deve se deparar com nenhum erro ao definir o tamanho de uma lista.

### Faça você mesmo

**3.8 Conhecendo o mundo:** Pense em pelo menos cinco lugares do mundo que você gostaria de conhecer.

* Armazene esses locais em uma lista. Verifique se ela não está em ordem alfabética.
* Exiba sua lista na ordem original. Não se preocupe em exibir a lista ordenadamente; basta exibi-la como uma lista crua do Python.
* Use `sorted()` para exibir sua lista em ordem alfabética, sem alterar a lista original.
* Mostre que sua lista ainda está na ordem original exibindo-a.
* Use o `sorted()` para exibir sua lista em ordem alfabética reversa, sem alterar a ordem original dela.
* Demonstre que sua lista ainda está na ordem original exibindo-a mais uma vez.
* Use o `reverse()` para alterar a ordem de sua lista. Exiba essa lista para mostrar que sua ordem foi alterada.
* Use o `reverse()` para alterar a ordem de sua lista novamente. Exiba-a a fim de mostrar que voltou à ordem original.
* Use a `sort()` para alterar sua lista para que ela seja armazenada em ordem alfabética. Exiba a lista para mostrar que sua ordem foi alterada.
* Use a `sort()` para alterar sua lista, de modo que ela seja armazenada em ordem alfabética inversa. Exiba a lista para mostrar que sua ordem foi alterada.

[Solução](./capitulo_03/Exercícios/conhecendo_o_mundo.py)
___

**3.9 Convidados para o jantar:** Recorra a um dos programas dos exercícios 3.4 a 3.7, e use `len()` para exibir uma mensagem indicando o número de pessoas que você está convidando para o jantar.

[Solução](./capitulo_03/Exercícios/convidados_para_o_jantar.py)

___

**3.10 Funções** Pense em coisas que você conseguiria armazenar em uma lista. Por exemplo, você pode criar uma lista de montanhas, rios, países, cidades, idiomas, ou qualquer outra coisa que quiser. Crie um programa com uma lista contendo esses itens e, em seguida, use cada função apresentada neste capítulo, pelo menos, uma vez.

> [!Note]
> *Resumo das funções:*
> 
> * `lista[índice]` - Não exatamente uma função mais serve para acessarmos um item da lista;
> * `lista[índice] = valor` - usado para modificar um elemento da lista;
> * `lista.append('valor')` - adiciona um novo elemento ao final da lista. serve também para criarmos uma lista dinamicamente, caso tenhamos uma lista vazia;
> * `lista.insert(posição, valor)` - insere um elemento na lista em uma posição específica. O elemento que ocupa a posição e os seguintes são deslocados para a "direita";
> * `del lista[posição]` - remove um elemento da lista. Utilizado quando sabemos o seu índice (posição);
> * `elemento_excluído = lista.pop(índice)` - remove um elemento da lista retornando o seu valor. Seu comportamento padrão, quando não informado o índice é de remover o último elemento;
> * `lista.remove(valor)` - remove um elemento por seu valor;
> * `lista.sort()` - ordena a lista por ordem alfabética. pode ser usado o `reverse=True` para ordem alfabética reversa. **Altera permanentemente a lista**;
> * `sorted(cars)` - ordena a lista por ordem alfabética. pode ser usado o `reverse=True` para ordem alfabética reversa. **conserva a lista original**;
> * `lista.reverse()` - reverte a ordem original dos elementos de uma lista. **Altera permanentemente a lista**;
> * `len(lista)` - Retorna o tamanha da lista

[Solução](./capitulo_03/Exercícios/funcoes.py)

### Evitando erros de índice ao trabalhar com listas

> ___
> Quando trabalhamos com listas pela primeira vez, podemos cometer um tipo de erro comum. Digamos que você tenha uma lista com três elementos e tente acessar um quarto item:
>
> [motorcycles_10.py](./capitulo_03/motorcycles_10.py)
>
> ```python
> motorcycles = ['Honda', 'Yamaha', 'Suzuki']
> print(motorcycles[3])
> ```
>
> Esse exemplo gera um erro de *índice*
>
> **Saída:**
>
> ```bash
> Traceback (most recent call last):
>   File "f:\Curso-Intensivo-de-Python-Terceira-Edicao\capitulo_03\motorcycles_10.py", line 2, in <module>
>     print(motorcycles[3])
>           ~~~~~~~~~~~^^^
> IndexError: list index out of range
> ```
>
> O Python tenta acessar o elemento no índice 3. Mas quando pesquisa na lista, nenhum elemento de *motorcycles* tem índice 3. Devido à natureza **off-by-one** da indexação em listas, temos aqui um típico erro. As pessoas costumam achar que o terceiro elemento é o elemento de número 3, pois começam a contar a partir de 1. Só que em Python o terceiro elemento é o número 2, porque a indexação começa a partir de 0.
>
> Caso um erro de índice aconteça em seu programa, tente ajustar o índice que voc|ê está querendo acessar em uym elemento. ?Depois, execute o programa mais uma vez para ver se os resultados estão corretos.
>
> **Lembre-se:** sempre que quiser acessar o último elemento de uma lista, use o índice *-1*. Funcionará mesmo que sua lista tenha mudado de tamanho. **O único momento que essa abordagem causará erro é quando tentarmos acessar o último elemento de uma lista vazia**
>
> ___

### Faça você mesmo

**3.11 Erro intencional:** Se você ainda não recebeu um erro de índice em um de seus programas, tente gerar um. Mude um índice em um de seus programas para gerar um erro de índice. Faça questão de corrigir o erro antes de fechar o programa.

[Solução](./capitulo_03/motorcycles_10.py)