import matplotlib.pyplot as plt
import numpy as np
from CG_calculations import CG, lemac, l_h
from Loading_diagram import mac
import Calculating_constants as cc

# all values are made up

#wing
x_ac = lemac + 0.25*mac
W_cruise = 38000
V_cruise = 242
C_L_a = W_cruise/(0.5*1*V_cruise**2*cc.S)
#C_L_alpha_a = 1.5

#tail
V_h_V = 0.85    # from slides
S_h = 15.9
S = 77.4  # confirm this #TODO
x_ac_h = l_h + 0.25*4.04
l_h = x_ac_h - x_ac
C_L_h = W_cruise/(0.5*1*(V_h_V*V_cruise)**2*S_h)
#C_L_alpha_h = 1.5

cm0 = 0.3        # entirely made up
flaps = 0.1       # also entirely made up, because the graph in the slides is incomprehensible
lf = 39.1
CL0 = 0.1       # again, entirely made up
C_m_ac = cm0*(cc.A*(np.cos(cc.lamb)**2)/(cc.A + 2*np.cos(cc.lamb))) + flaps - 1.8*(1 - 2.5*cc.bf/lf)*np.pi*cc.bf*cc.hf*lf/(4*cc.S*mac)*CL0/cc.Clah
#deps_dalpha = 0.4
SM = 0.5

S_h_S = [0.25, 0.5, 0.75, 1]
X_cg1 = []
X_cg2 = []
X_cg3 = []


for s in S_h_S:

    X_cg1.append(((x_ac + C_m_ac/C_L_a - C_L_h/C_L_a *(s*l_h/mac)*V_h_V**2)-lemac)/mac) # controlability
    X_cg2.append(((x_ac + cc.Clah/cc.Claw*(1-cc.depda)*(s*l_h/mac)*V_h_V**2 - SM)-lemac)/mac) #stability
    X_cg3.append(((x_ac + cc.Clah/cc.Claw*(1-cc.depda)*(s*l_h/mac)*V_h_V**2)-lemac)/mac) # neutral stability


if __name__ == "__main__":
    plt.plot(X_cg1,S_h_S, color='deeppink',label="Controlability")
    plt.plot(X_cg2,S_h_S, color='rebeccapurple', label='stability with safety margin')
    plt.plot(X_cg3,S_h_S, color='violet', label='stability without safety margin')
    plt.axhline(y=S_h/S, color='r', linestyle='--', linewidth=2)
    plt.xlabel("X_cg/mac")
    plt.ylabel("S_h/S")
    plt.legend()
    plt.show()
