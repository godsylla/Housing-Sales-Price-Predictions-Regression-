import numpy as np
import pandas as pd


def convert_qual_to_num_5 (df_column_name):
    '''
    for data frame columns that have qualitative ratings, convert the qualitative ratings to numeric ratings.
    takes a data frame column as an argument in the form of df['column_name'].
    '''
    df_new_column = []
    for i in range(len(df_column_name)):
        if df_column_name.iloc[i] == 'Ex':
            df_new_column.append(5)
        elif df_column_name.iloc[i] == 'Gd':
            df_new_column.append(4)
        elif df_column_name.iloc[i] == 'TA':
            df_new_column.append(3)
        elif df_column_name.iloc[i] == 'Fa':
            df_new_column.append(2)
        elif df_column_name.iloc[i] == 'Po':
            df_new_column.append(1)
        elif df_column_name.iloc[i] == 'NA':
            df_new_column.append(0)
            
    return df_new_column


def convert_bsmt_qual_to_num_4 (df_column_name):
    '''
    for data frame columns that have qualitative ratings, convert the qualitative ratings to numeric ratings.
    takes a data frame column as an argument in the form of df['column_name'].
    '''
    df_new_column = []
    for i in range(len(df_column_name)):
        if df_column_name.iloc[i] == 'Gd':
            df_new_column.append(4)
        elif df_column_name.iloc[i] == 'Av':
            df_new_column.append(3)
        elif df_column_name.iloc[i] == 'Mn':
            df_new_column.append(2)
        elif df_column_name.iloc[i] == 'No':
            df_new_column.append(1)
        elif df_column_name.iloc[i] == 'NA':
            df_new_column.append(0)
            
    return df_new_column


def convert_bsmt_qual_to_num_6 (df_column_name):
    '''
    for data frame columns that have qualitative ratings, convert the qualitative ratings to numeric ratings.
    takes a data frame column as an argument in the form of df['column_name'].
    '''
    df_new_column = []
    for i in range(len(df_column_name)):
        if df_column_name.iloc[i] == 'GLQ':
            df_new_column.append(6)
        elif df_column_name.iloc[i] == 'ALQ':
            df_new_column.append(5)
        elif df_column_name.iloc[i] == 'BLQ':
            df_new_column.append(4)
        elif df_column_name.iloc[i] == 'Rec':
            df_new_column.append(3)
        elif df_column_name.iloc[i] == 'LwQ':
            df_new_column.append(2)
        elif df_column_name.iloc[i] == 'Unf':
            df_new_column.append(1)
        elif df_column_name.iloc[i] == 'NA':
            df_new_column.append(0)    
    return df_new_column


def convert_exter_qual_to_num_4 (df_column_name):
    '''
    for data frame columns that have qualitative ratings, convert the qualitative ratings to numeric ratings.
    takes a data frame column as an argument in the form of df['column_name'].
    '''
    df_new_column = []
    for i in range(len(df_column_name)):
        if df_column_name.iloc[i] == 'Ex':
            df_new_column.append(4)
        elif df_column_name.iloc[i] == 'Gd':
            df_new_column.append(3)
        elif df_column_name.iloc[i] == 'TA':
            df_new_column.append(2)
        elif df_column_name.iloc[i] == 'Fa':
            df_new_column.append(1)
        elif df_column_name.iloc[i] == 'Po':
            df_new_column.append(0)
            
    return df_new_column


def calc_percent_nonnull (df, column_name):
    '''accepts column_name as an argument, which is a string'''
    percent = len(df[~df[column_name].isnull()])/len(df)
    return round(percent*100, 2)



