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
        self.browser.get('http://localhost:8000')
        doc_a = self.browser.find_element_by_id('id_doc_a')
        doc_b = self.browser.find_element_by_id('id_doc_b')
        doc_a.send_keys('Hello doc a')
        doc_b.send_keys('Hello doc b')
        button = self.browser.find_element_by_id('id_button')
        button.click()

        self.assertIn('Results', self.browser.title)

    def test_user_cannot_submit_invalid_form(self):
        self.browser.get('http://localhost:8000')
        doc_a = self.browser.find_element_by_id('id_doc_a')
        doc_b = self.browser.find_element_by_id('id_doc_b')
        doc_a.send_keys('Hello doc a')
        button = self.browser.find_element_by_id('id_button')
        button.click()

        self.assertNotIn('Results', self.browser.title)

    def test_results_page_renders(self):
        self.browser.get('http://localhost:8000')
        doc_a = self.browser.find_element_by_id('id_doc_a')
        doc_b = self.browser.find_element_by_id('id_doc_b')
        doc_a.send_keys('Hello doc a')
        doc_b.send_keys('Hello doc b')
        button = self.browser.find_element_by_id('id_button')
        button.click()

        self.assertIn('Results', self.browser.title)

    def test_results_page_contains_cosine(self):
        self.browser.get('http://localhost:8000')
        doc_a = self.browser.find_element_by_id('id_doc_a')
        doc_b = self.browser.find_element_by_id('id_doc_b')
        doc_a.send_keys('Hello doc a')
        doc_b.send_keys('Hello doc b')
        button = self.browser.find_element_by_id('id_button')
        button.click()

        table = self.browser.find_element_by_id('id_results')
        rows = table.find_elements_by_tag_name('td')

        self.assertIn('Cosine:', [row.text for row in rows])

    def test_results_page_contains_hamming(self):
        self.browser.get('http://localhost:8000')
        doc_a = self.browser.find_element_by_id('id_doc_a')
        doc_b = self.browser.find_element_by_id('id_doc_b')
        doc_a.send_keys('Hello doc a')
        doc_b.send_keys('Hello doc b')
        button = self.browser.find_element_by_id('id_button')
        button.click()

        table = self.browser.find_element_by_id('id_results')
        rows = table.find_elements_by_tag_name('td')

        self.assertIn('Hamming:', [row.text for row in rows])

    def test_results_page_contains_levenshtein(self):
        self.browser.get('http://localhost:8000')
        doc_a = self.browser.find_element_by_id('id_doc_a')
        doc_b = self.browser.find_element_by_id('id_doc_b')
        doc_a.send_keys('Hello doc a')
        doc_b.send_keys('Hello doc b')
        button = self.browser.find_element_by_id('id_button')
        button.click()

        table = self.browser.find_element_by_id('id_results')
        rows = table.find_elements_by_tag_name('td')

        self.assertIn('Levenshtein:', [row.text for row in rows])


    def test_results_page_contains_sorensen(self):
        self.browser.get('http://localhost:8000')
        doc_a = self.browser.find_element_by_id('id_doc_a')
        doc_b = self.browser.find_element_by_id('id_doc_b')
        doc_a.send_keys('Hello doc a')
        doc_b.send_keys('Hello doc b')
        button = self.browser.find_element_by_id('id_button')
        button.click()

        table = self.browser.find_element_by_id('id_results')
        rows = table.find_elements_by_tag_name('td')

        self.assertIn('Sorensen:', [row.text for row in rows])

    def test_results_page_contains_jaccard(self):
        self.browser.get('http://localhost:8000')
        doc_a = self.browser.find_element_by_id('id_doc_a')
        doc_b = self.browser.find_element_by_id('id_doc_b')
        doc_a.send_keys('Hello doc a')
        doc_b.send_keys('Hello doc b')
        button = self.browser.find_element_by_id('id_button')
        button.click()

        table = self.browser.find_element_by_id('id_results')
        rows = table.find_elements_by_tag_name('td')

        self.assertIn('Jaccard:', [row.text for row in rows])

    def test_results_page_contains_consensus(self):
        self.browser.get('http://localhost:8000')
        doc_a = self.browser.find_element_by_id('id_doc_a')
        doc_b = self.browser.find_element_by_id('id_doc_b')
        doc_a.send_keys('Hello doc a')
        doc_b.send_keys('Hello doc b')
        button = self.browser.find_element_by_id('id_button')
        button.click()

        table = self.browser.find_element_by_id('id_results')
        rows = table.find_elements_by_tag_name('td')

        self.assertIn('Variance:', [row.text for row in rows])
