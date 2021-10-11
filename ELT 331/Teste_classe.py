from controle import digital_controller
'''
print('- ' * 15,' Questão 01 ', '- ' * 15)
Q1_num = [10, 5]
Q1_den = [1, -1.2, .2]
Q1 = digital_controller((Q1_num, Q1_den))
Q1.X_k(5)

# ------------------------------------------ #
print('- ' * 15,' Questão 02 ', '- ' * 15)
Q2_num = [1, 2, 3, 4]
Q2_den = [1, 0, 0, 0]
Q2 = digital_controller((Q2_num, Q2_den))
Q2.X_k(5)
# ------------------------------------------ #
print('- ' * 15,' Questão 04 ', '- ' * 15)
Q4_num = [1, 1, 2]
Q4_den = [1, -2, 2, -1]
Q4 = digital_controller((Q4_num, Q4_den))
Q4.X_k(5)
# ------------------------------------------ #
print('- ' * 15,' Questão 05 ', '- ' * 15)
Q5_num = [2, 0, 1, 0]
Q5_den = [1, -5, 8, -4]
Q5 = digital_controller((Q5_num, Q5_den))
Q5.X_k(5)
# ------------------------------------------ #
print('- ' * 15,' Questão 06 ', '- ' * 15)
Q6_num_1 = [9, 0]
Q6_den_1 = [1, -4, 4]
Q6_num_2 = [-1, 0]
Q6_den_2 = [1, -2]
Q6_num_3 = [3, 0]
Q6_den_3 = [1, -1]
Q6_1 = digital_controller((Q6_num_1, Q6_den_1))
Q6_2 = digital_controller((Q6_num_2, Q6_den_2))
Q6_3 = digital_controller((Q6_num_3, Q6_den_3))
Q6_1.sum(Q6_2, Q6_3)
Q6_num = [2, 0, 1, 0]
Q6_den = [1, -5, 8, -4]
Q6 = digital_controller((Q6_num, Q6_den))
Q6.X_k(5)
# ------------------------------------------ #
print('- ' * 15,' Questão 07 ', '- ' * 15)
Q7_num = [1, 2]
Q7_den = [1, -2, 0 , 0]
Q7 = digital_controller((Q7_num, Q7_den))
Q7.X_k(6)
# ------------------------------------------ #
print('- ' * 15,' Questão 08 ', '- ' * 15)
Q8_num = [5, 0]
Q8_den = [1, 0, 1]
Q8 = digital_controller((Q8_num, Q8_den))

# ------------------------------------------ #
print('- ' * 15,' Questão 09 ', '- ' * 15)
Q9_num = [1, 0, 0, 0]
Q9_den = [2, -4, 3, -1]
Q9 = digital_controller((Q9_num, Q9_den))
Q9.partfrac()
Q9.X_k(8)
'''
# ------------------------------------------ #
print('- ' * 15,' Questão 13 ', '- ' * 15)
Q13_num = [1]
Q13_den = [1, 1, 0]
Q13 = digital_controller(Xs = (Q13_num, Q13_den), tau=1)
Q13.partfrac('s')
Q13.TZ(20)