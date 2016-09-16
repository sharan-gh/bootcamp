import pandas as pd
import numpy as np
#import datasets
grant_1973 = pd.read_csv('data/grant_1973.csv', comment='#')
grant_1975 = pd.read_csv('data/grant_1975.csv', comment='#')
grant_1987 = pd.read_csv('data/grant_1987.csv', comment='#')
grant_1991 = pd.read_csv('data/grant_1991.csv', comment='#')

#fix year column name
grant_1973 = grant_1973.rename(columns={"yearband":"year"})

grant_1973.ix[:,'year']=1973

#adding a column to the file with year
grant_1973['year']=np.ones(len(grant_1973), dtype=int)*1973
grant_1975['year']=np.ones(len(grant_1975), dtype=int)*1975
grant_1987['year']=np.ones(len(grant_1987), dtype=int)*1987
grant_1991['year']=np.ones(len(grant_1991), dtype=int)*1991
    #what we want is a column of ones that is len(df). We then multiply each element (each one) by the number we want. Cool!

grant_1973 = grant_1973.rename(columns={"beak length":"beak length (mm)"})
grant_1973 = grant_1973.rename(columns={"beak depth":"beak depth (mm)"})

#Columns renamed
grant_1975.columns = ['band', 'species', 'beak length (mm)', 'beak depth (mm)', 'year']
grant_1987.columns = ['band', 'species', 'beak length (mm)', 'beak depth (mm)', 'year']
grant_1991.columns = ['band', 'species', 'beak length (mm)', 'beak depth (mm)', 'year']
