import os
import sys
from lexico import lexico
from analisador_sintatico import Sintatico
from bag_of_word import BagOfWord


if __name__ == '__main__':
    table = lexico('entrada.txt').tabela_de_tokens()

    tabelas_textos = []
    tabelas_textos.append(table.copy())

    print("=====================================")
    print("Tabela Gerada pelo Analisador Léxico:")
    print("=====================================\n")
    for element in table:
        print(element)
    print("\n=====================================")

    with open("output/output_lexico.txt", "w", encoding="utf8") as output_lexico:
        for instance in table:
            output_lexico.write(str(instance)+"\n")

    print("\n\n=====================================")
    print("Validação do Analisador Sintático:")
    print("=====================================")
    Sintatico(table).texto()
    print("\n=====================================")

    textos = []
    textos.append(open("entrada.txt", 'r', encoding='utf-8').read().replace('\n',''))

    print("\n\n=====================================")
    print("Bag Of Words:")
    print("=====================================")
    BagOfWord(tabelas_textos).contador()
    print("\n=====================================")
