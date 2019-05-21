test = '(define square\n(lambda (x) (* x x)))'


def int_convert(string):
    if string.isdigit():
        return int(string)
    return string


def tokenize(code):
    """
    Split code into lexemes (either strings or parentheses)
    Lexemes are separated by spaces or newlines (or parentheses)
    """
    lexemes = []
    current_lexeme = []
    for char in code:
        if char in ('(', ')'):
            if current_lexeme:
                lexemes.append(int_convert(''.join(current_lexeme)))
            lexemes.append(char)
            current_lexeme = []
        elif char in (' ', '\n'):
            if current_lexeme:
                lexemes.append(int_convert(''.join(current_lexeme)))
            current_lexeme = []
        else:
             current_lexeme.append(char)
    return lexemes

# print(tokenize(test))