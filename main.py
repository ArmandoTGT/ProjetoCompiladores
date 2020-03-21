import os
import sys
from lexico import lexico
from analisador_sintatico import Sintatico
from bag_of_word import BagOfWord


if __name__ == '__main__':
    table = lexico('entrada.txt').tabela_de_tokens()

    print(table)
    for element in table:
        print(element)

    with open("output/output_lexico.txt", "w", encoding="utf8") as output_lexico:
        for instance in table:
            output_lexico.write(str(instance)+"\n")

    Sintatico(table).texto()

    textos = []
    textos.append(open("entrada.txt", 'r', encoding='utf-8').read().replace('\n',''))
    BagOfWord(textos).contador()
