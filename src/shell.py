# CLCLang
# A Simple Scripting Language
#
# Aria Bishma <ariabishma848@gmail.com>


from CLCParser import CLCParser

from CLCInterpreter import CLCInterpreter as Interpret

import sys


#####################################
# Shell
#####################################


parser = CLCParser()

file_name = sys.argv[1]

file_format = file_name[len(file_name)-4:]



try:
    with open(file_name) as f:
        script = f.read()

    if(file_format != ".clc"):
        script = ""
        print("the file format is must be .clc")
except: 
    script = ""
    print("cannot find '" , file_name ,"'")




script = script.splitlines()

asts = {"program" :[]}

class varSotrage:
    def __init__(self):
        self.vars = {}
    
    def setVar(self,identifier,value):
        self.vars[identifier] = value

    def getVar(self,identifier):
        if self.vars[identifier]:
            return self.vars[identifier]
        print("variable {} , has not declared",identifier)
        return 0
storage = varSotrage()


for s in script:
    ast = parser.parser.parse(s)
    if ast:
        res = Interpret(ast,storage)
