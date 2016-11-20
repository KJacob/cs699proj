from test import calc
import customparser

def factor_tail(x):
    if x is [None]:
        return x
    if x[2][0] == '*':
        return [x[0], x[1] * x[2][1]]
    else:
        return [x[0], x[1] / x[2][1]]
        
def factor_factortail(x):
    if x[1][0] == '*':
        return x[0] * x[1][1]
    else:
        return x[0] / x[1][1]
def term_termtail(x):
    if x is [None]:
        return x
    
    if x[2][0] == '+':
        return [x[0], x[1] + x[2][1]]
    else:
        return [x[0], x[1] - x[2][1]]
        
def term(x):
    if x[1][0] == '+':
        return x[0] + x[1][1]
    else:
        return x[0] - x[1][1]

call_dict = {0: lambda x: None,
             1: lambda x: None,
             2: lambda x: None,
             3: lambda x: print(x[0]),
             4: lambda x: term(x),
             5: lambda x: term_termtail(x),
             6: lambda x: ['+', 0],
             7: lambda x: factor_factortail(x),
             8: lambda x: factor_tail(x),
             9: lambda x: ['*', 1],
             10: lambda x: x[1],
             11: lambda x: x[0],
             12: lambda x: int(x[0]),
             13: lambda x: x[0],
             14: lambda x: x[0],
             15: lambda x: x[0],
             16: lambda x: x[0]
             }
grammar = ""
with open('./test/calc.px', 'r') as f:
    grammar = f.read()

calc.lexer.tokens = calc.tokens
parse_obj = customparser.get_parser(grammar, call_dict, calc.lexer)

while True:
    calc.lexer.input(input())
    parse_obj.do_parse()
