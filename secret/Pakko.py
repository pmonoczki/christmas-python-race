
from Competitor_Template import Competitor

class CoolCompetitor(Competitor):
    MIDDLE_NUMBER = 125000
    def __init__(self):
        self.n = []
        self.count = 0
        self.seek = 0

    def run(self, input_list):
        output_list = []

        self.count = len(output_list)

        self.n = input_list
        min = self.nextMin()
        max = self.nextMax()

        nI = max
        ni = self.nextMax()
        nii = self.nextMax()

        y = ni - nii
        maxdiff = 2 * ni - nI
        r1 = ni
        r2 = nI
        while nI > nii + 2 * y :

            diff = 2 * nii - ni
            if diff > maxdiff :

                maxdiff = diff
                r1 = nii
                r2 = ni

            nii = self.nextMax()
            ni = nii
            nI = ni
            y = ni - nii



        nI = min
        ni = self.nextMin()
        nii = self.nextMin()
        y = nii - ni
        mindiff = min - 2 * ni
        s1 = nI
        s2 = ni
        while nii > nI + 2 * y :

            diff = ni - 2 * nii
            if diff > mindiff :

                mindiff = diff
                s1 = ni
                s2 = nii

            nii = self.nextMax()
            ni = nii
            nI = ni
            y = nii - ni

        if maxdiff - min > mindiff + max :

            output_list.append(min)
            output_list.append(r1)
            output_list.append(r2)

        else :

            output_list.append(s1)
            output_list.append(s2)
            output_list.append(max)
        self.write_output(output_list)
        return output_list

    def nextMin(self):
        min = self.n[self.seek]
        self.seek += 1
        mini = 0
        for i in range(1, self.count +1):
            if self.n[i] < min :
                min = self.n[i]
                mini = i
        self.n[mini] = self.MIDDLE_NUMBER
        return min

    def nextMax(self):
        max = self.n[self.seek]
        self.seek += 1
        maxi = 0
        for i in range(1,self.count+1):
            if self.n[i] > max :
                max = self.n[i]
                maxi = i
        self.n[maxi] = self.MIDDLE_NUMBER

        return max
    def write_output(self, result_list):
        result_file = open("./Output/output.txt","w")
        for i in result_list :
            result_file.write(str(i)+ "\n")
        result_file.close()
