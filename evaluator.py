import parser, linked_list, tokenizer



builtins = {'+': sum,
            '-': lambda args: 0 - args[0] if len(args) == 1 else args[0] - sum(args[1:]),
            '*': lambda args: args[0] if len(args) == 1 else args[0] * builtins['*'](args[1:]),
            '/': lambda args: args[0] if len(args) == 1 else args[0] / builtins['*'](args[1:]),
            'cons': linked_list.cons,
            'car': lambda args: linked_list.car(args[0]),
            'cdr': lambda args: linked_list.cdr(args[0]),
            'list': linked_list.make_linked_list,
            'eq?': lambda args: all([args[i] == args[0] for i in range(len(args))])
            }


class Proc():
    def __init__(self, params, body, env):
        self.params = params
        self.body = body
        self.env = env

    def __call__(self, args):
        new_env = Env(parent=self.env)
        if len(args) != len(self.params):
            raise ValueError('Wrong number of arguments')
        for i in range(len(self.params)):
            new_env.define_in_env(self.params[i], evaluate(args[i], self.env)[0])
        return evaluate(self.body, new_env)[0]


class Env():
    def __init__(self, parent=None, bindings=None):
        self.parent = parent
        if bindings:
            self.bindings = bindings
        else:
            self.bindings = {}

    def define_in_env(self, var_name, val):
        self.bindings[var_name] = val

    def lookup(self, var_name):
        if var_name in self.bindings:
            return self.bindings[var_name]
        elif self.parent:
            return self.parent.lookup(var_name)
        else:
            return KeyError('Unbound variable: %s' % var_name)




def evaluate(expressions, env=None):
    if env is None:
        env = Env(parent=Env(bindings=builtins))

    if type(expressions) == list:
        tail = expressions[-1]

        if tail == 'let':
            new_bindings = expressions[0]
            new_env = Env(parent=env)
            for var_name, val in new_bindings:
                new_env.define_in_env(var_name, evaluate(val, env)[0])
                # for let*, can just change the above to evaluate(val, new_env)
            expr = expressions[1]
            return evaluate(expr, new_env)[0], env

        elif tail == 'define':
            var_name = expressions[0]
            val = expressions[1]
            env.define_in_env(var_name, evaluate(val, env)[0])
            return val, env

        elif tail == 'if':
            pred = expressions[0]
            if_true = expressions[1]
            if_false = expressions[2]
            if evaluate(pred, env)[0]:
                return evaluate(if_true, env)[0], env
            return evaluate(if_false, env)[0], env

        elif tail == 'lambda':
            params = expressions[0]
            body = expressions[1]

            procedure = Proc(params, body, env)
            return procedure, env

        else: # if it's just a regular function
            procedure = env.lookup(tail)
            try:
                result = procedure([evaluate(expr, env)[0] for expr in expressions[:-1]])
                return result, env
            except:
                raise TypeError('Not a function')


    elif expressions == '#t':
        return True, env

    elif expressions == '#f':
        return False, env

    elif type(expressions) in (int, bool):
        return expressions, env

    else:
        return env.lookup(expressions), env



def run(code):
    expressions = parser.parse(tokenizer.tokenize(code))
    print(expressions)
    env = None
    for expression in expressions[:-1]:
        env = evaluate(expression, env)[1]
    return evaluate(expressions[-1], env)


# sq_test = '(((square ((x) (x x *) lambda))) (3 square) let)'
# double_test = '(((double ((x) (x x +) lambda))) (3 double) let)'
# if_test = '((3 3 eq?) 1 0 if)'
with open('test.txt', 'r') as testfile:
    test = testfile.read()
    print('run_test_result:', run(test))

