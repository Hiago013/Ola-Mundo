from control import tf, impulse_response
import matplotlib.pyplot as plt
from lcapy.discretetime import z
from sympy import apart


class digital_controller:
    def __init__(self, num, den, tau=1):
        
        self.GkC = tf(num, den, tau)
        num_aux = den_aux = 0

        for grau in range(len(num)):
            num_aux += num[grau] * z ** (len(num) - grau -1)
        
        for grau in range(len(den)):
            den_aux += den[grau] * z ** (len(den) - grau -1)
        
        self.GkS = apart( num_aux / den_aux )

    def X_k(self, k=4, plot=False):
        time , magnitude = impulse_response(self.GkC)
        for i in range(k):
            print(f'x({i}) = {magnitude[i]}')
        if plot == True:
            plt.stem(time[:k], magnitude[:k])
            plt.grid()
            plt.show()
        return time[:k], magnitude[:k]
    
    def partfrac(self):
        return self.GkS