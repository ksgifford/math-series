def fibonacci(n):
    '''Return index[n] of Fibonacci series, accounting for initial values.'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    '''Return index[n] of Lucas series, accounting for initial values.'''
    if n == 0:
        return 2
    elif n == 1:
        return 1
    elif n > 1:
        return lucas(n-1) + lucas(n-2)


def sum_series(n, val1=0, val2=1):
    '''Return index[n] of any series based on Fibonacci and Lucas formula.'''
    if n == 0:
        return val1
    elif n == 1:
        return val2
    elif n > 1:
        return (sum_series(n-1, val1, val2) + sum_series(n-2, val1, val2))
