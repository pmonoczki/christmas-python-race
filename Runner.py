import os
import sys
import inspect
import time
from Generator import InputGenerator
from CompetitorContainer import CompetitorContainer
from Validator import Validator
import sys, traceback

def load_modules_from_path(path):
   """
   Import all modules from the given directory
   """
   # Check and fix the path
   if path[-1:] != '/':
       path += '/'

   # Get a list of files in the directory, if the directory exists
   if not os.path.exists(path):
        raise OSError("Directory does not exist: %s" % path)

   # Add path to the system path
   sys.path.append(path)
   # Load all the files in path
   for f in os.listdir(path):
       # Ignore anything that isn't a .py file
       if len(f) > 3 and f[-3:] == '.py':
           modname = f[:-3]
           # Import the module
           __import__(modname, globals(), locals(), ['*'])

def load_class_from_name(fqcn):
    # Break apart fqcn to get module and classname
    paths = fqcn.split('.')
    modulename = '.'.join(paths[:-1])
    classname = paths[-1]
    # Import the module
    __import__(modulename, globals(), locals(), ['*'])
    # Get the class
    cls = getattr(sys.modules[modulename], classname)
    # Check cls
    if not inspect.isclass(cls):
       raise TypeError("%s is not a class" % fqcn)
    # Return class
    return cls

def store_race_result(cc):
    result_file = open("./Output/result.txt", "w")
    l = 1

    for k in cc.get_winners():
        s = str(l) +"." +" " +str(k)
        result_file.write(s+" \n")
        l += 1
    result_file.close()

def print_result() :
    print("RACE HAS BEEN FINISHED")
    result_file = open("./Output/result.txt", "r")
    for ii in result_file.readlines():
        print(ii)
    result_file.close()

def getInputList():
    input_list = []
    file = open("./Input/input.txt","r")
    for i in file.readlines():
        input_list.append(int(i))
    file.close()
    return  input_list

def generate_Input() :
    if not os.path.exists("./Input/input.txt"):
        print("Generate input")
        InputGenerator.generateInput()
        print("Input has been generated")

def main():
    generate_Input()
    try:
        load_modules_from_path('competitors')
    except BaseException as ex:
                print("module execution error.")
                print(ex)
                traceback.print_exc(file=sys.stdout)
    cc = CompetitorContainer()
    for i in os.listdir('competitors'):
        if '.py' in i:
            fn = i.split('.')[0]
            print("* %s  Competitor Running*" %(fn))
            class_name = load_class_from_name( fn+'.CoolCompetitor')
            loop_num = 100
            start = time.time()

            obj = class_name()
            o_list = []
            try:
                for num in range(loop_num):
                    o_list = obj.run(getInputList())
                end = time.time()
                if Validator.isValidResult(o_list):
                    print("%s  Correct Result" %(fn))
                    cc.add_competitor(fn, (end-start)/loop_num)
                else:
                    print("%s  Not Correct Result" %(fn))
                print('')
            except BaseException as ex:
                print("code execution error.")
                print(ex)
                traceback.print_exc(file=sys.stdout)
    store_race_result(cc)
    print_result()

if __name__ == '__main__': main()
