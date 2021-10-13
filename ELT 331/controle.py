from control import tf, impulse_response, feedback, step_response
import matplotlib.pyplot as plt
from lcapy.discretetime import z
from sympy import apart, pprint, var
from numpy import arange, ones, linspace
import numpy as np

class digital_controller:
    def __init__(self, Xk = None, Xs = None, tau=1):
        self.tau = tau
        self.Gc = None
        if Xk != None:
            self.Xk = Xk
            num, den = Xk
            self.GkC = tf(num, den, tau)
            num_aux = den_aux = 0

            for grau in range(len(num)):
                num_aux += num[grau] * z ** (len(num) - grau -1)
            
            for grau in range(len(den)):
                den_aux += den[grau] * z ** (len(den) - grau -1)
            
            self.GkI = (num_aux / den_aux).simplify()
            self.GkS = apart( self.GkI )
        
        if Xs != None:
            s = var('s')
            self.Xs = Xs
            num, den = Xs
            self.GsC = tf(num, den)
            num_aux = den_aux = 0

            for grau in range(len(num)):
                num_aux += num[grau] * s ** (len(num) - grau -1)
            
            for grau in range(len(den)):
                den_aux += den[grau] * s ** (len(den) - grau -1)
            
            self.GsI = (num_aux / den_aux).simplify()
            self.GsS = apart( self.GsI/s )
    
    def __add__(self, *argsX):
        X = 0
        for item in argsX:
            X += item.GkI
        pprint((self.GkI + X).simplify())
        return (self.GkI + X)
    

    def X_k(self, k=4, plot=False):
        print('*' * 15, f'Os primeiros {k} resultados', '*' * 15)
        time , magnitude = impulse_response(self.GkC, T = arange(0, k, 1))
        for i in range(k):
            print(f'x({i}) = {magnitude[i]}')
        if plot == True:
            plt.style.use('ggplot')
            plt.stem(time[:k], magnitude[:k])
            plt.title(f'{k} primeiros resultados', fontfamily='monospace', fontweight='bold')
            plt.xlabel('k', fontsize=18, fontfamily='monospace')
            plt.ylabel('x(k)', fontsize=18, fontfamily='monospace')
            plt.tight_layout()
            # plt.grid()
            plt.show()
        print(' ')
        return time[:k], magnitude[:k]
    
    def partfrac(self, choose = 'k'):
        print('*' * 15, 'Expansão em frações parciais', '*' * 15 )
        if choose == 'k':
            pprint(self.GkS)
            print(' ')
            return self.GkS
        else:
            pprint(self.GsS)
            print(' ')
            return self.GsS
    
    def IZT(self):
        print('*' * 15, 'Inversa da transformada Z', '*' * 15)
        pprint(self.GkI.IZT())
        print(' ')
        return self.GkI.IZT()
    
    def sum(self, *args):
        X = 0
        for item in args:
            X += item.GkI
        pprint((X + self.GkI).simplify())
        return X + self.GkI
    
    def TZ(self, T_max=10):
        A = self.GsC.sample(self.tau)
        # print(A) -- preciso ajustar isso aqui
        T_amos = arange(0, T_max * self.tau + self.tau, self.tau)
        # print(feedback(A)) -- ajustar este também

        if self.Gc != None:
            print(A)
            print(self.Gc)
            B = A * self.Gc

        time, mag = step_response(feedback(A), T = T_amos)
        t = linspace(0, len(time)-1, 1000)
        new_mag = []
        k = 0
        for valor in t:
            if valor-1 > k:
                k += 1
            new_mag.append(mag[k])
        # ---------- Imprime na tela x(k) até T_Max ---------- 
        #for i in arange(0, T_max + 1, 1):
        #    print(f'x({i}) = {mag[i]:.4f}')
        # ---------- Plotagem ---------- 
        plt.style.use('ggplot')
        plt.plot(t, new_mag, linewidth=2, color='red')
        plt.plot(t, ones(len(t)), color='black', alpha=.5, linewidth=2)
        plt.xlabel('Número de amostras', fontfamily='monospace', fontsize='18')
        plt.ylabel('Amplitude', fontfamily='monospace', fontsize='18')
        plt.tight_layout()
        plt.show()
    
    def Gs2Gk(self, Gs, K, dp=3):
        Gc = tf(Gs[0], Gs[1])
        Gc_zeros = Gc.zero()
        Gc_poles = Gc.pole()
        A = np.round(-np.exp(Gc_zeros[0] * self.tau), dp)
        B = np.round(-np.exp(Gc_poles[0] * self.tau), dp)
        C = np.round(( K * Gc_zeros[0]  * (1+B) ) / ( (1+A) * Gc_poles[0] ), dp)
        self.Gc = C * tf([1, A], [1, B], self.tau)
        return (C, tf([1, A], [1, B], self.tau))

G = digital_controller(Xs=([4], [1, 2, 0]), tau=.01)
G.Gs2Gk(([1, 4.41], [1, 18.4]), 41.7, 3)
G.TZ(200)



