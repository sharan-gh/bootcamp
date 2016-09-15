def draw_bs_reps(data, func, n_reps=100000):
    '''Takes a set of data, and computes the bootstrapped confidence interval for test statistics according to numpy features and syntax. Bootstraps with 100,000 replicates as default (kwarg).'''
    #Number of replicas
    n_reps = n_reps
    #Initialize the array of replicates. This is an empty array where we will store the values of bootstrapped test statistics. We will then compute the confidence interval based on the distribution of means in this array.
        bs_func = np.empty(n_reps)
        #Here we are generating the bootstrap
        for i in range(n_reps):
            bs_sample = np.random.choice(data, replace=True, size=len(data))
            #Now you need to add this to the array...
            bs_func = np.func(bs_sample)
            #and compute the confidence interval
            conf_int_func = np.percentile(bs_func, [2.5, 97.5])
            return

            print('conf_interval for')
            print(func)
            print(conf_int_func)
