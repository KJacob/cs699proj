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
   'SYMBOL',
   'GIVES',
   'OR',
   'PYCODE'
)

# Regular expression rules for simple tokens
t_GIVES   = r'->'
t_OR   = r'|'

# A regular expression rule with some action code
def t_SYMBOL(t):
    r'[a-z]+'    
    return t

# Define a rule so we can track line numbers
def t_PYCODE(t):
    r'{.*}'
    t.val = t.val[1:-1]
    return t

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

lexer.input('A->B|C{print "{Hello World}"}')