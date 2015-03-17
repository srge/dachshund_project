from nltk import word_tokenize
from nltk.stem.lancaster import LancasterStemmer
from nltk.corpus import stopwords

def tokenize(test_string):
    return word_tokenize(test_string)


def stem_words(test_list):
    stem = LancasterStemmer().stem
    list_stem = []

    for word in test_list:
        list_stem.append(stem(word))

    return list_stem


def remove_stop_words(test_list):
    list_result = [w for w in test_list if w not in stopwords.words('english')]
    return list_result
