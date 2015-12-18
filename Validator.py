import os
class Validator :
    @staticmethod
    def isValidResult(list):

        oFile = open(".\Output\output.txt")
        list_valid = [int(line.replace('\n', '')) for line in oFile.readlines()]
        oFile.close()

        if not (len(list) == len(list_valid) ):
            return False
        for z in range(len(list_valid)):
            if not (list[z] in list_valid):
                return False

        return True
