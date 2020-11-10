# A Simple Calculator Language
# Aria Bishma <ariabishma848@gmail.com>


from CLCParser import CLCParser

from Core import Math

#####################################
# Interpreter
#####################################


parser = CLCParser()
# ast = parser.parser.parse(script)

# print(ast)

while True:
    script = input("calc-Lang >> ")
    if script == "exit":
        exit()
        
    ast = parser.parser.parse(script,debug=0)
    if ast :
        res = Math(ast)
        print(res.r)
    


    # tokens = parser.lexer.get_tokenized()

    # print("===================TOKEN===============")
    # print(tokens)
    # print("===================AST===============")
    # print(ast)
