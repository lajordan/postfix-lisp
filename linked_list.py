class Pair():
    def __init__(self, car, cdr=None):
        self.car = car
        self.cdr = cdr


def cons(x, y):
    return Pair(x, y)


def car(lst):
    return lst.car


def cdr(lst):
    return lst.cdr


def make_linked_list(arr):
    if not arr:
        return None
    else:
        return cons(arr[0], make_linked_list(arr[1:]))