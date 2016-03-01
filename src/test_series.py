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


@pytest.mark.parametrize('n, result', FIBB_TABLE)
def test_fibbonacci(n, result):
    '''Test fibonacci function against defined FIBB_TABLE above.'''
    from series import fibonacci
    assert fibonacci(n) == result
