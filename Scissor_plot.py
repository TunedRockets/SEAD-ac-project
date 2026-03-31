import matplotlib.pyplot as plt
import numpy as np
from CG_calculations import lemac, l_h, mac, l_p


# all values are made up
part_2 = True

import Calculating_constants as cc

Ah = 3.94       # bs number
beta = np.sqrt(1 - (241.78889)*0.85/343)
lambh = 20*np.pi/180       # bs number
eta = 0.9       # bs number
Clah = 2*np.pi*Ah/(2 + np.sqrt(4 + (Ah*beta/eta)**2*(1 + (np.tan(lambh)**2/beta**2))))

A = 7.38
if part_2: A *= 1.25


lamb = 26.9*np.pi/180
Claw = 2*np.pi*A/(2 + np.sqrt(4 + (A*beta/eta)**2*(1 + (np.tan(lamb)**2/beta**2))))

bf = 2.7    #m
b = 26.2
S = 77.4
taper = 0.28        # actually for EMB 170 which is similar plane
SnetS = (S-bf*mac)/S #1 - (taper*(1-bf/b)+bf/b)*bf/b
Claf = Claw*(1+2.15*bf/b)*SnetS + np.pi/2*bf**2/S

#depda = 6.5*(np.sin(12*lamb))       # bs number, but based on Torenbeek
r = -l_h/(b/2)
mtv = 5.592

K1 = (0.1124+0.1265*lamb+0.1766*lamb**2)/r**2 + 0.1024/r +2
K2 = 0.1124/r**2 +0.1024/r + 2
depda = K1/K2 * ((r/(r**2+mtv**2)) * 0.4876/(np.sqrt(r**2+0.6319+mtv**2))+ (1+(r**2/(r**2 +0.7915 +5.0734*mtv**2))**0.3113)*(1-np.sqrt(mtv**2/(1+mtv**2))))*Claw/(np.pi*A)

print(depda)

hf = bf     #assuming circular fuselage
lfn = lemac
c = mac
cg = 2*taper*S/(b*(1+taper))
xacf = 0.26 - 1.8/Clah*bf*hf*lfn/(S*c) + 0.273/(1 + taper)*bf*cg*(b-bf)/(c**2*(b+2.15*bf))*lamb         #assuming half chord and chorter-chord sweep is same because I cant find half-chord
xacf = (xacf -lemac)/mac

xacn = -0.25*1.3**2*(l_p-lemac)/(S*Clah)*2
xacn = (xacn -lemac)/mac

MTOW = 36968*9.81 #40995
rho = 1.225 #0.25
v = 56 #0.8*np.sqrt(1.4*222*287)
Clmax = MTOW/(0.5*rho*v**2*S)
if part_2:
    Clmax *= 1.2


#wing
S = 77.4
x_ac = 0.25 #lemac + 0.25*mac
W_cruise = 38000*9.81
V_cruise = 242
rho = 0.25
C_L_a = W_cruise/(0.5*rho*V_cruise**2*S)
#C_L_alpha_a = 1.5

#tail
V_h_V = 1#0.85    # from slides
S_h = 15.9
x_ac_h = ((l_h + 0.25*4.04) -lemac)/mac
l_h = x_ac_h - x_ac
C_L_h = -0.8

#C_L_alpha_h = 1.5

cm0 = -0.3        # entirely made up
flaps = 0.5      # also entirely made up, because the graph in the slides is incomprehensible
lf = 39.1
CL0 = 1       # again, entirely made up
C_m_ac = cm0*(A*(np.cos(lamb)**2)/(A + 2*np.cos(lamb))) + flaps - 1.8*(1 - 2.5*bf/lf)*np.pi*bf*hf*lf/(4*S*mac)*CL0/Clah
#deps_dalpha = 0.4
SM = 0.05

S_h_S = [0, 0.25, 0.5, 0.75, 1]
X_cg1 = []
X_cg2 = []
X_cg3 = []


for s in S_h_S:

    X_cg1.append(x_ac - C_m_ac/C_L_a + C_L_h/C_L_a *(s*l_h/mac)*V_h_V**2)#-lemac)/mac) # controlability
    X_cg2.append(((x_ac + Clah/Claw*(1-depda)*(s*l_h/mac)*V_h_V**2 - SM)))#-lemac)/mac) #stability
    X_cg3.append(((x_ac + Clah/Claw*(1-depda)*(s*l_h/mac)*V_h_V**2)))#-lemac)/mac) # neutral stability


if __name__ == "__main__":
    plt.plot(X_cg1,S_h_S, color='deeppink',label="Controlability")
    plt.plot(X_cg2,S_h_S, color='rebeccapurple', label='stability with safety margin')
    plt.plot(X_cg3,S_h_S, color='violet', label='stability without safety margin')
    plt.axhline(y=S_h/cc.S, color='r', linestyle='--', linewidth=2, label='actual Sh/S')
    plt.xlabel("X_cg/mac")
    plt.ylabel("S_h/S")
    plt.grid()
    plt.legend()
    plt.show()
