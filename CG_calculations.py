import numpy as np


#---------------------
# weights (1.cI)
#---------------------
EOW = 23133 # kg
W_w = 0.197*EOW # wing weight
W_h = 0.025*EOW # horizontal tail weight
W_v = 0.018*EOW # vertical tail weight
W_f = 0.35*EOW # fuselage weight
W_mg = 0.058*EOW # main landing gear weight
W_ng = 0.008*EOW # nose landing gear weight
W_p = 0.133*EOW # propulsion weight
W_c = 0.023*EOW # cockpit weight
# missing 8.8% of the EOW, does not affect cg apperantly

fus_group_W = np.array([W_h, W_v, W_f, W_ng, W_c, W_p])
wing_group_W = np.array([W_w, W_mg])

print("fuselage:", sum(fus_group_W))
print("wing:", sum(wing_group_W))

lemac = 22.866
#---------------------------------------
# locations wrt nose for fuselage group
#---------------------------------------

l_h = 39.133-4.04 # front of horizontal tail location
l_v = 35 # vertical tail location, made up
l_f = 36.466/2 # middle fuselage location
l_ng = 1.5 # nose landing gear location, made up
l_c = 1.5 # cockpit location (maybe assume same as nose gear), made up
l_p = 28.6 + 1.09
fus_group_l = np.array([l_h,l_v,l_f,l_ng,l_c, l_p])
#------------------------------------------------------------
# locations wrt lemac (in front -, behind +) for wing group
#------------------------------------------------------------
l_w = 3.48/2 # wing location
l_mg = 18.8 - lemac # main landing gear location

wing_group_l = np.array([l_w, l_mg])
#-------------------
# CG calculation
#-------------------

CG_wing = np.dot(wing_group_W, wing_group_l)/sum(wing_group_W)
CG_fus = np.dot(fus_group_W, fus_group_l)/sum(fus_group_W)


print("CG wing:", CG_wing)
print("CG fuselage:", CG_fus)
