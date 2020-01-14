"""
Lambdata - a collection of data scinece helper functions

"""

import pandas as pd
import numpy as np

# sample code
df = pd.DataFrame(np.ones(10))
ZEROS = pd.DataFrame(np.zeros(50))
NAN = pd.DataFrame(np.nan, index=[0,1,2,3], columns=['A'])

def list_func(x):
  ONES["Added values"] = ONES.add(x)

def list_to_df(x,y):
    '''
    takes in list as var one and a dataframe as var two. converts list
    to series and adds series to dataframe

    '''

    y['added value'] = pd.Series( (v[0] for v in x) )

def null_check(x):
    '''
    takes in a dataframe as a variable. checks for null values

    '''

    test =  x.isnull()
    count = 0
    for i in test:
      print('row ' + str(count) + ' has NaN value? ' + str(i))
      count = count + 1
