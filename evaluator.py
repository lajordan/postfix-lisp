def evaluate(expressions, env):
    def evaluate_expr(tokens, env):
        if type(tokens) != list: # If the "expression" is just a symbol
            # Figure out the type of head
            return dispatch(tokens).eval(env)

        head = tokens[0]

        if head == 'let':
            new_bindings = tokens[1]
            new_env = Env(parent=env)
            for var_name, val in new_bindings:
                new_env.define_in_env(var_name, evaluate(val, env))
                # for let*, can just change the above to evaluate(val, new_env)
            expr = tokens[2]
            return evaluate_expr(expr, new_env)

        elif head == 'define':
            var_name = tokens[1]
            val = tokens[2]
            env.define_in_env(var_name, evaluate(val, env))

        elif head == 'lambda':
            params = tokens[1]
            new_env = Env(parent=env)

        else: # Not a special form
            # apply isn't a thing, look up the actual syntax
            return apply(evaluate_expr(head), [evaluate_expr(t) for t in tokens[1:]])

    for expression in expressions[:-1]:
        evaluate_expr(expression, env)
    return evaluate_expr(expressions[-1], env)


def dispatch(sym):
    if is_number(sym):
        return Num(sym)
    elif is_string(sym):
        return String(sym)
    else:
        return Var(sym)

