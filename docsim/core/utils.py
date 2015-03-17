import nltk

def tokenize(test_string):
    words = nltk.word_tokenize(test_string)

    return words

def remove_stop_words(test_list):
    stopwords = nltk.corpus.stopwords.words('english')
    list_result = [w for w in test_list if w not in stopwords]
    return list_result

