import heapq


class CoolCompetitor:

    @staticmethod
    def run(input_list):
        a, b = heapq.nsmallest(2, input_list)
        c, d = heapq.nlargest(2, input_list)
        return [a, b, c] if b - a <= c - d else [a, d, c]
