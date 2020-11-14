from ply import yacc
from CLCLexer import CLCLexer


######################################################
# PARSER | CLCParser
#-----------------------------------------------------
# Parsing Tokens into AST (Abstract Syntax Tree)
######################################################


class CLCParser:
    
    def __init__(self):
        self.lexer = CLCLexer()
        self.tokens = self.lexer.tokens

        self.precedence = (
            ('left', 'PLUS','MINUS'),
            ('left', 'TIMES','DIVIDE'),
        )
     
        self.parser = yacc.yacc(module=self)

    # p_start = 'term'

    def p_program(self,p):
        """
        program : var
                | print
        """
        p[0] = p[1]

    def p_print(self,p):
        """
        print : PRINT expr
        """
        p[0] = ("PRINT",p[2])

    def p_varAssign(self,p):
        """
        var : VARIABLE ID EQ expr 
        """
        p[0] = ("var_assignment",p[2],p[4])

    
    def p_add(self,p):
        """
        mat_op : expr PLUS expr
               | expr TIMES expr
               | expr DIVIDE expr
               | expr MINUS expr
        """
        
        if p[2] == "*":
            p[0] = ("MAT_MULT",p[1],p[3])
        elif p[2] == "/":
            p[0] = ("DIVISION",p[1],p[3])
        elif p[2] == "-":
            p[0] = ("MIN",p[1],p[3])
        else:
            p[0] = ("MAT_ADD",p[1],p[3])


    def p_expr(self,p):
        """
        expr : NUMBER
             | ID
             | mat_op
             | STRING
        """
        p[0] = p[1]
        
    def p_error(self,p):
        # print("Error : ",p)
        return p
