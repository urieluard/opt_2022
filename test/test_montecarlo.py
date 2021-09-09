import pytest
import math
import montecarlo
import numpy as np


def test_integracion():
    f = lambda x, y: np.sqrt(x + y)
    a1 = 0
    b1 = 1
    a2 = 0
    b2 = 1
    obj = 2 / 3 * (2 / 5 * 2 ** (5 / 2) - 4 / 5)
    assert montecarlo.integracion(f, a1, b1, a2, b2) - obj < 0.01
