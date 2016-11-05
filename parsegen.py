import parse
import sys
import lex

#file_name = sys.argv[1]
file_name = 'gramm'
dollar = '$'
epsilon = 'eps'

with open(file_name, 'r') as fp:
    parse_input = fp.read()

parse.parser.parse(parse_input)
lex.lexer.input (parse_input)
print (parse.rules_list)
tkn = list(lex.lexer) + [dollar, dollar]

#lex.lexer.input (parse_input)

#for token in lex.lexer:
#    print (token)

def do_parse(lex_input):
    lex_input.input(parse_input)
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
        pass

def make_parse_table(rules, tokens):

    left_symb = []
    for rule in rules:
        left_symb.append(rule[0])
    left_symb = set(left_symb)

    non_terminals = []
    for rule in rules:
        for item in rule[1][0]:
            non_terminals.append(item)
    non_terminals = set(non_terminals) - set(tokens)

    symbols = left_symb | non_terminals
    tokens  = set(tokens)

    first_dict = dict()
    follow_dict = get_follow(symbols, rules, tokens)

    for symbol in symbols:
        first_dict[symbol] = get_first(symbol, rules, tokens)

    parse_table = dict()
    for symbol in symbols:
        parse_table[symbol] = dict()

    for i, rule in enumerate(rules):
        for term in first_dict[rule[0]]:
            first_alpha = get_body_first(rule[1][0], first_dict, tokens)
            for elem in first_alpha:
                if elem is not epsilon:
                    if elem in parse_table[rule[0]] and parse_table[rule[0]][elem] != i:
                        raise AmbiguousGrammarError
                    parse_table[rule[0]][elem] = i
                else:
                    for item in follow_dict[rule[0]]:
                        if item in parse_table[rule[0]] and parse_table[rule[0]][item] != i:
                            raise AmbiguousGrammarError
                        parse_table[rule[0]][item] = i
    return parse_table



def get_first(symbol, rules, tokens, depth = 0):
    first = set()
    if depth > len(rules):
        raise LeftRecursion
    for rule in rules:
        temp_set = set()
        if rule[0] == symbol:
            for non_term in rule[1][0]:
                if non_term in tokens:
                    temp_set.add(non_term)
                    if epsilon in temp_set:
                        temp_set.remove(epsilon)
                    break
                else:
                    temp = get_first(non_term, rules, tokens, depth + 1)
                    if epsilon not in temp:
                        temp_set |= temp
                        if epsilon in temp_set:
                            temp_set.remove(epsilon)
                        break
        first |= temp_set
    return first

def get_follow(symbols, rules, tokens):
    follow = dict()
    for symbol in symbols:
        follow[symbol] = set()
    start_symb = rules[0][0]
    follow[start_symb] |= {dollar}

    temp_follow = follow
    while True:
        for rule in rules:
            last_symb = rule[1][0][-1]
            if last_symb not in tokens:
                temp_follow[rule[0]] |= temp_follow[last_symb]
            prev = None
            for item in rule[1][0]:
                if item in tokens and prev is not None:
                    temp_follow[prev] |= item
        if temp_follow == follow:
            break
        follow = temp_follow
    return follow

def get_body_first(body, first_dict, tokens):
    body_first = set()
    for term in body:
        if term in tokens:
            body_first.add(term)
            break
        else:
            body_first |= first_dict[term]
            if epsilon not in first_dict[term]:
                break
    return body_first

tokens = (
    'PLUS','STAR',
    'LB','RB',
    )


def test():
    print (make_parse_table(parse.rules_list, tokens))

test()
