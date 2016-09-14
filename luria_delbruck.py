import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

#specifity parameters
#number of generations
n_gen = 16

#Change of having beneficial mutation
r = 1e-5

# Total number of cells
n_cells = 2**(n_gen-1)

ai_samples = np.random.binomial(n_cells, r, size=100000)

#Reprot mean and std
print('AI mean:', np.mean(ai_samples))
print('AI std:', np.std(ai_samples))
print('AI Fano:', np.var(ai_samples)/np.mean(ai_samples))

#Function to draw out of a random mutation hypothesis

def draw_random_mutation(n_gen, r):
    '''Draw sample under random mutation hypothesis.'''
    #Initialise number of mutations
    n_mut=0

    for g in range(n_gen):
        n_mut = 2*n_mut + np.random.binomial(2**g - 2*n_mut, r)

    return n_mut

def sample_random_mutation(n_gen, r, size =1):
    #intialize samples
    samples = np.empty(size)

    #Draw the samepls
    for i in range(size):
        samples[i] = draw_random_mutation(n_gen, r)

    return samples
