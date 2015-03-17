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
        self.fail('Implement this test')

    def test_inverse_doc_freq_finds_idf(self):
        self.fail('Implement this test')

    def test_can_calculate_tf_idf(self):
        self.fail('Implement this test')

    def test_calc_cos_returns_cosinine_similarity(self):
        self.fail('Implement this test')


class SorensenTest(TestCase):

    def test_build_intersection_set(self):
        test_list_a = ["The", "cat", "in", "the", "hat"]
        test_list_b = ["The", "dog", "in", "the", "car"]
        expected = ["The", "in", "the"]
        actual = setsimilarity.Sorensen(test_list_a, test_list_b).build_intersect()
        self.fail('Implement this test')

    def test_build_union_set(self):
        self.fail('Implement this test')

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
