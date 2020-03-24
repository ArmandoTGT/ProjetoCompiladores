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


*Texto &#8594; SintagmaAdverbial Texto | Sentença1 pontuação SentençasPosteriores*  
*SentençasPosteriores &#8594; Texto | ε*  
*Sentença1 &#8594; SintagmaNominal Sentença2*  
*Sentença2 &#8594; SintagmaNominal  Sentença2 | SintagmaVerbal Sentença2 | ε*  
*SintagmaNominal  &#8594; SintagmaAdjetival SintagmaNominal  | substantivo SintagmaNominal  | pronome SintagmaNominal  | substantivo | pronome*  
*SintagmaVerbal &#8594; SintagmaAdverbial SintagmaVerbal | verbo-auxiliar verbo | verbo PosteriorVerbo*  
*PosteriorVerbo &#8594; SintagmaVerbal | SintagmaAdjetival | ε*  
*SintagmaAdjetival  &#8594; SintagmaAdverbial adjetivo | adjetivo SintagmaAdjetival | ε*  
*SintagmaAdverbial &#8594; advérbio SintagmaAdverbial | advérbio | ε*  

## Bag of Words

# 
