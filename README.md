# Informações
Projeto final referente a cadeira Construção de Compiladores I do curso de Ciência da Computação da Universidade Federal da Paraíba (UFPB) ministrada pelo professor Clauirton de Albuquerque Sierra.
### Objetivo
Construir um analisador de textos que funciona com modelos parecidos ao de um compilador, como análise de sintaxe e classificação de palavras, como isso iremos verificar se o texto está correto usando o exemplo que foi disponibilizado como molde.
### Exemplo de texto
*A autora pediu a antecipação dos efeitos da tutela. Ela requereu a anulação do ato administrativo. A autora disse que foi aprovada em todas as etapas. A autora foi considerada inapta para o cargo. Os testes realizados são ilegais. Os testes não observam as determinações. A autora juntou os documentos.*
### Dependências
O código foi escrito usando **Python 3**, e utiliza a biblioteca externa **SpaCy**.

# Relatório
## Léxico
O analisador léxico é o responsável por gerar uma tabela com os **tokens** e suas **classes gramaticais**.

Para construir a tabela usando o SpaCy que é uma biblioteca que disponibiliza um **Processamento Natural de Linguagem (NLP)** para o Português que tem uma boa acurácia, entretanto ainda existem algumas palavras que não são identificadas corretamente então elas são incluídas em uma lista de exceções para caso apareçam no texto serem corrigidas.

Usando funções da biblioteca também garantimos a separação das palavras corretamente e excluímos as **stopwords**.

## Sintático
Esse analisador a verificação da sintaxe do texto usando funções recursivas que foram construídas com base na **gramática livre de contexto** criada com base no exemplo citado anteriormente. A gramática que vamos mostrar não abrange toda a língua portuguesa, só parte dela, mas o objetivo é que a linguagem seja feita para textos parecidos com o do exemplo.

A linguagem final já sem ambiguidade e recursão a esquerda:

------------------------------
texto ->

sintagma_adverbial texto |
sentença pontuação |
sentença pontuação texto

-------------------------------

sintagma_adverbial ->

advérbio sintagma_adverbial |
advérbio |
e

------------------------------

sentença ->

sintagma_nominal sentença |
sintagma_nominal sintagma_verbal

-----------------------------

sintagma_nominal ->

sintagma_adjetival sintagma_nominal |
substantivo sintagma_nominal |
pronome sintagma_nominal |
substantivo |
pronome

-----------------------------

sintagma_adjetival ->

sintagma_adverbial adjetivo |
adjetivo sintagma_adjetival |
e

------------------------------

sintagma_verbal ->

sintagma_adverbial sintagma_verbal |
verbo sintagma_adjetival |
verbo sintagma_nominal |
verbo_auxiliar verbo |
verbo sintagma_verbal |
verbo |
e
------------------------------

## Bag of Words

Após criar a nossa tabela utilizando o analisador léxico e validar essa tabela utilizando o analisador sintático que foi feito com base na gramática livre de contexto, também fizemos o uso do bag-of-words.

O modelo <b>bag-of-words</b> é uma representação simplificada usada no <b>processamento de linguagem natural (PLN)</b> e na <b>recuperação de informações (IR)</b>. Logo, neste modelo, representamos um texto, com seus <b>n</b> conjuntos de palavras como um <b><i>bag</i></b> (multiset) de suas palavras, desconsiderando a gramática e mesmo a ordem das palavras, mas, mantendo a multiplicidade. Assim, o <b>bag-of-words</b> apenas preocupasse com a frequência que essas palavras aparecem nos textos e em que textos elas aparecem, pois, a palavra pode aparecer em <b>m</b> textos. Assim, nós criamos uma frequência para cada palavra com base em todas as outras palavras, ou seja, fazemos um somatório da aparição da palavra nos diversos textos e dividimos pelo total de palavras nos textos e sem repetição, ao final multiplicamos por 100 para encontrar a sua porcentagem de frequência.

# 
