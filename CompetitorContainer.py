import operator

class CompetitorContainer:
    def __init__(self):
        self.Competitors = {}
    def add_competitor(self, name, time):
        self.Competitors[name] = time
    def get_winners(self):
        sorted_competitors = sorted(self.Competitors.items(), key=operator.itemgetter(1))
        return sorted_competitors
