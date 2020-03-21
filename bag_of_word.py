import sys

class BagOfWord():

    def __init__(self, textos):

        self.textos = textos

    def contador(self):

        qtd_textos = len(self.textos)
        bag = {}
        palavras = []
        count_textos = 0
        print(self.textos)
        for texto in self.textos:
            texto = texto.split(" ")

            for palavra in texto:
                if palavra not in palavras:
                    bag[palavra] = {}

                    bag[palavra]["contagem"] = [0] * qtd_textos
                    bag[palavra]["contagem"][count_textos] = 1

                    palavras.append(palavra)
                else:

                    bag[palavra]["contagem"][count_textos] += 1

                qtd_palavras = sum(bag[palavra]["contagem"])
                bag[palavra]["frequencia"] = ((1 - qtd_palavras)/qtd_textos)

            count_textos += 1

        print("\n\n\nPalavras:\n", palavras)
        print("\n\n\nBag of Words:\n", bag)
