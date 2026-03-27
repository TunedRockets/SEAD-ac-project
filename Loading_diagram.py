from CG_calculations import CG, lemac
import matplotlib.pyplot as plt
import numpy as np

W_pay = 11966 #kg
W_empty = 23133
mac = 3.48
x_empty = (CG - lemac) /mac


n_pas = 100
W_pas = 92 #kg

#Cargo weights and lengths
W_aft = 1807
W_forward = 962
W_both = W_aft + W_forward
l_forward = 10.5
l_aft = 29.0
W_cargo = n_pas*W_pas + W_aft + W_forward


l_tank = 0
W_fuel = 5842


l_1st_seat = 6.84 # m
l_2nd_seat = l_1st_seat + 0.9 # 0.9 space per row

#Loading diagram for cargo
x_aft = ((((W_empty * CG) + (W_aft * l_aft)) / (W_empty + W_aft)) - lemac) / mac
x_forward = ((((W_empty * CG) + (W_forward * l_forward)) / (W_empty + W_forward)) - lemac)/mac
x_both = ((((W_empty * CG) + (W_forward * l_forward) + (W_aft * l_aft)) / (W_empty + W_forward + W_aft)) - lemac)/mac
print(x_aft, x_forward)
plt.plot([x_forward, x_empty, x_aft, x_both, x_forward], [W_forward+W_empty, W_empty, W_aft+W_empty, W_both+W_empty, W_forward+W_empty], '-o', color='deeppink')
plt.show()