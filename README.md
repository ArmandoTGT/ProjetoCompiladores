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

sintagma_verbal sintagma_adjetival |
sintagma_verbal sintagma_nominal |
sintagma_adverbial sintagma_verbal |
verbo_auxiliar verbo |
verbo sintagma_verbal |
verbo |
e


## Bag of Words

# 
