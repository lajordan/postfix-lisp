def tokenize(code):
    lexemes = []
    current_lexeme = []
    for char in code:
        if char in ('(', ')'):
            if current_lexeme:
                lexemes.append(''.join(current_lexeme))
            lexemes.append(char)
            current_lexeme = []
        elif char == ' ':
            if current_lexeme:
                lexemes.append(''.join(current_lexeme))
            current_lexeme = []
        elif char == '\n':
            pass
        else:
             current_lexeme.append(char)
    return lexemes