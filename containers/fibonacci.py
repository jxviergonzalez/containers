
##################################################
# example fibonacci number code;
# you do not have to modify this code in any way
###################################################


def fibs(n):
    '''
    This function computes the first n fibonacci numbers.
    Notice that this function uses O(n) memory.
    '''
    fibs = []
    fibs.append(1)
    if n == 1:
        return fibs
    fibs.append(1)
    while len(fibs) < n:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


def fib_bad(n):
    '''
    This function computes the n-th fibonacci number,
    but it uses O(n) memory to do so,
    which is bad.
    '''
    return fibs(n)[-1]


def fib(n):
    '''
    This function computes the n-th fibonacci number,
    but it consumes only O(1) memory,
    and is optimal.
    '''
    if n < 2:
        return 1
    f0 = 1
    f1 = 1
    for i in range(n - 1):
        f2 = f1 + f0
        f0 = f1
        f1 = f2
    return f2


####################################################
# fibonacci number code using generators;
# you will need to implement the functions below
####################################################


class Fib:
    '''
    This class represents all the fibonacci numbers,
    but uses O(1) memory to do so.

    >>> list(Fib(5))
    [1, 1, 2, 3, 5]
    '''
    def __init__(self, n=None):
        self.n = n

    def __repr__(self):
        if self.n is not None:
            return f'Fib({self.n})'
        else:
            return 'Fib()'

    def __iter__(self):
        return FibIter(self.n)


class FibIter:
    '''
    This is the iterator helper class for the Fib class.
    '''
    def __init__(self, n=None):
        self.n = n
        self.i = 0
        self.f0 = 0
        self.f1 = 1

    def __next__(self):
        if self.n is not None and self.i >= self.n:
            raise StopIteration
        else:
            self.i += 1
            if self.i < 2:
                return 1
            self.f2 = self.f0 + self.f1
            self.f0 = self.f1
            self.f1 = self.f2
            return self.f2


def fib_yield(n=None):
    '''
    This function returns a generator that computes
    the first n fibonacci numbers.
    If n is None, then the generator is infinite.
    '''
    f1 = 1
    f0 = 1

    if n is not None:
        if n >= 1:
            yield f0
        if n >= 2:
            yield f1
        for x in range(n - 2):
            f2 = f1 + f0
            f0 = f1
            f1 = f2
            yield f2
    if n is None:
        yield f0
        yield f1
        while True:
            f2 = f1 + f0
            f0 = f1
            f1 = f2
            yield f2
