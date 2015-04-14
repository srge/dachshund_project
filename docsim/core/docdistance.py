import distance
from core.utils import match_list_size

class DocDistance(object):
    def __init__(self, list_a, list_b):
        self.list_a = list_a
        self.list_b = list_b

    def calculate_dist(self):
        raise NotImplementedError


class Levenshtein(DocDistance):
    def __init__(self, list_a, list_b):
        DocDistance.__init__(self, list_a, list_b)

    def calculate_dist(self):
        return distance.levenshtein(self.list_a, self.list_b)


class Hamming(DocDistance):
    def __init__(self, list_a, list_b):
        match_list_size(list_a, list_b)
        DocDistance.__init__(self, list_a, list_b)

    def calculate_dist(self):
        return distance.hamming(self.list_a, self.list_b)
