__author__ = 'Tiba Gabor'


class CoolCompetitor:

    @staticmethod
    def run(input_list):
        a = min(input_list)
        input_list.remove(a)
        b = min(input_list)
        c = max(input_list)
        input_list.remove(c)
        d = max(input_list)
        return [a, b, c] if b - a <= c - d else [a, d, c]
