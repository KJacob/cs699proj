import ply.lex

#The lexer

# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
tokens = (
   'ID',
   'EQUALS',
   'PLUS',
   'MINUS',
   'DIVIDE',
   'MULT',
   'LITERAL',
   'LEFTBR',
   'RIGHTBR'
)

# Regular expression rules for simple tokens
t_EQUALS   = r'='
t_PLUS   = r'\+'
t_MINUS = r'-'
t_DIVIDE = r'/'
t_MULT = r'\*'
t_LEFTBR = r'\('
t_RIGHTBR = r'\)'

# A regular expression rule with some action code
def t_ID(t):
    r'[a-zA-Z]+'
    return t

# Define a rule so we can track line numbers
def t_LITERAL(t):
    r'[0-9]+'
    return t

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t\n'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value)
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

#lexer.input('A->B|C{print "{Hello World}"}')
#for token in lexer:
#    print(token)
