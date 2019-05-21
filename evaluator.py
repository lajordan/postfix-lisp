from . import symbols, parser, linked_list


builtins = {'+': sum,
            '-': lambda args: 0 - args[0] if len(args) == 1 else args[0] - sum(args[1:]),
            '*': lambda args: args[0] if len(args) == 1 else args[0] * builtins['*'](args[1:]),
            '/': lambda args: args[0] if len(args) == 1 else args[0] / builtins['*'](args[1:]),
            'cons': linked_list.cons,
            'car': lambda args: linked_list.car(args[0]),
            'cdr': lambda args: linked_list.cdr(args[0]),
            'list': linked_list.make_linked_list,
            'eq?': lambda args: all([args[i] == args[0] for i in args])
            }


def evaluate(expressions, env=None):
    if env is None:
        env = Env(parent=Env(builtins=builtins))

    if type(expressions) == list:
        tail = tokens[-1]

        if tail == 'let':
            new_bindings = tokens[0]
            new_env = Env(parent=env)
            for var_name, val in new_bindings:
                new_env.define_in_env(var_name, evaluate(val, env))
                # for let*, can just change the above to evaluate(val, new_env)
            expr = tokens[1]
            return evaluate(expr, new_env)

        elif tail == 'define':
            var_name = tokens[0]
            val = tokens[1]
            env.define_in_env(var_name, evaluate(val, env))

        elif tail == 'if':
            pred = tokens[0]
            if_true = tokens[1]
            if_false = tokens[2]
            if evaluate(pred, env):
                return evaluate(if_true, env)
            return evaluate(if_false, env)


        elif tail == 'lambda':
            params = tokens[0]
            body = tokens[1]
            return Proc(params, body, env)

        # else: # Not a special form
        #     return tail([evaluate(t) for t in tokens[1:]])

    elif expressions == '#t':
        return True

    elif expressions == '#f':
        return False

    elif type(expressions) in (int, str, bool):
        return expressions

    else:
        return env.lookup(expressions)

for expression in expressions[:-1]:
    evaluate(expression, env)
    return evaluate(expressions[-1], env)

