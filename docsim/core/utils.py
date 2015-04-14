from nltk import word_tokenize
from nltk.stem.lancaster import LancasterStemmer
from nltk.corpus import stopwords

def tokenize(text):
    return word_tokenize(text)


def stem_words(list_words):
    stem = LancasterStemmer().stem
    list_stem = []

    for word in list_words:
        list_stem.append(stem(word))

    return list_stem


def remove_stop_words(list_words):
    return [w for w in list_words if w not in stopwords.words('english')]


def match_list_size(list_a, list_b):
    diff = len(list_a) - len(list_b)
    if diff > 0:
        list_b.extend([""]*diff)
    elif diff < 0:
        list_a.extend([""]*-diff)

    return
