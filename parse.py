# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lex import tokens

rules_list = []

def p_rules(p):
	'rules : rules rule'
	rules_list = rules_list + p[2]

def p_rule(p):
	'rule : leftsymb GIVES bodies'
	p[0] = [[p[1], x] for x in p[3]]

def p_bodies(p):
	'bodies : body bodies'
	p[1] = 

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = raw_input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)
