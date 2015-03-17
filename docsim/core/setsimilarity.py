class SetSimilarity(object):

    def __init__(self, list_a, list_b):
        self.list_a = list_a
        self.list_b = list_b

    def build_intersect(self):
        raise NotImplementedError

    def build_union(self):
        raise NotImplementedError


class Sorensen(SetSimilarity):

    def __init__(self, list_a, list_b):
        SetSimilarity.__init__(self, list_a, list_b)

    def build_intersect(self):
        return list(set(self.list_a) & set(self.list_b))

    def build_union(self):
        return list(set(self.list_a) | set(self.list_b))


class Jaccard(SetSimilarity):
    
    def __init__(self, list_a, list_b):
        SetSimilarity.__init__(self, list_a, list_b)

    def build_intersect(self):
        return list(set(self.list_a) & set(self.list_b))

    def build_union(self):
        return list(set(self.list_a) | set(self.list_b))
