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



#Loading diagram for cargo
x_aft = ((((W_empty * CG) + (W_aft * l_aft)) / (W_empty + W_aft)) - lemac) / mac
x_forward = ((((W_empty * CG) + (W_forward * l_forward)) / (W_empty + W_forward)) - lemac)/mac
x_both = ((((W_empty * CG) + (W_forward * l_forward) + (W_aft * l_aft)) / (W_empty + W_forward + W_aft)) - lemac)/mac
#print(x_aft, x_forward)


#Passenger weights and lengths
l_1 = 6.84 # m
x_window = []
w_window = []
M_n = (W_empty+W_both)*x_both
# forward window
for n in range(1,24):
    l_n = l_1 + 0.8*n # 0.8 space per row
    w_n = (W_empty+W_both) + W_pas*2*n
    M_n =+ 2*W_pas*l_n
    x_n = (M_n/w_n ) /mac
    x_window.append(x_n)
    w_window.append(w_n)






plt.plot([x_forward, x_empty, x_aft, x_both, x_forward], [W_forward+W_empty, W_empty, W_aft+W_empty, W_both+W_empty, W_forward+W_empty], '-o', color='deeppink')
plt.scatter(x_window, w_window)
plt.show()