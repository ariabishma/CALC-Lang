class Math:
    def __init__(self,ast):
        self.r = 0
        if ast[0] == "ADDITION" : 
            self.add(ast[1],ast[2])
        if ast[0] == "DIVISION" : 
            self.div(ast[1],ast[2])
        if ast[0] == "MULT" : 
            self.mult(ast[1],ast[2])
        if ast[0] == "MIN" : 
            self.minus(ast[1],ast[2])

    def add(self,n1,n2):
        self.r = n1+n2
    
    def div(self,n1,n2):
        self.r = n1/n2

    def mult(self,n1,n2):
        self.r = n1*n2

    def minus(self,n1,n2):
        self.r = n1-n2
        
    def __repr__(self):
        return str(self.r)