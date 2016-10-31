import parse
import sys
import lex

file_name = sys.argv[1]

with open(file_name, 'r') as fp:
	parse_input = fp.read()

parse.parser.parse(parse_input)

print (parse.rules_list)

#lex.lexer.input (parse_input)

#for token in lex.lexer:
#	print (token)

