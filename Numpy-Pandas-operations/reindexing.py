#Gaurav patil A-33
#import necessary library
import pandas as pd
import numpy as np
 
#define index and column
column=['A','B','C','D','E']
index=[1,2,3,4,5]
 
# create a dataframe of random values of array
df1 = pd.DataFrame(np.random.rand(5,5),columns=column, index=index)

#show dataframe
print(df1)

#reindex dataframe
print('\n\nDataframe after reindexing rows: \n',
df1.reindex([5,3,4,2,1]))