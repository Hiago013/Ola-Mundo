from lcapy.discretetime import n, z
from lcapy import delta, s, t, exp
from control import tf, step_response, feedback
import numpy as np

class digital:
    def __init__(self, Xz = 1, Xk = 1, Gs=1, Gsc=1, tau=1):
        self._Xz = Xz
        self._Xk = Xk
        self._Gs = Gs
        self._Gsc = Gsc
        self._tau = tau
        self._fz = 1
        self._Gz = 1
    
    def izt(self):
        self._Xk = self._Xz(n)
        return self._Xz(n)

    def ztrans(self):
        self._Xz = self._Xk(z)
        return self._Xz 
    
    def calcn(self, m = 5):
        values = np.zeros(m, dtype=float)
        for k in range(m):
            aux_str = str(self._Xk.subs(n, k))
            if '/' in aux_str:
                for i in range(len(aux_str)):
                    if aux_str[i] == '/':
                        aux_str = str(float(aux_str[:i]) / float(aux_str[i+1:]))
                        break
            values[k] = np.float64(aux_str)

        return values

    def s2t(self):
        return self._Gs(t)
    
    def s2z(self):
        self._Gz = self._Gsc.sample(self._tau)
        return self._Gsc.sample(self._tau)
    
    def Fz(self, T_max = 10, fb=1):
        fz = feedback(self._Gz, fb)
        time, mag = step_response(fz, T_max)
        self._fz = fz
        return fz, time, mag




