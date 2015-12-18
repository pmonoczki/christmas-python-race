import time
import math
from Competitor_Template import Competitor

class CoolCompetitor(Competitor):
    c_BLOCK_SIZE = 256
    c_MAX_NUMBER = 2500000
    c_MIN_NUMBER = 1
    lowThreshold = 0
    highThreshold = 0
    c_CAPACITY  = 200000
    numbers = []
    lowNumbers = []
    highNumbers  = []
    inputSize = 0
    min, max = 0, 0
    hp1, hp2, lp1, lp2 = 0,0,0,0
    cnt, i, next, x = 0,0,0,0
    def _init__(self):
        print("init")
    def run(self, input_list):
        self.numbers = [0] * self.c_CAPACITY
        self.load(input_list)
        self.calculateHighPair()
        self.calculateLowPair()
        self.write_output(self.writeResult())
        return self.writeResult()

    def writeResult(self):
        list_result = []

        if math.fabs(self.min + self.hp2 - self.hp1 - self.hp1) > math.fabs(self.lp1 + self.max - self.lp2 - self.lp2) :
            list_result.append(self.min)
            list_result.append(self.hp1)
            list_result.append(self.hp2)
        else :
            list_result.append(self.lp1)
            list_result.append(self.lp2)
            list_result.append(self.max)
        return list_result

    def load(self, list_in):

        self.inputSize = len(list_in)
        ccc = 0
        if self.inputSize <= self.c_BLOCK_SIZE + self.c_BLOCK_SIZE :
            self.lowThreshold = self.c_MIN_NUMBER
            self.highThreshold = self.c_MAX_NUMBER
        else :
            self.lowThreshold = self.c_MIN_NUMBER + self.c_BLOCK_SIZE
            self.highThreshold = self.c_MAX_NUMBER - self.c_BLOCK_SIZE
        for l in range(0, self.c_BLOCK_SIZE):
            self.lowNumbers.append(False)
            self.highNumbers.append(False)
        for t in range (0, self.inputSize) :
            w = list_in[t]
            if w < self.lowThreshold :
                self.lowNumbers[w - self.c_MIN_NUMBER] = True
            elif w > self.highThreshold :
                self.highNumbers[self.c_MAX_NUMBER - w] = True
            else :
                ccc+=1
                self.numbers[ccc] = w

    def calculateHighPair(self):
        self.max = self.findNextHigh(self.c_MAX_NUMBER + 1)
        self.hp2 = self.findNextHigh(self.c_MAX_NUMBER + 1)
        self.hp1 = self.findNextHigh(self.hp2)
        openMax = self.hp1
        while self.isHighImprovementPossible(openMax):
            b = self.findNextHigh(openMax)
            if self.isHighImprovement(b, openMax):
                self.hp1 = b
                self.hp2 = openMax
            openMax = b

    def calculateLowPair(self):
        self.lp1 = self.findNextLow(self.c_MIN_NUMBER - 1)
        self.min = self.findNextLow(self.c_MIN_NUMBER - 1)
        self.lp2 = self.findNextLow(self.lp1)

        openMin = self.lp2

        while self.isLowImprovementPossible(openMin):
            m = self.findNextLow(openMin)
            if self.isLowImprovement(openMin, m):
                self.lp1 = openMin
                self.lp2 = m
            openMin = m

    def isHighImprovement(self, g, h):
        return g + g + self.hp2 > self.hp1 + self.hp1 + h
    def isLowImprovement(self,g,h):
        return h + h + self.lp1 < self.lp2 + self.lp2 + g

    def findNextHigh(self, pprev):
        for y in range (pprev -1, self.highThreshold,-1):
            if self.highNumbers[self.c_MAX_NUMBER - y] :
                return y
        nnext = self.c_MIN_NUMBER
        for yy in range(0, self.cnt) :
            if self.numbers[i] > nnext and numbers[yy] < pprev :
                nnext = self.numbers[yy]

        return nnext

    def findNextLow(self, prevv):
        for iii in range (prevv+1, self.lowThreshold):
            if self.lowNumbers[iii - self.c_MIN_NUMBER]:
                return iii
        nextt = self.c_MAX_NUMBER
        print("lofasz %s" %(self.cnt) )
        for ii in range (0, self.cnt) :
            if self.numbers[ii] > prevv and self.numbers[ii] < nextt :
                nextt = self.numbers[ii];
        return nextt


    def isHighImprovementPossible(self, openMax):
        return openMax + self.hp2 > self.hp1 + self.hp1 + 2

    def isLowImprovementPossible(self, openMin):
        return openMin + 2 + self.lp1 < self.lp2 + self.lp2

    def write_output(self, result_list):
        result_file = open("./Output/output.txt","w")
        for i in result_list :
            result_file.write(str(i)+ "\n")
        result_file.close()