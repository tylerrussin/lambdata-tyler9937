"""
Lambdata - a collection of data scinece helper functions

"""

import pandas as pd
import numpy as np


class Basic_functions:
    '''
    Class has a couple of functions that preform various tasks
    '''

    def __init__(self, list_var=[['a'], ['b'], ['c']], df=pd.DataFrame(np.ones(10))):
        '''
        initaiating the self variable and defining default values for
        a list_var and df
        '''
        self.list_var = list_var
        self.df = df

    def list_to_df(list, df):
        '''
        takes in list as var one and a dataframe as var two. converts list
        to series and adds series to dataframe
        '''

        df['added value'] = pd.Series((v[0] for v in list))

    def null_check(df):
        '''
        takes in a dataframe. checks for null values.
        note: currently only works for taking in pandas series. a bug
        occures when dealing with dataframes
        '''

        test = df.isnull()
        count = 0
        for i in test:
            print('row ' + str(count) + ' has NaN value? ' + str(i))
            count = count + 1
