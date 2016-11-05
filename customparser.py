#Assume that we have LL(1) parsing table and rules.

import functools

CODE = 0
TERMINAL = 1
NONTERMINAL = 2

class DOLLAR:
    self.type = '$'
    self.value = '$'

class CustomParser:
    __init__(self, lexer, parse_table, rules_list, call_dict, terminals):
        self.lexer = lexer
        self.parse_table = parse_table
        self.rules_list = rules_list
        self.call_dict = call_dict
        self.terminals = terminals
    
    def do_parse(parse_input):
        lexer.input(parse_input)
        start_symb = parse.rules_list[0][0]
        
        parse_stack = []
        parse_stack.append((NON_TERMINAL, start_symb))
        value_stack = []
        input_tokens = list(lexer.lexer) + [DOLLAR]
        
        #The stack has been initialized
        while len(parse_stack) > 0:
            curr_symbol = parse_stack.pop()
            
            if curr_symbol[0] == CODE:
                n_values = curr_symbol[2]
                arg_list = value_stack[-n:]
                ret_val = curr_symbol[1](arg_list)
                value_stack = value_stack[0:-n]
                value_stack.push(ret_val)
                continue
                
            next_token = input_tokens.pop(0)
            
            if curr_symbol[0] == TERMINAL:
                value_stack.push(next_token.value)
                continue
                
            rule = parse_table[curr_symbol][next_token.type]
            
            symb_to_push = rules_list[rule][0][0]
            symb_to_push = map (lambda x: (TERMINAL, x) if x in terminals else (NONTERMINAL, x), sym_to_push)
            symb_to_push.append((CODE, call_dict[rule], len(sym_to_push)))
            
            symb_to_push = list(reversed(symb_to_push))
            
            parse_stack += symb_to_push
            
