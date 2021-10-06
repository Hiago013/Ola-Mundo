from control import tf, impulse_response, feedback, step_response
import matplotlib.pyplot as plt
from lcapy.discretetime import z
from sympy import apart, pprint, var
from numpy import arange

class digital_controller:
    def __init__(self, Xk = None, Xs = None, tau=1):
        self.tau = tau
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
            self.GsS = apart( self.GsI )
    
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
    
    def TZ(self, T_max):
        A = self.GsC.sample(self.tau)
        print(A)
        T_amos = arange(0, T_max + 1, self.tau)
        print(feedback(A))
        time, mag = step_response(feedback(A), T = T_amos)
        plt.bar(T_amos - self.tau/2, mag, self.tau, edgecolor='black', color='white')
        plt.plot(T_amos, [1 for i in T_amos], color='black', alpha=.5, linewidth=2)
        plt.xlabel('Número de amostras', fontfamily='monospace', fontsize='18')
        plt.ylabel('Amplitude', fontfamily='monospace', fontsize='18')
        plt.show()


print('- ' * 15,' Questão 09 ', '- ' * 15)
Q7_num = [1]
Q7_den = [1, 1, 0]
Q7 = digital_controller(Xs = (Q7_num, Q7_den), tau=1)
# Q7.partfrac('s')
Q7.TZ(20)