arr = ['(', 'foo', '(', 'bar', 'y', '(', 'yeet', 'z', ')', ')', 'x', 'w', ')']
arr2 = ['(', 'foo', '(', 'bar', 'y', ')', 'x', ')', '(', 'yeet', 'w', ')']


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

print(parse(arr))

"""
TODO:
Implement lambda
Implement is_number
Implement is_string
Make list of builtin operations
Initialize global environment with builtins
Implement operator class?
Turn apply into whatever it should be
Set up all the imports
Implement eq? builtin
Implement actual Lisp quoting (probably in parser, or even tokenizer)
Implement cons builtin
Implement car builtin
Implement cdr builtin
Implement atom? builtin
Implement cond special form
Implement list builtin
Change list implementation to linked list
Make it all postfix
"""

