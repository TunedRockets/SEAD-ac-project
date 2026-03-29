import numpy as np


intom = 0.0254      #m/in

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

#print("fuselage:", sum(fus_group_W))
#print("wing:", sum(wing_group_W))

lemac = (900.257 - 144)*intom      #m
mac = 3.48 #m

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

CG = (np.dot(wing_group_W, (wing_group_l+lemac)) + np.dot(fus_group_W, fus_group_l))/(sum(wing_group_W)+sum(fus_group_W))

print(CG)



#------------
# Part 2
# ----------

'''Changes:
- wing weight -9%
- fuselage weight -7%
- 2 battery packs added:
    * 2025 kg in the most forward part of cargo hold, taking up 1300 L
    * 2475 kg in the aftmost part of the aft cargo hold, for 1600L
    * installation adds 4000 kg to weight (500 kg reused?)
- 3 last pax rows removed
- cargo distribution shifted by batteries (weight remains the same)
- MTOW remains same, difference taken out of fuel load
- Aspect increased by 25%
- max CL increased by 20%
- gear heightened by 30 cm
'''
# update weights:
OEW_adjust = (-W_w*0.09 - W_f*0.07 +4000)
W_w *= (1-0.09)
W_f *= (1-0.07)
W_bf = 2025 # forward battery
W_ba = 2475 # aft battery

l_bf = 10.5 # TODO: not correct number, part 1 ppl fill in
l_ba = 29.0 # TODO: ----||----

fus_group_l = np.array([l_h,l_v,l_f,l_ng,l_c, l_p, l_bf, l_ba])

fus_group_W = np.array([W_h, W_v, W_f, W_ng, W_c, W_p, W_bf, W_ba])
wing_group_W = np.array([W_w, W_mg])

CG_wing = np.dot(wing_group_W, wing_group_l)/sum(wing_group_W)
CG_fus = np.dot(fus_group_W, fus_group_l)/sum(fus_group_W)


#print("CG wing:", CG_wing)
#print("CG fuselage:", CG_fus)

CG_EXX = (np.dot(wing_group_W, (wing_group_l+lemac)) + np.dot(fus_group_W, fus_group_l))/(sum(wing_group_W)+sum(fus_group_W))

print(f"\n\nNew CG: {CG_EXX:.3f}\t new OEW: {EOW-OEW_adjust:.2f}")
print("CG table:")
names = ["Horizontal tail", "vartical tail", "fuselage", "Nose gear", "Cockpit", "propulsion", "fore battery", "aft battery"]
print("Name:\t\t weight:\t pos(from nose)\t pos(LEMAC)")
for i in range(len(fus_group_l)):
    print(f"{names[i]:15}\t {fus_group_W[i]:7.2f}\t {fus_group_l[i]:7.3f}\t {(fus_group_l[i]- lemac)/mac :6.3f}")

names2 = ["Wing", "Main gear"]
for i in range(len(wing_group_l)):
    print(f"{names2[i]:15}\t {wing_group_W[i]:7.2f}\t {wing_group_l[i]:7.3f}\t {(wing_group_l[i]- lemac)/mac :6.3f}")

