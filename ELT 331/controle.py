from control import tf, impulse_response
import matplotlib.pyplot as plt
from lcapy.discretetime import z
from sympy import apart, pprint
from numpy import arange

class digital_controller:
    def __init__(self, num, den, tau=1):
        
        self.GkC = tf(num, den, tau)
        num_aux = den_aux = 0

        for grau in range(len(num)):
            num_aux += num[grau] * z ** (len(num) - grau -1)
        
        for grau in range(len(den)):
            den_aux += den[grau] * z ** (len(den) - grau -1)
        
        self.GkI = (num_aux / den_aux).simplify()
        self.GkS = apart( self.GkI )
    
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
    
    def partfrac(self):
        print('*' * 15, 'Expansão em frações parciais', '*' * 15 )
        pprint(self.GkS)
        print(' ')
        return self.GkS
    
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
