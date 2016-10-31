# Yacc example

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lex import tokens

rules_list = []

def p_rules(p):
	'''rules : rules rule
			 | rule'''
	global rules_list
	
	if len(p) == 2:
		rules_list = rules_list + p[1]
	else:
		rules_list = rules_list + p[2]

def p_rule(p):
	'rule : leftsymb GIVES bodies'
	p[0] = [[p[1], x] for x in p[3]]

def p_bodies(p):
	'''bodies : body OR bodies
			  | body'''
	if len(p) == 4:
		p[0] = [p[1]] + p[3]
	else:
		p[0] = [p[1]]

def p_body(p):
	'body : terminals PYCODE'
	p[0] = [p[1], p[2]]
	
def p_terminals(p):
	'''terminals : terminal terminals
				 | terminal'''
	if len(p) == 3:
		p[0] = [p[1]] + p[2]
	else:
		p[0] = [p[1]]
		
def p_leftsymb(p):
	'leftsymb : SYMBOL'
	p[0] = p[1]

def p_terminal(p):
	'terminal : SYMBOL'
	p[0] = p[1]
	
def p_error(what):
	print ("What?"+str(what))

# Build the parser
parser = yacc.yacc()

