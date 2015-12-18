__author__ = 'Zoltan'
from time import time
from itertools import combinations

start_time=time()
class CoolCompetitor :

    def __init__(self):
        pass

    def selecting(self,lst):
        results=[]
        diff=0.0
        combination=list(combinations(lst,3))
        for i in combination:
            i=[i[0],i[1],i[2]]
            i.sort()
            if abs((i[0]+i[1]+i[2])/3-i[1])>diff:
                results = i
                diff=abs((i[0]+i[1]+i[2])/3-i[1])

        return results

    def exam(self,difference,lista):
        if min(lista) < potentionals[0] + difference*2-1:
            potentionals.append(min(lista))
            lista.remove(min(lista))
            self.exam(difference,lista)
        if max(lista) > potentionals[1] - difference*2+1:
            potentionals.append(max(lista))
            lista.remove(max(lista))
            self.exam(difference,lista)

    def run(self,lista):
        global potentionals
        potentionals=[]
        potentionals.append(min(lista))
        potentionals.append(max(lista))
        lista.remove(min(lista))
        lista.remove(max(lista))

        difference=potentionals[1]-max(lista)
        if min(lista)-potentionals[0] < difference:
            difference=min(lista)-potentionals[0]
            if difference<=2:
                potentionals.append(min(lista))
                return potentionals
        if difference <=2:
            potentionals.append(max(lista))
            return potentionals
        self.exam(difference,lista)

        if len(potentionals)==3:

            return potentionals
        return self.selecting(potentionals)




