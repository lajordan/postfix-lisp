class Pair():
    def __init__(self, car, cdr=None):
        self.car = car
        self.cdr = cdr


    def cons(self, other):
        if self.cdr is None:
            self.cdr = other
        else:
            cons(self.cdr, other)
        # tail of self should set its cdr to car of other
        # to avoid side effects, need a way to deep copy (maybe a method)

    def deep_copy(self, copy=None):
        if self.cdr is None:
            return Pair(copy, None)
        else:
            return Pair(self.car, )