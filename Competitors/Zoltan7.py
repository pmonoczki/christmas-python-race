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
        for i in range(len(lst)):
            for j in range(len(lst)):
                if i < j:
                    for k in range(len(lst)):
                        if j<k:
                            res=[lst[i],lst[j],lst[k]]
                            res.sort()
                            if abs((res[0]+res[1]+res[2])/3-res[1])>diff:
                                results = res
                                diff = abs((res[0]+res[1]+res[2])/3-res[1])
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




