# USEFUL FUNCTIONS FOR MANAGE THE DATASET
# WARNING: ALL THE FUNCTION IN THIS FILE ARE STRICTLY RELATED ON THE DATASET FORMAT IN THE PROJECT

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def fix_private_entries(dataset):
    # It is possible that sometimes between the two different times we used the two scraper some user 
    # switch from public to private. It's not possibile to get information from private users 
    # (it's a consistency problem) so the solution adopted is to switch the attribute private 
    # to public since when we collected the datas the users were public. It's also possible 
    # to switch to private and delete the statistic informations dropping additional infos 
    # that could be interesting and useful for the classification problem.
    dataset.loc[(dataset['is_private']==True)&(dataset['min_likes'].notnull()),['is_private']] = False
    return dataset

def get_target_dataset(dataset):
    return dataset['real_account'].values

def drop_NaN_entries(dataset):
    ds=dataset.copy(deep=True)
    ds.dropna(inplace=True)
    return ds

def get_trainset(dataset):
    ds=dataset.loc[:,'profile_pic':'skw_time_between_posts']
    return ds

def drop_stats(dataset):
    ds=dataset.loc[:,'profile_pic':'highlight_reel_count']
    return ds

def fill_NaN_median(dataset):
    ds=dataset.copy(deep=True)
    ds.fillna(ds.median(),inplace=True)
    return ds

def fill_NaN_mean(dataset):
    ds=dataset.copy
    ds.fillna(ds.mean(),inplace=True)
    return ds

def get_columns_list(dataset):
    return list(dataset.columns)

def StandardScale_dataset(dataset):
    dataset=StandardScaler().fit_transform(dataset)
    return dataset

def MinMaxScale_dataset(dataset):
    dataset=MinMaxScaler().fit_transform(dataset)
    return dataset

def get_columns_list(dataset):
    return list(dataset.columns)