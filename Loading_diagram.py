from CG_calculations import CG, lemac, fore_occupied_len, aft_occupied_len, CG_EXX, W_bf, W_ba, l_bf, l_ba 
import matplotlib.pyplot as plt
import numpy as np



def load_diagram(part_2:bool, plot:bool):
    rows = 25
    W_pay = 11966 #kg
    W_empty = 23133

    if part_2:
        W_empty = 20109.91
        cg = CG_EXX 
    else: cg = CG
        

    mac = 3.48
    x_empty = (cg - lemac) /mac
    n_pas = 100
    if part_2:
        n_pas -= 3 * 4 # 4 pax per row
        rows -= 3
    W_pas = 84 #kg

    #Cargo weights and lengths
    W_aft = 1807
    W_forward = 962
    W_both = W_aft + W_forward
    l_forward = 10.5
    l_aft = 29.0
    W_cargo = n_pas*W_pas + W_aft + W_forward

    if part_2:
        # l fore and aft should be changed after losing volume
        #from cg:
        l_aft -= 0.5*aft_occupied_len
        l_forward += 0.5*fore_occupied_len
        # don't loose mass though

    l_tank = 18.8
    W_fuel = 5842

    if part_2:
        # fuel decreased to keep MTOW the same
        # since MTOW = OEW + fuel + pax + cargo, 
        # net change is delta OEW + delta pax + batteries
        d_pax = - (3*4)*W_pas
        d_OEW = -(23133 - 20109.91) #from other file
        d_fuel = -(d_pax + d_OEW) # make up difference
        W_fuel += d_fuel
        print(f"to keep MTOW. fuel load is adjusted from {W_fuel-d_fuel:.1f} Kg to {W_fuel:.1f} Kg (Net change: {d_fuel:.1f} Kg)")

    #Loading diagram for cargo
    x_aft = ((((W_empty * cg) + (W_aft * l_aft)) / (W_empty + W_aft)) - lemac) / mac
    x_forward = ((((W_empty * cg) + (W_forward * l_forward)) / (W_empty + W_forward)) - lemac)/mac
    x_both = ((((W_empty * cg) + (W_forward * l_forward) + (W_aft * l_aft)) / (W_empty + W_forward + W_aft)) - lemac)/mac
    #print(x_aft, x_forward)



        

    #Passenger weights and lengths
    l_front = 6.84 - lemac # m (pax front seat)
    x_window = [x_both,] # array cg pos from window boarding
    w_window = [W_empty+W_both,] # array cg weight --||--
    x_window_two = [x_both,] # same but boarding backwards
    w_window_two = [W_empty+W_both,]
    M_n = (W_empty+W_both)*x_both # cg moment (M_n / w = x_cg)
    W_n = (W_empty+W_both)
    # forward window
    for n in range(rows): # from front
        l_n = l_front + 0.8*n # 0.8 space per row
        W_n += W_pas*2 # add weight
        M_n += 2*W_pas*l_n # add moment
        x_n = (M_n/W_n) # new cg pos
        x_window.append(x_n)
        w_window.append(W_n)


    M_n = (W_empty+W_both)*x_both # reset moment
    W_n = (W_empty+W_both)
    l_back = l_n # aftmost seat
    # assert abs(l_back - (l_front + 0.8*(rows-1))) < 1e-8
    for n in range(rows): # from back
        l_n = l_back - 0.8*n # 0.8 space per row
        W_n += W_pas*2
        M_n += 2*W_pas*l_n
        x_n = (M_n/W_n)
        x_window_two.append(x_n)
        w_window_two.append(W_n)

    x_aisle = [x_window_two[-1],] # start from end of prev
    w_aisle = [w_window_two[-1],]
    x_aisle_two = [x_window_two[-1],]
    w_aisle_two = [w_window_two[-1],]
    w_n_init = W_n # weight/moment after window boarding
    M_n_init = M_n
    for n in range(rows):
        l_n = l_front + 0.8*n # 0.8 space per row
        W_n += W_pas*2
        M_n += 2*W_pas*l_n
        x_n = (M_n/W_n)
        x_aisle.append(x_n)
        w_aisle.append(W_n)

    W_n = w_n_init
    M_n = M_n_init
    for n in range(rows):
        l_n = l_back - 0.8*n # 0.8 space per row
        W_n += W_pas*2
        M_n += 2*W_pas*l_n
        x_n = (M_n/W_n)
        x_aisle_two.append(x_n)
        w_aisle_two.append(W_n)

    W_last = w_aisle_two[-1]
    x_last = x_aisle_two[-1]
    #print(W_last, x_last)

    x_fuel = (((W_fuel * (l_tank - lemac)) + (W_last * x_last)) / (W_fuel + W_last)) /mac
    W_final = W_last + W_fuel

    #Finding most aft and most forward cg
    min_cg = min(*x_aisle, x_forward, x_fuel)
    max_cg = max(*x_window_two, x_aft, x_fuel)
    print("min", min_cg, "max", max_cg)

    if part_2:
        # find the OEW sans batteries:
        M_cg = W_empty * x_empty
        l_bamac = (l_ba -lemac)/ mac
        l_bfmac = (l_bf -lemac)/ mac
        M_batt = l_bamac*W_ba + l_bfmac*W_bf
        M_wo_batt = M_cg-M_batt
        W_wo_batt =  W_empty - W_ba - W_bf
        x_wo_batt = (M_wo_batt/W_wo_batt)
    
    if plot:
        if part_2:
            plt.plot([x_wo_batt,x_empty],[W_wo_batt,W_empty], '--o', color="red", label='Battery Packs')
            print(f"OEW sans battery location: {x_wo_batt:.2f}")
            print(f"Battery locations: fore:{l_bfmac:.2f}\taft: {l_bamac:.2f}")

        plt.plot([x_forward, x_empty, x_aft, x_both, x_forward], [W_forward+W_empty, W_empty, W_aft+W_empty, W_both+W_empty, W_forward+W_empty], '-o', color='deeppink', label = 'Cargo')
        plt.plot(x_window, w_window, '-o', color = 'darkviolet', label = 'Window seats')
        plt.plot(x_window_two, w_window_two, '-o', color = 'darkviolet')
        plt.plot(x_aisle, w_aisle, '-o', color = 'violet', label ='Aisle seats')
        plt.plot(x_aisle_two, w_aisle_two,'-o', color = 'violet')
        plt.plot([x_last, x_fuel], [W_last, W_final], '-o', color='cyan', label = 'Fuel')
        plt.vlines(min_cg, W_empty, W_final, color = 'mediumvioletred', label = 'cg range')
        plt.vlines(min_cg-0.02, W_empty, W_final, color = 'rebeccapurple', label="cg range with safety margin")
        plt.vlines(max_cg, W_empty, W_final, color = 'mediumvioletred')
        plt.vlines(max_cg+0.02, W_empty, W_final, color = 'rebeccapurple')

        # print relevant values:
        print(f"OEW location: {x_empty:.2f}")
        print(f"Aftmost location: {max_cg:.2f}, Foremost location: {min_cg:.2f}")
        print(f"fully loaded: {x_fuel:.2f}")
        print(f"cg of front+rear cargo (only): {(l_forward-lemac)/mac:.2f}\t{(l_aft-lemac)/mac:.2f}")
        print(f"cg of fueltanks (only): {(l_tank-lemac)/mac:.2f}")
        print("*only as in not the whole place cg with those included, it's just the component cg")

        
        # plt.title("Loading diagram") # put title in latex
        plt.ylabel("Weight [kg]")
        plt.xlabel("Cg [mac]")
        plt.legend()
        plt.grid()
        plt.show()
    else: # combine all into the master potato
        x_all = [x_empty, x_forward, x_both]
        x_all.extend(x_window)
        x_all.extend(x_aisle)
        x_all.append(x_fuel)
        x_all.extend(x_aisle_two[::-1])
        x_all.extend(x_window_two[::-1])
        x_all.extend([x_aft,x_empty])

        W_all = [W_empty, W_forward+W_empty, W_both+W_empty]
        W_all.extend(w_window)
        W_all.extend(w_aisle)
        W_all.append(W_final)
        W_all.extend(w_aisle_two[::-1])
        W_all.extend(w_window_two[::-1])
        W_all.extend([W_aft+W_empty,W_empty])
        return x_all, W_all



if __name__ == "__main__":

    # part 1:
    load_diagram(False,True)
    
    # part 2:
    x_pt1, w_pt1 = load_diagram(False,False) #type:ignore
    plt.plot(x_pt1,w_pt1, '--',color="gray", label="Old loading diagram", ms=3, lw=0.7)
    load_diagram(True,True)

    


