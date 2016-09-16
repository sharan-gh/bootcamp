import numpy as np
import pandas as pd
import seaborn as sbn
import matplotlib.plotpy as plt

def bs_reps(data, func, n_reps=100000):
    '''Computes the bootstrapped confidence interval for test statistics according to numpy features and syntax. 100,000 replicates as default.'''
    #Initialize the array of replicates. We will compute the confidence interval based on the distribution of means in this array.
    bs_func = np.empty(n_reps)
    #Here we are generating the bootstrap
    for i in range(n_reps):
        bs_sample = np.random.choice(data, replace=True, size=len(data))
        #Now you need to add this to the array...
        bs_func[i] = func(bs_sample)
        #and compute the confidence interval
        conf_int_func = np.percentile(bs_func, [2.5, 97.5])
        return
        print(conf_int_func)
