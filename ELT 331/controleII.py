from lcapy.discretetime import n, z
from lcapy import delta, s, t, exp
from control import tf, step_response, feedback
import numpy as np
import matplotlib.pyplot as plt

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
    
    def Fz(self, T_max = 10, fb=1, plot=False, save=False):
        fz = feedback(self._Gz, fb)
        time, mag = step_response(fz, T_max * self._tau)
        self._fz = fz

        if plot == True:
            time_plot = np.linspace(0, len(time)-1, 1000)
            mag_plot = []
            k = 0
            for valor in time_plot:
                if valor-1 > k:
                    k += 1
                mag_plot.append(mag[k])
            mag_plot = np.array(mag_plot)
            plt.figure(figsize=(8, 5))
            plt.style.use('ggplot')
            plt.plot(time_plot, mag_plot, linewidth=2, color='red')
            plt.plot(time_plot, np.ones(len(time_plot)), color='black', alpha=.5, linewidth=2)
            plt.xlabel('Número de amostras', fontfamily='monospace', fontsize='18')
            plt.ylabel('Amplitude', fontfamily='monospace', fontsize='18')
            plt.tight_layout()

            if save == True:
                plt.savefig('fig.png', dpi=600)

            plt.show()

        return fz, time, mag

    def controlador(self, K, Gc, dp=6):
        num, den = Gc
        a = num[1]
        b = den[1]
        param = lambda x: np.exp(-self._tau * x)

        A = param(a)
        B = param(b)
        C = K * a * (1 - B) / (b * (1-A))

        return np.round( (A, B, C), dp)


    
if __name__ == '__main__':
    gss = 1/(10*s**3 + s**2)
    gsc = tf(1, [10, 1, 0])
    print(gsc)
    tau = .2
    Q16 = digital(Gs=gss, Gsc=gsc, tau = tau)
    print(Q16.s2z())
    print(Q16.s2t())
    val = Q16.Fz(200, plot=True)
    print(val[0])

    gcs = ([1, 0.1], [1, 2])
    K = 8
    print( Q16.controlador(K, gcs, 4) )

    #fz, time, mag = Q16.Fz(14, fb = 0.05)
    #print(mag)
    #display(fz)




