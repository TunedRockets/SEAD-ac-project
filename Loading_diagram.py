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

l_tank = 29
W_fuel = 5842



#Loading diagram for cargo
x_aft = ((((W_empty * CG) + (W_aft * l_aft)) / (W_empty + W_aft)) - lemac) / mac
x_forward = ((((W_empty * CG) + (W_forward * l_forward)) / (W_empty + W_forward)) - lemac)/mac
x_both = ((((W_empty * CG) + (W_forward * l_forward) + (W_aft * l_aft)) / (W_empty + W_forward + W_aft)) - lemac)/mac
#print(x_aft, x_forward)


#Passenger weights and lengths
l_1 = 6.84 - lemac # m
x_window = [x_both,]
w_window = [W_empty+W_both,]
x_window_two = [x_both,]
w_window_two = [W_empty+W_both,]
M_n = (W_empty+W_both)*x_both 
# forward window
for n in range(24):
    l_n = l_1 + 0.8*n # 0.8 space per row
    w_n = (W_empty+W_both) + W_pas*2*n
    M_n = M_n + 2*W_pas*l_n
    x_n = (M_n/w_n)
    x_window.append(x_n)
    w_window.append(w_n)


M_n = (W_empty+W_both)*x_both 
l_n = l_n + 0.8
for n in range(24):
    l_n = l_n - 0.8 # 0.8 space per row
    w_n = (W_empty+W_both) + W_pas*2*n
    M_n = M_n + 2*W_pas*l_n
    x_n = (M_n/w_n)
    x_window_two.append(x_n)
    w_window_two.append(w_n)

x_aisle = [x_window_two[-1],]
w_aisle = [w_window_two[-1],]
x_aisle_two = [x_window_two[-1],]
w_aisle_two = [w_window_two[-1],]
w_n_init = np.copy(w_n)
M_n_init = np.copy(M_n)
for n in range(24):
    l_n = l_1 + 0.8*n # 0.8 space per row
    w_n = w_n_init + W_pas*2*n
    M_n = M_n + 2*W_pas*l_n
    x_n = (M_n/w_n)
    x_aisle.append(x_n)
    w_aisle.append(w_n)

M_n = M_n_init
l_n = l_n + 0.8
for n in range(24):
    l_n = l_n - 0.8 # 0.8 space per row
    w_n = w_n_init + W_pas*2*n
    M_n = M_n + 2*W_pas*l_n
    x_n = (M_n/w_n)
    x_aisle_two.append(x_n)
    w_aisle_two.append(w_n)

W_last = w_aisle_two[-1]
x_last = x_aisle_two[-1]
print(W_last, x_last)

x_fuel = (((W_fuel * (l_tank - lemac)) + (W_last * x_last)) / (W_fuel + W_last)) /mac
W_final = W_last + W_fuel

print(x_fuel, W_final)
plt.plot([x_forward, x_empty, x_aft, x_both, x_forward], [W_forward+W_empty, W_empty, W_aft+W_empty, W_both+W_empty, W_forward+W_empty], '-o', color='deeppink', label = 'Cargo')
plt.plot(x_window, w_window, '-o', color = 'darkviolet', label = 'Window seats')
plt.plot(x_window_two, w_window_two, '-o', color = 'darkviolet')
plt.plot(x_aisle, w_aisle, '-o', color = 'violet', label ='Aisle seats')
plt.plot(x_aisle_two, w_aisle_two,'-o', color = 'violet')
plt.plot([x_last, x_fuel], [W_last, W_final], '-o', color='cyan', label = 'Fuel')
plt.title("Loading diagram")
plt.ylabel("Weight")
plt.xlabel("Cg [mac]")
plt.legend()
plt.show()

#Finding most aft and most forward cg
min_cg = min(x_aisle)
max_cg = max(x_window_two)
print("min", min_cg, "max", max_cg)
