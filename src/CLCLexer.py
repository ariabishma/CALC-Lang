from ply import lex

######################################################
# LEXER | CLCLexer
#-----------------------------------------------------
# Tokenize input script
######################################################

class CLCLexer:
    t_PLUS     = r'\+'
    t_MINUS    = r'-'
    t_TIMES    = r'\*'
    t_DIVIDE   = r'/'
    t_VARIABLE = r'_var'
    t_PRINT    = r'_print'
    t_EQ       = r'='

    t_ignore   = ' \t\n'
   
    def __init__(self,script=None):
        self.tokens = [
            'NUMBER',
            'PLUS',
            'MINUS',
            'TIMES',
            'VARIABLE',
            'PRINT',
            'ID',
            'STRING',
            'EQ',
            'DIVIDE'            
        ]
        self.lexer = lex.lex(module=self)
        
        if script != None:
            self.script = script
            self.lexer.input(self.script)
    
    def get_tokenized(self):
        tokens = []
        lex = self.lexer
        while True:
            tok = lex.token()
            if not tok:
                break      # No more input
            tokens.append(tok)
        return tokens

    def t_STRING(self,token):
        r'\"([a-zA-Z ]+)\"'
        return token

    def t_ID(self,token):
        r'[a-zA-Z]+'
        return token

    def t_NUMBER(self,token):
        r'\d+'
        token.value = int(token.value)
        return token


    def t_error(self,t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
        return t