class Proc():
    def __init__(self, params, body, env):
        self.params = params
        self.body = body
        self.env = env

    def __call__(self, args):
        new_env = Env(parent=self.env)
        if len(args) != len(params):
            raise ValueError('Wrong number of arguments')
        for i in range(len(params)):
            new_env.define_in_env(params[i], args[i])
        # apply body


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
            return parent.lookup(var_name)
        else:
            return KeyError('Unbound variable: %s' % var_name)

