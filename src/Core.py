class Math:
    def __init__(self,ast):
        self.r = 0
        self.visit(ast)

    def visit(self,ast):
        if ast[0] == "MAT_ADD" : 
            return self.add(ast)
        if ast[0] == "DIVISION" : 
            return self.div(ast)
        if ast[0] == "MAT_MULT" : 
            return self.mult(ast)
        if ast[0] == "MIN" : 
            return self.minus(ast)

    def add(self,node):
        left = node[1]
        right = node[2] 

        if type(left) is tuple:
            left = self.visit(left)
        if type(right) is tuple:
            right = self.visit(right)

        self.r = left+right
        return left+right

    def div(self,node):
        left = node[1]
        right = node[2] 

        if type(left) is tuple:
            left = self.visit(left)
        if type(right) is tuple:
            right = self.visit(right)

        self.r = left/right
        return left/right

    def mult(self,node):
        left = node[1]
        right = node[2] 

        if type(left) is tuple:
            left = self.visit(left)
        if type(right) is tuple:
            right = self.visit(right)

        self.r = left*right
        return left*right

    def minus(self,node):
        left = node[1]
        right = node[2] 

        if type(left) is tuple:
            left = self.visit(left)
        if type(right) is tuple:
            right = self.visit(right)

        self.r = left-right
        return left-right
        
    def __repr__(self):
        return str(self.r)