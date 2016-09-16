#Darwins finches code.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

grant_complete = pd.read_csv('data/grant_complete.csv')

#data subsetting.

#year
g_1973 = grant_complete.loc[grant_complete['year']==1973]

g_1975 = grant_complete.loc[grant_complete['year']==1975]

g_1985 = grant_complete.loc[grant_complete['year']==1985]

g_1987 = grant_complete.loc[grant_complete['year']==1987]


#year>species
g_73f = g_1973.loc[g_1973['species']=='fortis']
g_73s = g_1973.loc[g_1973['species']=='scandens']

g_75f = g_1975.loc[g_1975['species']=='fortis']
g_75s = g_1975.loc[g_1975['species']=='scandens']

g_85f = g_1985.loc[g_1985['species']=='fortis']
g_85s = g_1985.loc[g_1985['species']=='scandens']

g_87f = g_1987.loc[g_1987['species']=='fortis']
g_87s = g_1987.loc[g_1987['species']=='scandens']

#year>species>trait

g_73f_bd = g_73f['beak depth (mm)']
g_75f_bd = g_75f['beak depth (mm)']
g_85f_bd = g_85f['beak depth (mm)']
g_87f_bd = g_87f['beak depth (mm)']

g_73f_bd = g_73f['beak length (mm)']
g_75f_bd = g_75f['beak length (mm)']
g_85f_bd = g_85f['beak length (mm)']
g_87f_bd = g_87f['beak length (mm)']
