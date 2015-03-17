class SetSimilarity(object):

    def __init__(self, list_a, list_b):
        self.list_a = list_a
        self.list_b = list_b

    def build_intersect(self):
        raise NotImplementedError

    def build_union(self):
        raise NotImplementedError

    def calculate_sim(self):
        raise NotImplementedError


class Sorensen(SetSimilarity):

    def __init__(self, list_a, list_b):
        SetSimilarity.__init__(self, list_a, list_b)
        self.build_intersect()
        self.build_union()

    def build_intersect(self):
        self.intersect = list(set(self.list_a) & set(self.list_b))
        return self.intersect

    def build_union(self):
        self.union = list(set(self.list_a) | set(self.list_b))
        return self.union

    def calculate_sim(self):
        return 2 * len(self.intersect) / len(self.union)


class Jaccard(SetSimilarity):

    def __init__(self, list_a, list_b):
        SetSimilarity.__init__(self, list_a, list_b)
        self.build_intersect()
        self.build_union()

    def build_intersect(self):
        self.intersect = list(set(self.list_a) & set(self.list_b))
        return self.intersect

    def build_union(self):
        self.union = list(set(self.list_a) | set(self.list_b))
        return self.union

    def calculate_sim(self):
        return len(self.intersect) / len(self.union)
