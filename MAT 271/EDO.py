import numpy as np
from sympy import log, ln, sin, cos, tan, exp, var, Lambda, diff

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
        while k < N:
            y_aux = y[k] + h * dy(aux, y[k])
            aux += h
            k += 1
            x[k] = aux
            y[k] = y_aux
        y = np.round(y, dp)
        return (y[-1], y, x)

    def taylor2(self, I, N = 5, dp = 4):
        vx = var('x')
        vy = var('y')
        x0 = self._x0
        y0 = self._y0
        dy = self._dy
        fx = Lambda((vx, vy), diff(dy(vx, vy),  vx))
        fy =  Lambda((vx, vy), diff(dy(vx, vy),  vy))
        h = (I[1] - self._x0) / N
        aux = x0
        y = np.empty(N+1, dtype=float)
        x = np.empty(N+1, dtype=float)
        x[0] = x0
        y[0] = y0
        k = 0
        while k < N:
            y_aux = y[k] + h * dy(aux, y[k])
            ruge_kuta2 = h**2/ 2 * (fx(aux, y[k]) + fy(aux, y[k]) * dy(aux, y[k]))
            aux += h
            k += 1
            x[k] = aux
            y[k] = y_aux
        y = np.round(y, dp)
        return (y[-1], y, x)

    def runge_kutta2(self, I, N = 5, dp = 4):
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

        while k < N:
            k1 = dy(aux, y[k])
            k2 = dy(aux + h, y[k]+ h * k1)
            y_aux = y[k] + h/2 * (k1 + k2)
            aux += h
            k += 1
            x[k] = aux
            y[k] = y_aux
        y = np.round(y, dp)
        return (y[-1], y, x)
    
    def runge_kutta4(self, I, N = 5, dp = 4):
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

        while k < N:
            k1 = dy(aux, y[k])
            k2 = dy(aux + h/2, y[k] + h/2 * k1)
            k3 = dy(aux + h/2, y[k] + h/2 * k2)
            k4 = dy(aux + h, y[k] + h * k3)
            #print(k1, k2, k3, k4)
            y_aux = y[k] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
            #print(y_aux)
            aux += h
            k += 1
            x[k] = aux
            y[k] = y_aux
        y = np.round(y, dp)
        return (y[-1], y, x)

    def runge_kutta2z(self, dz, z0, I, N = 5, dp = 4):
        x0 = self._x0
        y0 = self._y0
        dy = self._dy
        h = (I[1] - self._x0) / N
        aux = x0
        y = np.empty(N+1, dtype=float)
        x = np.empty(N+1, dtype=float)
        z = np.empty(N+1, dtype=float)
        x[0] = x0
        y[0] = y0
        z[0] = z0
        k = 0

        while k < N:
            # parte do y
            k1 = dy(aux, y[k], z[k])
            k1z = dz(aux, y[k], z[k])
            k2 = dy(aux + h, y[k]+ h * k1, z[k] + h*k1z)
            k2z = dz(aux + h, y[k]+ h * k1, z[k] + h*k1z)
            y_aux = y[k] + h/2 * (k1 + k2)
            z_aux = z[k] + h/2 * (k1z + k2z)
            aux += h
            k += 1
            x[k] = aux
            y[k] = y_aux
            z[k] = z_aux
        y = np.round(y, dp)
        z = np.round(z, dp)
        return (y[-1], z[-1], y, z, x)
    
    def runge_kutta4z(self, dz, z0, I, N = 5, dp = 4):
        x0 = self._x0
        y0 = self._y0
        dy = self._dy
        h = (I[1] - self._x0) / N
        aux = x0
        y = np.empty(N+1, dtype=float)
        x = np.empty(N+1, dtype=float)
        z = np.empty(N+1, dtype=float)
        x[0] = x0
        y[0] = y0
        z[0] = z0
        k = 0

        while k < N:
            k1 = dy(aux, y[k], z[k])
            k1z = dz(aux, y[k], z[k])
            k2 = dy(aux + h/2, y[k] + h/2 * k1, z[k] + h/2 * k1z)
            k2z = dz(aux + h/2, y[k] + h/2 * k1, z[k] + h/2 * k1z)
            k3 = dy(aux + h/2, y[k] + h/2 * k2, z[k] + h/2 * k2z)
            k3z = dz(aux + h/2, y[k] + h/2 * k2, z[k] + h/2 * k2z)
            k4 = dy(aux + h, y[k] + h * k3, z[k] + h * k3z)
            k4z = dz(aux + h, y[k] + h * k3, z[k] + h * k3z)
            y_aux = y[k] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
            z_aux = z[k] + h / 6 * (k1z + 2 * k2z + 2 * k3z + k4z)
            #print(y_aux)
            aux += h
            k += 1
            x[k] = aux
            y[k] = y_aux
            z[k] = z_aux
        y = np.round(y, dp)
        z = np.round(z, dp)
        return (y[-1], z[-1], y, z, x)

#Exemplo de como usar a classe EDo
if __name__ == '__main__':
    x = var('x')
    y = var('y')
    z = var('z')
    x0 = 0
    y0 = 1
    z0 = 2
    dy = Lambda((x, y, z), z)
    dz = Lambda((x, y, z), -3*z -2*y + exp(x))
    I = (0, 0.4)
    N = 2
    Y = EDO(dy, y0, x0)
    res = Y.runge_kutta4z(dz, z0, I, N, dp=6)
    print(res[0], res[1])