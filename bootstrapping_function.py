def draw_bs_reps(data, func, n_reps=100000):
    '''Takes a set of data, and computes the bootstrapped confidence interval for test statistics including the mean, std..[insert other test stats you might want to put in at some stage...]. Bootstraps with 100,000 replicates as default.'''

    #Number of replicas
    n_reps = n_reps

    #Bootstrap mean module
    if func == 'mean'
    #Initialize the array of replicates. This is an empty array where we will store the values of bootstrapped means.
        bs_mean = np.empty(n_reps)
        #Here we are generating the bootstrap
        for i in range(n_reps):
            bs_sample = np.random.choice(data, replace=True, size=len(data))
            bs_mean[i] = np.mean(bs_sample)

            #Now you need to add this to the array...


            print(conf_int_data = np.percentile(data, [2.5, 97.5])


    #Boostrap std module
    if func == 'std'
        bs_std = np.empty(n_reps)
        for i in range(n_reps):
            bs_sample = np.random.choice(data, replace=True, size=len(data))
            bs_std[i] = np.std(bs_sample)

            return bs_std

    if func == 'std'
                bs_std[i] = np.std(bs_sample)
