lines = [line.split() for line in open("input.txt").read().split("\n")]
symbol_map = {}
symbol_cache = {}
for line in lines: symbol_map[line[-1]] = line[:-2]

def eval_symbol(symbol):
    if symbol[0].isdigit():
        return int(symbol)

    if symbol in symbol_cache:
        return symbol_cache[symbol]
    
    formula = symbol_map[symbol]
    if len(formula) == 1:
        value = eval_symbol(formula[0])
    elif len(formula) == 2: # NOT <...>
        value = ~eval_symbol(formula[1]) & 0xFFFF
    elif formula[1] == "AND":
        value = eval_symbol(formula[0]) & eval_symbol(formula[2])
    elif formula[1] == "OR":
        value = eval_symbol(formula[0]) | eval_symbol(formula[2])
    elif formula[1] == "LSHIFT":
        value = (eval_symbol(formula[0]) << int(formula[2])) & 0xFFFF
    elif formula[1] == "RSHIFT":
        value = eval_symbol(formula[0]) >> int(formula[2])
    
    symbol_cache[symbol] = value
    return value

print(eval_symbol("a"))
