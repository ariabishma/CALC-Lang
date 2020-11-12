######################################################
# Interpreter | CLCInterpreter
#-----------------------------------------------------
# Interpreting AST (Abstract Syntax Tree) 
######################################################

class CLCInterpreter:
    def __init__(self,ast,storage):
        self.r = 0
        self.storage = storage
        self.visit(ast)

    def visit(self,ast):
        if ast[0] == "MAT_ADD": 
            return self.add(ast)
        if ast[0] == "DIVISION" : 
            return self.div(ast)
        if ast[0] == "MAT_MULT" : 
            return self.mult(ast)
        if ast[0] == "MIN" : 
            return self.minus(ast)
        if ast[0] == "var_assignment":
            return self.assign(ast)
        if ast[0] == "PRINT":
            return self.program_print(ast)


    def program_print(self,node):
        val = node[1]
        if type(val) is str and val[0] != '\"' :
            val = self.var_access(val)
        if type(val) is tuple:
            val = self.visit(val)
        
        print("PRINT OUT : ",val)

    def assign(self,node):
        identifier = node[1]
        value = node[2] 

        if type(value) is tuple:
            value = self.visit(value)
        
        self.storage.setVar(identifier,value)
        return value

    def var_access(self,identifier):
        return self.storage.getVar(identifier)

    def add(self,node):
        left = node[1]
        right = node[2] 
    
        if type(left) is tuple:
            left = self.visit(left)
        if type(right) is tuple:
            right = self.visit(right)

        if type(left) is str:
            left = self.var_access(left)
        if type(right) is str:
            right = self.var_access(right)
        
        self.r = left+right
        return left+right

    def div(self,node):
        left = node[1]
        right = node[2] 
    
        if type(left) is tuple:
            left = self.visit(left)
        if type(right) is tuple:
            right = self.visit(right)

        if type(left) is str:
            left = self.var_access(left)
        if type(right) is str:
            right = self.var_access(right)
        
        self.r = left/right
        return left/right

    def mult(self,node):
        left = node[1]
        right = node[2] 
    
        if type(left) is tuple:
            left = self.visit(left)
        if type(right) is tuple:
            right = self.visit(right)

        if type(left) is str:
            left = self.var_access(left)
        if type(right) is str:
            right = self.var_access(right)
        
        self.r = left*right
        return left*right

    def minus(self,node):
        left = node[1]
        right = node[2] 
    
        if type(left) is tuple:
            left = self.visit(left)
        if type(right) is tuple:
            right = self.visit(right)

        if type(left) is str:
            left = self.var_access(left)
        if type(right) is str:
            right = self.var_access(right)
        
        self.r = left-right
        return left-right
        
    def __repr__(self):
        return str(self.r)