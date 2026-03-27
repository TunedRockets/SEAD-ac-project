import matplotlib.pyplot as plt
from CG_calculations import CG, lemac, l_h
from Loading_diagram import mac

# all values are made up

#wing
x_ac = lemac + 0.25*mac
S = 77.4
W_cruise = 38000
V_cruise = 242
C_L_a = W_cruise/(0.5*1*V_cruise**2*S)
C_L_alpha_a = 1.5

#tail
V_h_V = 0.9
S_h = 15.9
x_ac_h = l_h + 0.25*4.04
l_h = x_ac_h - x_ac
C_L_h = W_cruise/(0.5*1*(V_h_V*V_cruise)**2*S_h)
C_L_alpha_h = 1.5


C_m_ac = -1
deps_dalpha = 0.4
SM = 0.1

S_h_S = [1,2,3,4]
X_cg1 = []
X_cg2 = []
X_cg3 = []


for s in S_h_S:

    X_cg1.append(((x_ac - C_m_ac/C_L_a - C_L_h/C_L_a *(s*l_h/mac)*V_h_V**2)-lemac)/mac) # controlability
    X_cg2.append(((x_ac + C_L_alpha_h/C_L_alpha_a*(1-deps_dalpha)*(s*l_h/mac)*V_h_V**2 - SM)-lemac)/mac) #stability
    X_cg3.append(((x_ac + C_L_alpha_h/C_L_alpha_a*(1-deps_dalpha)*(s*l_h/mac)*V_h_V**2)-lemac)/mac) # neutral stability



plt.plot(X_cg1,S_h_S, label="1")
plt.plot(X_cg2,S_h_S)
plt.plot(X_cg3,S_h_S)
plt.xlabel("X_cg/mac")
plt.ylabel("S_h/S")
plt.legend()
plt.show()
