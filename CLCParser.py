from ply import yacc
from CLCLexer import CLCLexer

class CLCParser:
    
    def __init__(self):
        self.lexer = CLCLexer()
        self.tokens = self.lexer.tokens
        self.parser = yacc.yacc(module=self)
    
    def p_addition(self,p):
        """
        EXPR : NUMBER PLUS NUMBER
        """
        p[0] = ("ADDITION",p[1], p[3])
    
    def p_division(self,p):
        """
        EXPR : NUMBER DIVIDE NUMBER
        """
        p[0] = ("DIVISION",p[1], p[3])
    
    def p_mul(self,p):
        """
        EXPR : NUMBER TIMES NUMBER
        """
        p[0] = ("MULT",p[1], p[3])
    
    def p_min(self,p):
        """
        EXPR : NUMBER MINUS NUMBER
        """
        p[0] = ("MIN",p[1], p[3])

    def p_error(self,p):
        print("Error : ",p)