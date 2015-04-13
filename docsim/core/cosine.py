from core import utils
import nltk
import math

class Cosine:

    def __init__(self, string1, string2):
        self.doc_a = utils.tokenize(string1)
        self.doc_b = utils.tokenize(string2)
        self.stop_doc_a = utils.remove_stop_words(self.doc_a)
        self.stop_doc_b = utils.remove_stop_words(self.doc_b)
        self.stem_doc_a = utils.stem_words(self.stop_doc_a)
        self.stem_doc_b = utils.stem_words(self.stop_doc_b)
        self.doc_ab = list(self.stem_doc_a)
        self.doc_ab.extend(self.stem_doc_b)
        self.union_ab = list(set(self.stem_doc_a).union(self.stem_doc_b))
        self.term_freq_a = self.term_freq(self.stem_doc_a)
        self.term_freq_b = self.term_freq(self.stem_doc_b)
        self.inv_doc_freq = self.inverse_doc_freq(self.union_ab,
                self.term_freq_a, self.term_freq_b)
        self.tf_idf_a = self.tf_idf(self.term_freq_a, self.inv_doc_freq)
        self.tf_idf_b = self.tf_idf(self.term_freq_b, self.inv_doc_freq)
        self.cos_result = self.calc_cos(self.tf_idf_a, self.tf_idf_b)

    def term_freq(self, list_words):
        fdist = nltk.FreqDist(list_words).most_common(200)
        return dict(fdist)

    def inverse_doc_freq(self, list_words_ab, tf_a, tf_b):
        dict_words = {}
        for word in list_words_ab:
            if word in tf_a and word in tf_b:
                #dict_words[word] = math.log10(2/2)
                dict_words[word] = 2/2
            else:
                #dict_words[word] = math.log10(2/1)
                dict_words[word] = 2/1
        return dict_words

    def tf_idf(self, dict_tf, dict_idf):
        dict_tfidf = {}

        for k in dict_idf:
            if k in dict_tf:
                dict_tfidf[k] = dict_tf[k] * dict_idf[k]
            else:
                dict_tfidf[k] = 0

        return dict_tfidf

    def calc_cos(self, tf_idf_a, tf_idf_b):
        numer = 0
        denom_a = 0
        denom_b = 0

        for k in tf_idf_a:
            val_a = tf_idf_a[k]
            val_b = tf_idf_b[k]
            numer += val_a * val_b
            denom_a += val_a ** 2
            denom_b += val_b ** 2

        return numer / (math.sqrt(denom_a) * math.sqrt(denom_b))
