"""
Lambdata - a collection of data scinece helper functions

"""

import pandas as pd
import numpy as np


def list_to_df(list, df):
    '''
    takes in list as var one and a dataframe as var two. converts list
    to series and adds series to dataframe
    '''

    return pd.Series((v[0] for v in list))


def null_check(df):
    '''
    takes in a dataframe. checks for null values.
    reports them as true
    '''

    df_null = df.isnull()
    print('The Following Locations That Report True Are Null Values')
    print(test2)


def plot_confustion_matrix(true, predicted):
    """
    takes in the predictions and the actual and plots into confusiton matrix
    """
    import seaborn as sns
    from sklearn.metrics import confusion_matrix
    from sklearn.utils.multiclass import unique_labels

    labels = unique_labels(true)
    columns = [f'Predicted {label}' for label in labels]
    index = [f'Actual {label}' for label in unique_labels]
    table = pd.DataFrame(confustion_matrix(true, predicted),
                         columns=columns, index=index)
    return sns.heatmap(table, annot=True, fmt='d', cmap='viridis')


def train_split_test(data, target):
    """
    takes in data and splits it into trian, val, and test
    also takes in target
    """
    from sklearn.model_selection import train_test_split

    # splitting test and train
    train0, test = train_test_split(data, train_size=0.80, test_size=0.20,
                                    stratify=train[target], random_state=42)

    # splitting train and val
    train, val = train_test_split(train0, train_size=0.80, test_size=0.20,
                                  stratify=train[target], random_state=42)


def random_func(df):
    '''
    reusable func made for generate_more_data func
    '''
    import random
    random_list = []
    for i in range(0, len(df)):
        random_list.append([random.randrange(1, 101, 1)])
    return random_list


def generate_more_data(df, random_amount=3):
    '''
    takes in a df and generates more data onto it
    '''
    for i in range(0, random_amount):

        df['r'+str(i)] = list_to_df(random_func(df), df)


def simple_func(x):
    '''
    created for testing purposes, just return absolute value
    '''
    return abs(x)
