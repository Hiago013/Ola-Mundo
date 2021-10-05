from control import tf
from controle import digital_controller

Xk_1 = tf([10, 5], [1, -1.2, 0.2], 1)
Q1 = digital_controller(Xk_1)
Q1.X_k(plot=True)