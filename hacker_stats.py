import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')
bd_2012 = np.loadtxt('data/beak_depth_scandens_2012.csv')

bs_sample = np.random.choice(bd_1975, replace=True, size = len(bd_1975))




def ecdf(data):
    '''Compute x, y values for an empirical distribution function.'''

    x = np.sort(data)
    y = np.arange(0,1,1/len(x))

    return x, y

x_1975, y_1975 = ecdf(bd_1975)
x_2012, y_2012 = ecdf(bd_2012)
x_1975_bs, y_1975_bs = ecdf(bs_sample)

plt.plot(x_1975, y_1975, marker = '.', linestyle = 'none')
plt.plot(x_2012, y_2012, marker = '.', linestyle = 'none')

plt.plot(x_1975_bs, y_1975_bs, marker = '.', linestyle = 'none')


plt.xlabel('beak depth in mm')
plt.ylabel('ECDF')
plt.legend(('1975', 'bootstrap'), loc='lower right')
plt.show()
