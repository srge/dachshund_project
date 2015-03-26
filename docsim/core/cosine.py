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
        self.term_freq_a = self.term_freq(self.stem_doc_a)
        self.term_freq_b = self.term_freq(self.stem_doc_b)
        self.doc_ab = list(set(self.stem_doc_a) | set(self.stem_doc_b))
        self.inv_doc_freq = self.inverse_doc_freq(self.doc_ab,
                                self.term_freq_a, self.term_freq_b)

    def term_freq(self, list_words):
        fdist = nltk.FreqDist(list_words).most_common(200)
        return dict(fdist)

    def inverse_doc_freq(self, list_words_ab, list_tf_a, list_tf_b):
        dict_words = {}
        for word in list_words_ab:
            if word in list_tf_a and word in list_tf_b:
                dict_words[word] = math.log10(2/2)
            else:
                dict_words[word] = math.log10(2/1)
        return dict_words

    def tf_idf(self, dict_tf, dict_idf):
        dict_tfidf = {}
        for (k,v), (k2,v2) in zip(dict_tf.items(), dict_idf.items()):
            if(k == k2):
                tfidf = float(v*v2)
                dict_tfidf[k] = tfidf
        return dict_tfidf
