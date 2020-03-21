import os
import sys
from lexico import lexico


if __name__ == '__main__':
    table = lexico('entrada.txt').tabela_de_tokens()

    for element in table:
        print(element)