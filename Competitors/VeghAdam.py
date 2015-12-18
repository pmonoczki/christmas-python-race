__author__ = 'Vegh Adam'


class CoolCompetitor:
    @staticmethod
    def run(list_num: list):
        list_num.sort()
        list1 = [list_num[0], list_num[1], list_num[-1]]
        list2 = [list_num[0], list_num[-2], list_num[-1]]
        if abs(sum(list1)/3 - list_num[1]) > abs(sum(list2)/3 - list_num[-2]):
            #print(abs(sum(list1)/3 - list_num[1]))
            #print(abs(sum(list1)/3 - list_num[1]))
            return list1
        else:
            print(abs(sum(list2)/3 - list_num[-2]))
            return list2

