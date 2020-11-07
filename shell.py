# A Simple Calculator Language
# Aria Bishma <ariabishma848@gmail.com>


from CLCParser import CLCParser

from Core import Math

#####################################
# Interpreter
#####################################

script ="1+1"

parser = CLCParser()

while True:
    script = input("calc-Lang >> ")
    if script == "exit":
        exit()
        
    ast = parser.parser.parse(script)
    res = Math(ast)

    print("result : ",res)