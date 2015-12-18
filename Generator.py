import os
import random
class InputGenerator :
    @staticmethod
    def generateInput():
        input_list = []
        cc = 0
        while cc < 200000:
            x = random.randrange(1,2500000)
            if not str(x) in input_list :
                input_list.append(str(x)+'\n')
                cc += 1
        input_file = open("./Input/input.txt", "w")
        input_file.writelines(input_list)
        input_file.close()


