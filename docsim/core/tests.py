from django.test import TestCase


class UtilsTest(TestCase):

    def test_can_tokenize(self):
        self.fail('Implement this test')

    def test_can_remove_stop_words(self):
        self.fail('Implement this test')

    def test_can_stem_words(self):
        self.fail('Implement this test')


class LevenshteinTest(TestCase):

    def test_calc_lev_calculates_distance(self):
        self.fail('Implement this test')


class HammingTest(TestCase):

    def test_calc_ham_calculates_distance(self):
        self.fail('Implement this test')


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
