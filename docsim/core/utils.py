from nltk import word_tokenize
from nltk.stem.lancaster import LancasterStemmer

def tokenize(test_string):
    return word_tokenize(test_string)


def stem_words(test_list):
    stem = LancasterStemmer().stem
    list_stem = []

    for word in test_list:
        list_stem.append(stem(word))

    return list_stem


