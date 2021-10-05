from controle import digital_controller

Q1_num = [10, 5]
Q1_den = [1, -1.2, .2]
Q1 = digital_controller(Q1_num, Q1_den)

Q1.X_k()
Q1.partfrac()
Q1.IZT()