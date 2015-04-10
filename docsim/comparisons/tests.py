from django.test import TestCase
from comparisons.models import Comparison
from django.http import HttpRequest
from comparisons.views import get_results


class ComparisonModelTest(TestCase):

    def test_can_save_model_data(self):
        comp = Comparison()
        comp.doc_a = 'Hello test'
        comp.doc_b = 'Bye test'
        comp.save()

        self.assertEqual(Comparison.objects.all().count(), 1)


    def test_can_retrieve_model_data(self):
        comp1 = Comparison()
        comp1.doc_a = 'Hello 1'
        comp1.doc_b = 'Bye 1'
        comp1.save()

        comp2 = Comparison()
        comp2.doc_a = 'Hello 2'
        comp2.doc_b = 'Bye 2'
        comp2.save()

        saved_comps = Comparison.objects.all()

        self.assertEqual(saved_comps[0].doc_a, 'Hello 1')
        self.assertEqual(saved_comps[1].doc_b, 'Bye 2')


class HomePageTest(TestCase):

    def test_home_page_renders_home_template(self):
        self.fail('Implement this test')

    def test_home_page_can_save_POST(self):
        self.fail('Implement this test')

    def test_home_page_redirects_after_POST(self):
        self.fail('Implement this test')

    def test_does_not_save_if_form_is_incomplete(self):
        self.fail('Implement this test')


class ResultsPageTest(TestCase):

    def test_results_page_renders_results_template(self):
        self.fail('Implement this test')

    def test_results_page_context_contains_cosine(self):
        self.fail('Implement this test')

    def test_results_page_context_contains_hamming(self):
        self.fail('Implement this test')

    def test_results_page_context_contains_levenshtein(self):
        self.fail('Implement this test')

    def test_results_page_context_contains_sorensen(self):
        self.fail('Implement this test')

    def test_results_page_context_contains_jaccard(self):
        self.fail('Implement this test')

    def test_results_page_context_contains_consensus(self):
        self.fail('Implement this test')

    def test_redirects_home_if_page_visited_arbitrarily(self):
        request = HttpRequest()
        response = get_results(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')
