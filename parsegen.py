import sys
import lex
import copy

#file_name = sys.argv[1]
file_name = 'gramm'
dollar = '$'
epsilon = 'EPS'

#with open(file_name, 'r') as fp:
#    parse_input = fp.read()
#
#parse.parser.parse(parse_input)
#lex.lexer.input (parse_input)
#print (parse.rules_list)
#tkn = list(lex.lexer) + [dollar, dollar]

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
    tokens.add(epsilon)

    first_dict = dict()

    for token in tokens:
        first_dict[token] = token

    for symbol in symbols:
        first_dict[symbol] = get_first(symbol, rules, tokens)
        
    follow_dict = get_follow(symbols, rules, first_dict, tokens)

    parse_table = dict()
    for symbol in symbols:
        parse_table[symbol] = dict()

    for i, rule in enumerate(rules):
        for term in first_dict[rule[0]]:           
            first_alpha = get_body_first(rule[1][0], first_dict, tokens)
            for elem in first_alpha:
                if elem != epsilon:
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
                if non_term == epsilon:
                    temp_set.add(non_term)
                    break
                if non_term in tokens:
                    temp_set.add(non_term)
                    if epsilon in temp_set:
                        temp_set.remove(epsilon)
                    break
                else:
                    temp = get_first(non_term, rules, tokens, depth + 1)
                    temp_set |= temp
                    if epsilon not in temp:
                        if epsilon in temp_set:
                            temp_set.remove(epsilon)
                        break
        first |= temp_set
    return first

def get_follow(symbols, rules, first_dict, tokens):
    follow = dict()
    for symbol in symbols:
        follow[symbol] = set()
    start_symb = rules[0][0]
    follow[start_symb] |= {dollar}
    
    temp_follow = copy.deepcopy(follow)
    while True:
        for rule in rules:
            for i, term in enumerate(rule[1][0]):
                if term not in tokens:
                    if i == len(rule[1][0]) - 1:
                        temp_follow[term] |= temp_follow[rule[0]]
                        continue
                    remain_first = get_body_first(rule[1][0][i+1:], first_dict, tokens)
                    if epsilon in remain_first:
                        remain_first.remove(epsilon)
                        temp_follow[term] |= remain_first
                        temp_follow[term] |= temp_follow[rule[0]]
                        
                    else:
                        temp_follow[term] |= remain_first
        if temp_follow == follow:
            break
        follow = copy.deepcopy(temp_follow)

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

#tokens = (
#    'PLUS','STAR',
#    'LB','RB',
#    )


#def test():
#    print (make_parse_table(parse.rules_list, tokens))

#test()
