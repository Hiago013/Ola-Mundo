import numpy as np
from sympy import log, ln, sin, cos, tan, exp, var, Lambda

class EDO:
    def __init__(self, dy, y0, x0):
        self._dy = dy
        self._y0 = y0
        self._x0 = x0

    def euler(self, I, N = 5, dp = 4):
        x0 = self._x0
        y0 = self._y0
        dy = self._dy
        h = (I[1] - self._x0) / N
        aux = x0
        y = np.empty(N+1, dtype=float)
        x = np.empty(N+1, dtype=float)
        x[0] = x0
        y[0] = y0
        k = 0
        while aux < I[1]:
            y_aux = y[k] + h * dy(aux, y[k])
            aux += h
            k += 1
            x[k] = aux
            y[k] = y_aux
        y = np.round(y, dp)
        return (y[-1], y, x)

# Exemplo de como usar a classe EDo
# x = var('x')
# y = var('y')
# x0 = 0
# y0 = 3
# dy = Lambda((x, y), -.06 * y**.5)
# I = (0, 2)
# N = 8

# Y = EDO(dy, y0, x0)
# y1, y_steps, x_steps = Y.euler(I, N, dp=4)
# print(y1)