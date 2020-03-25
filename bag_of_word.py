import sys
import json

class BagOfWord():

    def __init__(self, textos):

        self.textos = textos

    def contador(self):

        qtd_textos = len(self.textos)
        bag = {}
        palavras = []
        count_textos = 0

        print("\n--------------------------------------")
        print("=====================================")
        print("Texto Completo:")
        print("=====================================")
        print(self.textos)
        print("--------------------------------------")

        for texto in self.textos:

            for palavra in texto:
                palavra = palavra['token']
                if palavra not in palavras:
                    bag[palavra] = {}

                    bag[palavra]["contagem"] = [0] * qtd_textos
                    bag[palavra]["contagem"][count_textos] = 1

                    palavras.append(palavra)
                else:

                    bag[palavra]["contagem"][count_textos] += 1

            count_textos += 1

        for palavra in palavras:

            total_palavras = len(palavras)
            qtd_palavra = sum(bag[palavra]["contagem"])

            bag[palavra]["frequencia"] = ((qtd_palavra)/total_palavras) * 100
            bag[palavra]["frequencia"] = str("{:.2f}".format(bag[palavra]["frequencia"])) + "%"

        print("\n--------------------------------------")
        print("=====================================")
        print("Palavras Presentes no Texto:")
        print("=====================================")
        print(palavras)
        print("--------------------------------------")

        print("\n--------------------------------------")
        print("=====================================")
        print("Resultado Final:")
        print("=====================================\n")
        print(json.dumps(bag, indent=4, ensure_ascii=False))
        print("--------------------------------------\n")
