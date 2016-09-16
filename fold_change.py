import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

#load all data
wt = np.loadtxt('data/wt_lac.csv', comments='#', delimiter=',', skiprows=3)

q18m = np.loadtxt('data/q18m_lac.csv', comments='#', delimiter=',', skiprows=3)

q18a = np.loadtxt('data/q18m_lac.csv', comments='#', delimiter=',', skiprows=3)


#extract rows for ecdf
wt_iptg = wt[:,1]
q18m_iptg = q18m[:,1]
q18a_iptg = q18a[:,1]


#ecdf
def ecdf(data):
    '''Compute x, y values for an empirical distribution function.'''
    x = np.sort(data)
    y = np.arange(0,1,1/len(data))
    return x, y

#define axes for ecdf
wt_x, wt_y = ecdf(wt_iptg)
q18m_x, q18m_y = ecdf(q18m_iptg)
q1a_x, q18a_y = ecdf(q18a_iptg)

#plot ecdfs

plt.semilogx(wt_x, wt_y, marker = '.', markersize = 13, linestyle = 'none')

plt.semilogx(q18m, q18m_y , marker = '.', markersize = 13, linestyle = 'none')

plt.semilogx(q18a, q18a_y , marker = '.', markersize = 13,  linestyle = 'none')

#fold change computation

def fold_change_for loop(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    clist = c.tolist()

    for c in clist:
        fc=[1+(((RK)*(1+c/Kda)**2))/((1+c/KdA)**2)+Kswitch*(1+c/KdI)**2]**-1
        return fc
        #shouldn't need a for loop!

def fold_change_array(c, RK, KdA=0.017, KdI=0.002, Kswitch=5.8):
    '''Computes theoretical fold change given IPTG concentration. Variable c should be entered as a numpy array of values.'''
    
    fc=[1+(((RK)*(1+c/Kda)**2))/((1+c/KdA)**2)+Kswitch*(1+c/KdI)**2]**-1
    return fc
