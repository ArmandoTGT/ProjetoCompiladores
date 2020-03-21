import sys

class Sintatico():

    def __init__(self, output_lexico):
        self.output_lexico = output_lexico

        self.token_atual = self.output_lexico[0]['token']
        self.class_atual = self.output_lexico[0]['class']
        print("\n\nAtual:", self.output_lexico[0])

        del self.output_lexico[0]

        self.sentenca = ['NOUN', 'PRON', 'ADJ']
        self.verbal = ['ADV', "VERB", "AUX"]

    #Função que determina o atual elemento sendo analisado
    def __atualiza_token(self):

        try:
            print("Atual:", self.output_lexico[0])
            self.token_atual = self.output_lexico[0]['token']
            self.class_atual = self.output_lexico[0]['class']
            del self.output_lexico[0]

        except Exception as error:
            print("Error:", error)
            self.token_atual = ""
            self.class_atual = ""

    #A Função texto é o inicio da análise, consideramos tudo texto e depois vamos destrinchando
    def texto(self):
        print("Texto")

        #Verificamos se é um adverbio
        if (self.class_atual == "ADV"):
            #Vamos verificar se existem outros advérbios
            self.__sintagma_adverbial()

            self.texto()

        #Caso não seja um advérbio ele precisa ser uma sentença
        elif (self.class_atual in self.sentenca):
            self.__sentenca()
            print(self.class_atual)

            if (self.class_atual == "SYM"):
                self.__atualiza_token()

            if (self.class_atual == "PUNCT"):
                self.__atualiza_token()

                if (self.class_atual != ""):
                    self.texto()
            else:

                print("Falta pontuação na sentença!")
                sys.exit(0)

    #Função que valida a sequencia adverbial
    def __sintagma_adverbial(self):
        print("Sintagma Adverbial")

        if (self.class_atual == "ADV"):

            #Atualizamos o valor e vamos verificar se o próximo também é Advérbio
            self.__atualiza_token()

            self.__sintagma_adverbial()

    def __sentenca(self):
        print("Sentença")

        self.__sintagma_nominal()

        if (self.class_atual in self.sentenca):

            self.__sentenca()

        elif (self.class_atual in self.verbal):

            self.__sintagma_verbal()

            self.__sintagma_nominal()

    def __sintagma_nominal(self):
        print("Sintagma Nominal")

        if (self.class_atual == "ADJ"):

            self.__sintagma_adjetival()

            self.__sintagma_nominal()


        elif (self.class_atual == "NOUN"):

            self.__atualiza_token()

            self.__sintagma_nominal()

        elif (self.class_atual == "PRON"):

            self.__atualiza_token()

            self.__sintagma_nominal()

    def __sintagma_adjetival(self):
        print("Sintagma Adjetival")

        #Verificamos se é um adjetivo
        if (self.class_atual == "ADJ"):

            self.__atualiza_token()

            self.__sintagma_adjetival()

        #Verificamos se é um adverbio
        elif (self.class_atual == "ADV"):

            self.__sintagma_adverbial()

            if (self.class_atual == "PRON"):

                self.__atualiza_token()
                return

            else:

                print("Advérbio não possuí um adjetivo como sucessor!")
                sys.exit(0)

    def __sintagma_verbal(self):
        print("Sintagma Verbal")

        if (self.class_atual == "VERB"):

            self.__atualiza_token()

            if (self.class_atual == "PRON"):

                self.__sintagma_adjetival()

                return

            else:

                self.__sintagma_verbal()

        elif (self.class_atual == "ADV"):
            self.__sintagma_adverbial()

            self.__sintagma_verbal()

        elif (self.class_atual == "AUX"):

            self.__atualiza_token()

            if (self.class_atual == "VERB"):

                self.__atualiza_token()

                return

            else:

                print("Verbo Auxiliar não possui um verbo como próximo elemento!")
                sys.exit(0)
