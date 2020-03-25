import re
import os
import sys
import spacy


class lexico:

    def __init__(self, path):
        with open(path, 'r', encoding='utf-8') as file:
            entrada = file.read().replace('\n', ' ')
            analizador = spacy.load('pt_core_news_sm')

        self._tokens = analizador(entrada)

    def stop_word(self, token, classe_gramatical):
        contracoes = [
            'à', 'às', 'ao', 'aos', 'cum', 'do', 'da', 'dos', 'das', 'dum', 'duns', 'duma',
            'dumas', 'no', 'na', 'nos', 'nas', 'num', 'nuns', 'numa', 'numas', 'pro', 'pra',
            'pros', 'pras', 'prum', 'pruns', 'pruma', 'prumas', 'pelo', 'pela', 'pelos', 'pelas']

        artigos = ['a', 'o', 'as', 'os', 'em', 'de', 'por']

        if classe_gramatical in ['CONJ', 'CCONJ', 'SCONJ', 'ADP', 'DET', 'INTJ']:
            return True
        elif token in contracoes or token in artigos:
            return True
        else:
            return False


    def execoes(self, element):
        if(element.orth_ == "testes" and element.pos_ != "NOUN"):
            element.pos_ = "NOUN"
        if(element.orth_ == "documentos" and element.pos_ != "NOUN"):
            element.pos_ = "NOUN"
        return element

    def tabela_de_tokens(self):
        table = []

        for element in self._tokens:
            if element.pos_ in ['VERB', 'AUX']:
                token = element.lemma_.lower()
            else:
                token = element.orth_.lower()

            element = self.execoes(element)
            if self.stop_word(token, element.pos_):
                continue
            table.append({'token': token, 'class': element.pos_})

        return table
