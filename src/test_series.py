# -*- coding: utf-8 -*-
import pytest


FIBB_TABLE = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13)
]

LUCAS_TABLE = [
    (0, 2),
    (1, 1),
    (2, 3),
    (3, 4),
    (4, 7),
    (5, 11),
    (6, 18),
    (7, 29)
]

SUM_SERIES_TABLE = [
    (0, 0, 1, 0),
    (1, 0, 1, 1),
    (2, 0, 1, 1),
    (3, 0, 1, 2),
    (4, 0, 1, 3),
    (5, 0, 1, 5),
    (6, 0, 1, 8),
    (7, 0, 1, 13),
    (0, 2, 1, 2),
    (1, 2, 1, 1),
    (2, 2, 1, 3),
    (3, 2, 1, 4),
    (4, 2, 1, 7),
    (5, 2, 1, 11),
    (6, 2, 1, 18),
    (7, 2, 1, 29),
    (0, 3, 2, 3),
    (1, 3, 2, 2),
    (2, 3, 2, 5),
    (3, 3, 2, 7)
]


@pytest.mark.parametrize('n, result', FIBB_TABLE)
def test_fibbonacci(n, result):
    '''Test fibonacci function against defined FIBB_TABLE above.'''
    from series import fibonacci
    assert fibonacci(n) == result


@pytest.mark.parametrize('n, result', LUCAS_TABLE)
def test_lucas(n, result):
    '''Test lucas function against defined LUCAS_TABLE above'''
    from series import lucas
    assert lucas(n) == result


@pytest.mark.parametrize('n, val1, val2, result', SUM_SERIES_TABLE)
def test_sum_series(n, val1, val2, result):
    '''Test sum_series function against Lucas, Fibonacci and custom values.'''
    from series import sum_series
    assert sum_series(n, val1, val2) == result
