import numpy as np


def integracion(
    f,
    a1,
    b1,
    a2,
    b2,
    ):
    density_p = int(10 ** 4)
    x_p = np.random.uniform(a1, b1, density_p)
    y_p = np.random.uniform(a2, b2, density_p)
    vol = (b1 - a1) * (b2 - a2)
    f_bar = np.mean(f(x_p, y_p))
    ex_1 = vol * f_bar
    return ex_1
