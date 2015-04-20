from core import utils
from core.cosine import Cosine
from core.docdistance import Hamming
from core.docdistance import Levenshtein
from core.setsimilarity import Sorensen
from core.setsimilarity import Jaccard
from statistics import mean, variance

class Consensus(object):

    def __init__(self, doc_a, doc_b):
        self.list_a = utils.tokenize(doc_a)
        self.list_b = utils.tokenize(doc_b)
        self.jac = Jaccard(self.list_a, self.list_b).calculate_sim()
        self.sor = Sorensen(self.list_a, self.list_b).calculate_sim()
        self.ham = Hamming(self.list_a, self.list_b).calculate_dist()
        self.lev = Levenshtein(self.list_a, self.list_b).calculate_dist()
        self.cos = Cosine(doc_a, doc_b).cos_result

    def get_consensus(self):
        results = {
                'jac': self.jac,
                'sor': self.sor,
                'ham': self.ham,
                'lev': self.lev,
                'cos': self.cos,
            }

        data = results.values()
        m = mean(data)
        var = variance(data, m)

        results['var'] = var

        return results
