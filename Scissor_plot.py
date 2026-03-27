import matplotlib.pyplot as plt
from CG_calculations import CG, lemac
from Loading_diagram import mac

# all values are made up

#wing
x_ac = lemac
C_L_a = 1
C_L_alpha_a = 1

#tail
x_ac_h = 37
l_h = x_ac_h - x_ac
C_L_h = 1
C_L_alpha_h = 1


V_h_V = 1
C_m_ac = 1
deps_dalpha = 1
SM = 0.1

S_h_S = [1,2,3,4]
X_cg1 = []
X_cg2 = []
X_cg3 = []


for s in S_h_S:

    X_cg1.append(((x_ac - C_m_ac/C_L_a + C_L_h/C_L_a *(s*l_h/mac)*V_h_V**2)-lemac)/mac) # controlability
    X_cg2.append(((x_ac + C_L_alpha_h/C_L_alpha_a*(1-deps_dalpha)*(s*l_h/mac)*V_h_V**2 - SM)-lemac)/mac) #stability
    X_cg3.append(((x_ac + C_L_alpha_h/C_L_alpha_a*(1-deps_dalpha)*(s*l_h/mac)*V_h_V**2)-lemac)/mac) # neutral stability



plt.plot(X_cg1,S_h_S)
plt.plot(X_cg2,S_h_S)
plt.plot(X_cg3,S_h_S)
plt.xlabel("X_cg/mac")
plt.ylabel("S_h/S")
plt.show()