from django.test import TestCase
from core import utils, docdistance, setsimilarity

class UtilsTest(TestCase):

    def test_can_tokenize(self):
        test_string = 'The quick brown fox jumps over the lazy dog.'
        list_expected = ['The', 'quick', 'brown', 'fox', 'jumps', 'over',
                'the', 'lazy', 'dog', '.']
        list_actual = utils.tokenize(test_string)
        self.assertListEqual(list_expected, list_actual,
                "Lists should be equal")

    def test_can_remove_stop_words(self):
        test_list = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours',
                         'quick', 'brown', 'fox', 'why', 'how', 'all',
                         'any', 'both', 'each']
        list_expected = ['quick', 'brown', 'fox']
        list_actual = utils.remove_stop_words(test_list)
        self.assertListEqual(list_expected, list_actual,
                "Stop Words not removed correctly.")

    def test_can_stem_words(self):
        test_list = ['Scientists', 'are', 'reading', 'mostly', 'everything',
                'on', 'the', 'internet']
        list_expected = ['sci', 'ar', 'read', 'most', 'everyth', 'on', 'the',
                'internet']
        list_actual = utils.stem_words(test_list)
        self.assertListEqual(list_expected, list_actual,
                "Lists should be equal")


class LevenshteinTest(TestCase):

    def test_calc_lev_calculates_distance(self):
        test_list_a = ['A', 'pocket', 'full', 'of', 'posies', 'ashes',
                       'ashes', 'we', 'all', 'fall', 'down']
        test_list_b = ['pocket', 'full', 'of', 'posies', 'ashes']
        expected = 0.5454545454
        actual = docdistance.Levenshtein(test_list_a, test_list_b).calculate_dist()
        self.assertAlmostEqual(expected, actual,
                msg="Normalized Levenshtein calculate dist not as expected")


class HammingTest(TestCase):

    def test_calc_ham_calculates_distance(self):
        test_list_a = ['the', 'cow', 'jumped', 'over', 'the', 'moon']
        test_list_b = ['the', 'cat', 'jumped', 'into', 'the', 'sun']
        expected = 0.5
        actual = docdistance.Hamming(test_list_a, test_list_b).calculate_dist()
        self.assertAlmostEqual(expected, actual,
                msg="Normalized Hamming calculate dist not as expected")


class CosineTest(TestCase):

    def test_term_freq_finds_each_word_count(self):
        test_list_words = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana'
                           'apple', 'banana', 'pear', 'orange', 'banana', 'pear']
        dict_expected = {'apple' : 3, 'banana' : 3, 'orange' : 3, 'pear' : 3}
        dict_actual = cosine.term_freq(test_list_words)
        self.assertDictEqual(dict_expected, dict_actual,
                "term frequency dictionaries do not have the same keys and values")

    def test_inverse_doc_freq_finds_idf(self):
        test_dict_tf = {'apple' : 1, 'banana' : 2, 'orange' : 2, 'pear' : 1}
        dict_expected = {'apple' : 2, 'banana' : 1, 'orange' : 1, 'pear' : 2}
        dict_actual = cosine.inverse_doc_freq(test_dict_tf)
        for key in dict_expected:
            if key not in dict_actual:
                self.fail(key + 'is in expected but not actual')
            else:
                self.assertAlmostEqual(dict_expected[key], dict_actual[key],
                    msg="IDF vectors are not the almost equal at key: "+key)

    def test_can_calculate_tf_idf(self):
        test_dict_tf = {'apple' : 3, 'banana' : 3, 'orange' : 3, 'pear' : 3}
        test_dict_idf = {'apple': 2, 'banana': 1, 'orange': 1, 'pear': 2}
        dict_expected = {'apple': 0.9030899869919435, 'pear': 0.9030899869919435,
                         'banana': 0.0, 'orange': 0.0}
        dict_actual = cosine.tf_idf(test_dict_tf, test_dict_idf)
        for key in dict_expected:
            if key not in dict_actual:
                self.fail(key + 'is in expected but not actual')
            else:
                self.assertAlmostEqual(dict_expected[key], dict_actual[key],
                    msg="TF-IDF vectors are not the almost equal at key: "+key)

    def test_calc_cos_returns_cosinine_similarity(self):
        test_dict_tf_idf = {'apple': 0.9030899869919435, 'pear': 0.9030899869919435,
                         'banana': 0.0, 'orange': 0.0}
        expected = 1.0
        actual = cosine.calc_cos(test_dict_tf_idf, test_dict_tf_idf)

        self.assertAlmostEqual(expected, actual, msg="cosine value is not almost equal")

class SorensenTest(TestCase):

    def test_build_intersection_set(self):
        test_list_a = ["The", "cat", "in", "the", "hat"]
        test_list_b = ["The", "dog", "in", "the", "car"]
        expected = ["The", "in", "the"]
        actual = setsimilarity.Sorensen(test_list_a, test_list_b).build_intersect()
        self.assertListEqual(expected, actual, "Lists should be equal")

    def test_build_union_set(self):
        test_list_a = ["The", "cat", "in"]
        test_list_b = ["the", "hat"]
        expected = ["The", "cat", "in", "the", "hat"]
        actual = setsimilarity.Sorensen(test_list_a, test_list_b).build_union()
        self.assertListEqual(expected, actual, "Lists should be equal")

    def test_calculate_sorensen(self):
        self.fail('Implement this test')


class JaccardTest(TestCase):

    def test_build_intersection_set(self):
        self.fail('Implement this test')

    def test_build_union_set(self):
        self.fail('Implement this test')

    def test_calculate_jaccard(self):
        self.fail('Implement this test')


class ConsensusTest(TestCase):

    def test_calc_consensus_finds_consensus(self):
        self.fail('Implement this test')
