#Assume that we have LL(1) parsing table and rules.

#Parsing table : parse_table
#Rules list: rules_list

class CustomParser:
    self.parse_table = parse_table
    self.rules_list = rules_list
    
    __init__(self, lexer):
        self.lexer = lexer
    
    def do_parse(parse_input):
        lexer.input(parse_input)
        start_symb = parse.rules_list[0][0]
        
        parse_stack = []
        rule_stack = []
        parse_stack.append(start_symb)
        parse_table = make_parse_table(parse.rules_list, list(lex_input.tokens))
        tokens = list(lex_input.lexer()) + [dollar, dollar]
        
        for token in tokens:
            symb = parse_stack.pop()
            if token[0] not in parse_table[symb]:
                raise ParseError
            else:
                rule_index = parse_table[symb][token[0]]
                rule = parse.rules_list[rule_index]
                for item in reversed(rule[1][0]):
                    parse_stack.append(item)
                rule_stack.append(rule_index)

            #Remove the last dollar symbol.
        tokens.pop()

        value_stack = []
        rule_index = rules_stack.pop()
        rule = parse.rules_list[rule_index]
        value_stack = tokens[:-len(rule[0][1])]
        value_stack = [None] + value_stack


        while len(rule_stack) > 0:
