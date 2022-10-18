import pytest

import numpy as np

from constants import pi

from simple_functions import my_sum
from simple_functions import factorial


class TestSimpleFunctions(object):
    '''Class to test our simple functions are working correctly'''

    @pytest.mark.parametrize('iterable, expected', [
        ([8, 7, 5], 20),
        ((10, -2, 5, -10, 1), 4)
    ])
    def test_my_add(self, iterable, expected):
        '''Test our add function'''
        isum = my_sum(iterable)
        assert isum == expected

    @pytest.mark.parametrize('number, expected', [
        (5, 120),
        (3, 6),
        (1, 1)
    ])
    def test_factorial(self, number, expected):
        '''Test our factorial function'''
        answer = factorial(number)
        assert answer == expected


class TestPi(object):
    '''Class to test our constants are computed correctly'''

    def test_pi(self):
        '''Test computation of pi'''
        my_pi = pi(2)
        assert np.isclose(my_pi, np.pi, atol=1e-12)
