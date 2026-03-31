import numpy as np
import CG_calculations as cgc
from CG_calculations import mac, lemac
from Scissor_plot import l_h

##----------------------------------
#DONT WORK HERE PLS, JUST GO IN SCOSSOR PLOT
#--------------------------------------------
part_2 = False


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
lfn = cgc.lemac
c = cgc.mac
cg = 2*taper*S/(b*(1+taper))
xacf = 0.26 - 1.8/Clah*bf*hf*lfn/(S*c) + 0.273/(1 + taper)*bf*cg*(b-bf)/(c**2*(b+2.15*bf))*lamb         #assuming half chord and chorter-chord sweep is same because I cant find half-chord
xacf = (xacf -lemac)/mac

xacn = -0.25*1.3**2*(cgc.l_p-cgc.lemac)/(S*Clah)*2
xacn = (xacn -lemac)/mac

MTOW = 36968*9.81 #40995
rho = 1.225 #0.25
v = 56 #0.8*np.sqrt(1.4*222*287)
Clmax = MTOW/(0.5*rho*v**2*S)
if part_2:
    Clmax *= 1.2


if __name__ == "__main__":
    print(r"$V_c$&  470 kts\\")
    print(r"$V_s$&  140 kts\\")
    print(r"$\frac{V_h}{V}$& 0.85 \\")
    print(r"$C_{L_{\alpha,h}}$&", Clah, r"\\")
    print(r"$C_{L_{\alpha,w}}$ &", Claw, r"\\")
    print(r"$C_{L_{\alpha,f}}$&", Claf, r"\\")
    print(r"$\frac{d\varepsilon}{d\alpha}$ &", depda, r"\\")
    print(r"$x_{ac,w}$ &", 0.26, r"\\")     #from the graph in the slides
    print(r"$x_{ac,f}$ &", xacf, r"\\")
    print(r"$x_{ac,nacelle}$ &", xacn, r"\\")
    print(r"$C_{L_{max,h}}$ &",Clmax, r"\\")
    print(r"$\theta_{0,a-h}$ &")


