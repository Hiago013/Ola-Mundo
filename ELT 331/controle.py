from control import tf, impulse_response
import matplotlib.pyplot as plt
from lcapy.discretetime import z

class digital_controller:
    def __init__(self, Xz):
        self.Xz = Xz

    def X_k(self, k=4):
        time , magnitude = impulse_response(self.Xz)
        for i in range(k):
            print(f'x({i}) = {magnitude[i]}')
        plt.stem(time[:k], magnitude[:k])
        plt.grid()
        plt.show()