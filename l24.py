import numpy as np
import scipy.stats

import matplotlib.pyplot as plt

import seaborn as sns

rc={'lines.linewidth' : 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

#We load data that will use numpy with np.loadtxt (there is another type for csvs)

data_txt= np.loadtxt('data/collins_switch.csv', delimiter=',' , skiprows=2)

#slice out iptg and gfp
iptg = data_txt[:,0]
gfp = data_txt[:,1]
sem = data_txt[:,2]

# Plot ipgt vs gfp

#basic plot
plt.plot(iptg, gfp, marker='.', linestyle = 'none')
plt.xlabel('IPTG (mM)')
plt.ylabel('Normalized GFP')
plt.title('ITPG Titration - semilog X w/ ErrorBars')

#log scale plot
plt.loglog(iptg, gfp, marker='.', linestyle = 'none')
plt.xlabel('IPTG (mM)')
plt.ylabel('Normalized GFP')
plt.title('ITPG Titration - semilog X w/ ErrorBars')

#semilog scale plot (only one axis logarithmic)
plt.semilogx(iptg, gfp, marker='.', linestyle = 'none', markersize=15)
plt.xlabel('IPTG (mM)')
plt.ylabel('Normalized GFP')
plt.title('ITPG Titration - semilog X w/ ErrorBars')
plt.show()


#plot with error bars
plt.errorbar(iptg, gfp, yerr= sem, linestyle='none', marker ='.', markersize=20)
plt.xlabel('IPTG (mM)')
plt.ylabel('Normalized GFP')
plt.title('ITPG Titration - semilog X w/ ErrorBars')
plt.ylim(-0.02, 1.02)
plt.xlim(8e-4, 15)
plt.xscale('log')
plt.show()
    #The problem with this plot is that the x axis needs to be logarithmic, but there is no way to do this using plt.errorbar.
    #But, we can do this post-hoc with plt.xscale('log').
