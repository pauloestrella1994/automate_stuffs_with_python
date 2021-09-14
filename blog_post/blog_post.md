# Expressões Regulares (ReGex) com Python (Aplicações Práticas)

Expressões regulares são, por definição, notações padronizadas que representam um conjunto de dados do tipo string, em outras palavras, regex é um método formal para especificar um padrão de texto.

A maneira com a qual a expressão regular pode sintetizar um padrão de caracteres é por meio de metacaracteres, alguns deles são:

```
. ? * + ^ $ | [ ] { } ( ) \
```

### Mas e aí, qual é a importância das expressões regulares?
As regex servem, na prática, para validações de strings em formulários, para salvar dados em um banco (mantendo a consistência de dados), separar o que são dados úteis ou inúteis para a sua análise de dados, validar também se o usuáro está preenchendo campos da forma correta, capturar informações de URLs, entre outras milhares de aplicações. Aqui vamos mostrar alguns exemplos!

Imagine que dentro de um texto você precisa achar quantas vezes um sobrenome é citado, por exemplo, 'Müller'. Porém, você se depara com a seguinte situação, essa string está escrita de diversas maneiras, algumas até com erros claros de digitação, como: 'Miler', 'Miller', 'Müler', 'miller' e, por fim, 'Müller'. E se existisse uma expressão que fosse possível identificar todas esses sobrenomes? A regex abaixo consegue descrever esse padrão da seguinte forma:

```
(M|m)(i|u|ü)ll?er
```

Detalhando a espressão: Os metacaracteres '()' foram utilizados para agrupar duas letras, 'M' e 'm', usando também o '|', expressão 'or', ou seja, queremos achar palavras que comecem com a letra 'M' ou 'm'. Em sequência, agrupamos as palavras que, após o primeiro agrupamento, possuam as letras 'i', 'u' ou 'ü'. Por fim, o metacaractere '?' representa que, o caractere anterior a ele pode ou não estar incluso na palavra, aceitando, portanto, palavras com 'l' ou 'll'. 

Uma forma de você entender melhor é estudando sobre a infinidade de metacaracteres e seus significados, para isso, o [material online](https://aurelio.net/regex/guia/) do Aurélio Jargas pode ajudar! Além disso, práticar é muito importante, você pode utilizar o [RegEx Pal](https://www.regexpal.com/) para isso também!

### Usando o Python, será que consigo escrever uma expressão regular?
Com certeza! A maioria das linguagens de programação suporta o uso de regex como código, para o Python, não seria diferente. Para começar a usar regex em seus códigos python, você deve importar a biblioteca 're':

```
import re
```

E vamos de mais exemplos! Imagine que você tenha um formulário e precise que o seu usuário digite um CPF válido. Para isso, vamos pensar em algums possíveis CPFs que o usuário possa digitar. Para esse exemplo, usamos [um gerador de CPF aleatório](https://www.4devs.com.br/gerador_de_cpf)!

```
906.591.650-40
90659165040
906 591 650 40
906591.650-40
906.591650-40
```

Validando esses valores com o python ficaria algo como:

``` python
import re

CPF = input('Digite seu CPF: ')
regex = '\d{3}(\.|\s)?\d{3}(\.|\s)?\d{3}(\-|\s)?\d{2}'
validador = re.compile(regex)

if bool(validador.fullmatch(CPF)) is True:
    print('Esse é um CPF válido!')
else:
    print('Esse não é um CPF válido!')
```
Para esse exemplo, a função `fullmatch` verificar se a string inteira é válida para a regex escrita. 

Executando esse bloco de código, podemos verificar que várias possíveis maneiras de apresentar um CPF são válidas. Vejamos!

```
Digite seu CPF: 906.591.650-40
Esse é um CPF válido!
```
```
Digite seu CPF: 906591.650-40
Esse é um CPF válido!
```

Pórem, se, por algum acaso, o usuário digitar algum caractere errado, ou digitar um outro tipo de dado (por exemplo, um email) nesse campo, a regex nos auxilia pra negar essa validação!

```
Digite seu CPF: 906.59A.650-40
Esse não é um CPF válido!
```
```
Digite seu CPF: 906591.650-40812723
Esse não é um CPF válido!
```
```
Digite seu CPF: usuario@gmail.com
Esse não é um CPF válido!
```

### Achando padrões dentro de um texto
Vamos a mais um exemplo? Imagine agora que você tem um texto dentro de um email e precisa retirar apenas os números de telefone que estão contidos na mensagem, sejam eles quantos forem. Dada a mensagem abaixo:

```
'Preciso que você me ligue amanhã em um desses números: (55)55555-5555 ou (55)44444-4444. É urgente!'
```

Em python teríamos algo como:

``` python
import re

messagem = 'Preciso que você me ligue amanhã em um desses números: (55)55555-5555 ou (55)44444-4444. É urgente!'

fone_num_regex = re.compile(r'\(\d{2}\)\d{5}-\d{4}')
números_de_telefone = fone_num_regex.findall(messagem)
print(números_de_telefone)
```

A função `findall` retorna uma lista das strings encontradas, para o nosso exemplo, o retorno seria:

``` 
['(55)55555-5555', '(55)44444-4444']
```

# Conclusão
As expressões regulares podem te ajudar muito com a validação, verificação, limpagem, raspagem de dados, entre outros objetivos, sejam eles quais forem! Para entender melhor como funciona a biblioteca de expressões regulares e quais métodos ela fornece, você pode acessar a [documentação oficial](https://docs.python.org/3/library/re.html).
