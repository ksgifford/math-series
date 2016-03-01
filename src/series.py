def fibonacci(n):
    '''Returns index[n] of Fibonacci series, accounting for initial values.'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    pass


def sum_series(n, val1, val2):
    pass
