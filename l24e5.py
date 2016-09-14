import numpy as np
import scipy.stats
import bootcamp_utils

import matplotlib.pyplot as plt

import seaborn as sns

rc={'lines.linewidth' : 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

#Load Data
xa_high = np.loadtxt('data/xa_high_food.csv', comments = '#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments = '#')

#Here, we are calling the ecdf module for each dataset. Remember that the module gives you a tuple with two elements, and the way we
#are assigning variables here is for the first element followed by the second element.
x_high, y_high = bootcamp_utils.ecdf(xa_high)
x_low, y_low =bootcamp_utils.ecdf(xa_low)

#Next we plot both the high and low food data as ecdfs on the same plot (for comparison). 
plt.plot(x_high, y_high, marker='.', linestyle='none', markersize=20)
plt.plot(x_low, y_low, marker='.', linestyle='none', markersize=20, alpha=0.5)
plt.xlabel('Cross-sectional area (um)')
plt.ylabel('eCDF')
plt.legend(('high food', 'low food'), loc = 'lower right')
plt.show()

x = np.linspace(1600, 2500, 400)

cdf_high = scipy.stats.norm.cdf(x, loc=np.mean(xa_high),scale=np.std(xa_high))

cdf_low = scipy.stats.norm.cdf(x, loc=np.mean(xa_low), scale=np.std(xa_low))
plt.plot(x, cdf_high, color='gray')
plt.plot(x, cdf_low, color='gray')
lt.xlabel('Cross-sectional area (um)')
plt.ylabel('eCDF')
plt.legend(('high food', 'low food'), loc = 'lower right')
plt.show()
