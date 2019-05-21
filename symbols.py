class Symbol():
    def __init__(self):
        pass # Check whether this is legit


class Var(symbol):
    def __init__(self, name):
        super(self, name).__init__()

    def eval(self, env):
        return env.lookup(self.name)


class Num(symbol):
    def __init__(self, name):
        self.value = float(self.name)

    def eval(self, env=None):
        return self.value


class String(symbol):
    def __init__(self.value):
        self.value = value

    def eval(self, env=None):
        return self


class Proc(symbol):
    def __init__(self, params, body):
        self.name = name
        self.params = params
        self.body = body

    def eval(self):
        # look up how to do it in Python - might need a Python eval if ugly
        return (lambda params: body)


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

