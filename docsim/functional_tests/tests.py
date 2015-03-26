from django.test import LiveServerTestCase
from selenium import webdriver

class DocsimTests(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_home_page_renders(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Dachshund', self.browser.title)

    def test_user_can_submit_form(self):
        self.fail('Implement this test')

    def test_user_cannot_submit_invalid_form(self):
        self.fail('Implement this test')

    def test_results_page_renders(self):
        self.fail('Implement this test')

    def test_results_page_contains_cosine(self):
        self.fail('Implement this test')

    def test_results_page_contains_hamming(self):
        self.fail('Implement this test')

    def test_results_page_contains_levenshtein(self):
        self.fail('Implement this test')

    def test_results_page_contains_sorensen(self):
        self.fail('Implement this test')

    def test_results_page_contains_jaccard(self):
        self.fail('Implement this test')

    def test_results_page_contains_consensus(self):
        self.fail('Implement this test')
