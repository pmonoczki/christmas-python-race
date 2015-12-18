__author__ = 'Vegh Adam'


class CoolCompetitor:
    @staticmethod
    def run(list_num: list):
        first = min(list_num)
        last = max(list_num)
        list_num.remove(first)
        list_num.remove(last)
        middle1 = min(list_num)
        middle2 = max(list_num)
        list1 = [first, middle1, last]
        list2 = [first, middle2, last]
        return list1 if abs(sum(list1)/3 - middle1) > abs(sum(list2)/3 - middle2) else list2
