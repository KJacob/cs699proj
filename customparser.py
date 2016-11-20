#Assume that we have LL(1) parsing table and rules.

import functools
import parsegen
import parse

CODE = 0
TERMINAL = 1
NON_TERMINAL = 2

class DOLLAR:
    def __init__(self):
        self.type = '$'
        self.value = '$'
    
#grammar -> string
def get_parser(grammar, call_dict, lexer):
    parse.parser.parse(grammar)
    parse_table = parsegen.make_parse_table(parse.rules_list, lexer.tokens)
    parser_obj = CustomParser(parse_table, lexer, parse.rules_list, call_dict)
    return parser_obj

class CustomParser:
    def __init__(self, parse_table, lexer, rules_list, call_dict):
        self.parse_table = parse_table
        self.rules_list = rules_list
        self.call_dict = call_dict
        self.terminals = lexer.tokens
        self.lexer = lexer
    
    def do_parse(self):
        start_symb = parse.rules_list[0][0]  
        parse_stack = []
        parse_stack.append((NON_TERMINAL, start_symb))
        value_stack = []
        input_tokens = list(self.lexer) + [DOLLAR()]
        next_token = input_tokens.pop(0)
        
        #The stack has been initialized
        while len(parse_stack) > 0:
            curr_symbol = parse_stack.pop()
            
            if curr_symbol[0] == CODE:
                n_values = curr_symbol[2]
                arg_list = value_stack[-n_values:]
                ret_val = curr_symbol[1](arg_list)
                if n_values != 0:
                    value_stack = value_stack[0:-n_values]
                value_stack.append(ret_val)
                continue
            
            if curr_symbol[0] == TERMINAL:
                value_stack.append(next_token.value)
                next_token = input_tokens.pop(0)
                continue
            
            if curr_symbol[1] == 'EPS':
                continue
            rule = self.parse_table[curr_symbol[1]][next_token.type]
            
            symb_to_push = self.rules_list[rule][1][0]
            
            symb_to_push = list(map (lambda x: (TERMINAL, x) if x in self.terminals else (NON_TERMINAL, x), symb_to_push))
            symb_to_push.append((CODE, self.call_dict[rule], len(symb_to_push)))
            
            symb_to_push = list(reversed(symb_to_push))
            
            if (NON_TERMINAL, 'EPS') in symb_to_push:
                parse_stack.append((CODE, self.call_dict[rule], 0))
                continue
            parse_stack += symb_to_push
            
