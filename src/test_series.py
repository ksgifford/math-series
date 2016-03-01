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
    (7, 29),

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
