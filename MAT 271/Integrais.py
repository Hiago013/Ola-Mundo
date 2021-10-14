import numpy as np
from sympy import var, Lambda, exp, log, sin, cos, tan, sqrt, diff, solve

class Integrais:
    
    def __init__(self, f, a, b):
        self._f = f
        self._a = a
        self._b = b

    def erro_trp(self):
        var('x')
        t = np.linspace(self._a, self._b, 100)
        df2 = Lambda(x, diff(diff(self._f(x))))
        t_val = np.array(np.absolute([df2(i) for i in t]))
        t_max = t_val.max()
        return np.float64(t_max)
    
    def erro_spn1_3(self):
        var('x')
        t = np.linspace(self._a, self._b, 100)
        df4 = diff(self._f(x), x)
        for i in range(3):
            df4 = diff(df4, x)
        df4 = Lambda(x, df4)
        t_val = np.array(np.absolute([df4(i) for i in t]))
        t_max = t_val.max()
        return np.float64(t_max)
        
    
    def trapezio(self, n = 2, dp = 4, erro=0.01, dupla=False):
        x = var('x')
        f = self._f
        a = self._a
        b = self._b
        h = (b - a) / n

        if dupla == True:
            print('*'*15,'Regra do Trapézio -- Integral Dupla', 15*'*')
            total = f(x, a) + f(x, b)
            n_aux = a + h
            while n_aux < b:
                total += (2 * f(x, n_aux))
                n_aux += h
            y = (h/2 * total)
            display(y)
            return Lambda(x, y)
        
        print('*'*15,'Regra do Trapézio', 15*'*')
        df2_max = self.erro_trp()
        n_min = (df2_max * (b - a)**3 / (12 * erro))**0.5
        n_min = np.ceil(n_min)
        total = f(a) + f(b)
        n_aux = a + h
        while n_aux < b:
            total += np.float64(2 * f(n_aux))
            n_aux += h
        y = np.float64(h/2 * total)

        E = h ** 2 /12 * (b - a) * df2_max

        y_round = np.round(y, dp)
        E_round = np.round(E, dp)


        print('Portanto a integral é:')
        print(y_round, f'com |E| < {E_round}\n')
        
        if E_round > erro:
            print('*' * 20, ' AVISO ', '*' * 20)
            print(f'Para garantia de um |E| < {erro}, utilize n = {n_min}\n')

        
        return y_round

    def simpson1_3(self, n=2, dp=4, erro=0.01, dupla = False):
        x = var('x')
        f = self._f
        a = self._a
        b = self._b
        h = (b - a) / n

        if dupla == True:
            print('*'*15,'Regra de 1/3 de Simpson -- Integral Dupla', 15*'*')
            total = f(x, a) + f(x, b)
            n_aux = a + h
            k = 1

            while n_aux < b:
                if k%2 == 0:
                    total += (2 * f(x, n_aux))
                else:
                    total += (4 * f(x, n_aux))
                k += 1
                n_aux += h
            display(h / 3 * (total))
            return Lambda(x, (h / 3 * (total)))
            
        
        print('*'*15,'Regra de 1/3 de Simpson', 15*'*')
        df4_max = self.erro_spn1_3()
        n_min = (df4_max * (b - a)**5 / (180 * erro))**0.25
        n_min = np.ceil(n_min)

        while n_min % 2 != 0:
            n_min += 1

        total = f(a) + f(b)
        n_aux = a + h
        k = 1
        
        while n_aux < b:
            if k%2 == 0:
                total += np.float64(2 * f(n_aux))
            else:
                total += np.float64(4 * f(n_aux))
            k += 1
            n_aux += h
            
        y = np.float64(h / 3 * (total))
        E = df4_max * (b - a ) * h ** 4 / 180
        
        y_round = np.round(y, dp)
        E_round = np.round(E, dp)
        print(f'Portanto, o valor da integral é:\n{y_round}, com |E| < {E_round}\n')
        
        if E_round > erro:
            print('*' * 20, ' AVISO ', '*' * 20)
            print(f'Para garantia de um |E| < {erro}, utilize n = {n_min}\n')
        
        return y_round

    def simpson3_8(self, n=3, dp=4, erro=0.01, dupla=False):
        x = var('x')
        f = self._f
        a = self._a
        b = self._b
        h = (b - a) / n

        if dupla == True:
            print('*'*15,'Regra de 3/8 de Simpson -- Integral Dupla', 15*'*')
            total = f(x, a) + f(x, b)
            n_aux = a + h
            k = 1
            
            while n_aux < b:
                if k%3 == 0:
                    total += (2 * f(x, n_aux))
                else:
                    total += (3 * f(x, n_aux))
                k += 1
                n_aux += h
            y = (3 / 8 * h  * (total))
            display(y)
            return Lambda(x, y)
        
        print('*'*15,'Regra de 3/8 de Simpson', 15*'*')
        df4_max = self.erro_spn1_3()
        n_min = (df4_max * (b - a)**5 / (80 * erro))**0.25
        n_min = np.ceil(n_min)
        
        while n_min % 3 != 0:
            n_min += 1
        total = f(a) + f(b)
        n_aux = a + h
        k = 1
        
        while n_aux < b:
            if k%3 == 0:
                total += np.float64(2 * f(n_aux))
            else:
                total += np.float64(3 * f(n_aux))
            k += 1
            n_aux += h
            
        y = np.float64(3 / 8 * h  * (total))
        E = df4_max * (b - a ) * h ** 4 / 80
        
        y_round = np.round(y, dp)
        E_round = np.round(E, dp)
        print(f'Portanto, o valor da integral é:\n{y_round}, com |E| < {E_round}\n')
        
        if E_round > erro:
            print('*' * 20, ' AVISO ', '*' * 20)
            print(f'Para garantia de um |E| < {erro}, utilize n = {n_min}\n')
        
        return y_round


        def verify_improp(self):
            x = var('x')
            a = self._a
            b = self._b
            f = self._f
            den = f(x).simplify().as_numer_denom()[1]
            






