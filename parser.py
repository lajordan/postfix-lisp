from tokenizer import tokenize

# arr = ['(', 'foo', '(', 'bar', 'y', '(', 'yeet', 'z', ')', ')', 'x', 'w', ')']
# arr2 = ['(', 'foo', '(', 'bar', 'y', ')', 'x', ')', '(', 'yeet', 'w', ')']

test = '(define square\n(lambda (x) (* x x)))'

def parse_inner(tokens, index=0, sofar=[]):
    if index < len(tokens):
        token = tokens[index]
        if token == '(':
            parsed_this, i_this = parse_inner(tokens, index + 1, [])
            new_sofar = sofar + [parsed_this]
            parsed_after, i_after = parse_inner(tokens, i_this, new_sofar)
            return parsed_after, i_after
        elif token == ')':
            return sofar, index + 1
        else:
            parsed, i = parse_inner(tokens, index + 1, sofar + [token])
            return parsed, i
    return sofar, index


def parse(tokens):
    parsed_inner = parse_inner(tokens)
    return parsed_inner[0]

# print(parse(tokenize(test)))

"""
TODO:
Implement real Lisp quoting and backquoting/escaping
Implement cond special form
Implement map, filter, reduce
Debug/test
Implement amb
Implement some other kind of concurrency/parallelization
Probabilistic programming
And, or, <, , etc.
Repl
Display
Define syntactic sugar (define x y (foo))
"""

