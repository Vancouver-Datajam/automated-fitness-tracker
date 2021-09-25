import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def Pre_process(df):
    
    df_c = df.copy()
    df_c['y23_const'] = df_c['y23']
    df_c['z23_const'] = df_c['z23']
    df_c['y24_const'] = df_c['y24']
    df_c['z24_const'] = df_c['z24']
    
    
    #normalize the y and z corrdinate
    for i in range(0,33):
        
        df_c[f'y{i}'] = (df_c[f'y{i}']/((df_c['y23_const'] + df_c['y24_const'])/2)) - 1
        df_c[f'z{i}'] = (df_c[f'z{i}']/((df_c['z23_const'] + df_c['z24_const'])/2)) - 1
    
    #drop the unneeded columns
    df_c = df_c.drop(['y23_const', 'z23_const', 'y24_const', 'z24_const'], axis=1)
    
    for i in range(0,33):
        df_c = df_c.drop([f'x{i}'], axis=1)
        
    #fill missing values
    df_c = df_c.fillna(method="ffill")
    
    df_c = df_c[df_c['obs.no'] != 13]

    return df_c

# check and return missing values in each features in the dataframe
def missing_statistics(df):
    """
    This function check and return missing values in each features for a dataframe

    Parameters
    ----------
        df: dataframe

    Returns
    -------
        statitics (dataframe) contains missing inforamtion for each features

    """
    statitics = pd.DataFrame(df.isnull().sum()).reset_index()
    statitics.columns = ['COLUMN NAME', "MISSING VALUES"]
    statitics['TOTAL ROWS'] = df.shape[0]
    statitics['% MISSING'] = round((statitics['MISSING VALUES'] / statitics['TOTAL ROWS']) * 100, 2)
    return statitics