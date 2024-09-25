import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
# calc bmi
df['height_meters'] = df['height'] / 100
print("\n---------- df['height_meters]:")
print(df['height_meters'])
df['bmi'] = df['weight'] / (df['height_meters'] ** 2)
print("\n---------- df['bmi]:")
print(df['bmi'])
# create overweight column
df['overweight'] = (df['bmi'] > 25).astype(int)
print("\n---------- df['overweight]:")
print(df['overweight'])

# 3
# Normalize data by making 0 always good and 1 always bad. If the value of cholesterol or gluc is 1, set the value to 0. If the value is more than 1, set the value to 1.
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
print("\n---------- df['cholesterol]:")
print(df['cholesterol'])
df['gluc'] = (df['gluc'] > 1).astype(int)
print("\n---------- df['gluc]:")
print(df['gluc'])


# 4
def draw_cat_plot():
    """Draws a categorical plot using seaborn's catplot."""

    # 5
    # Create DF for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    columns_to_melt = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    print("\n---------- columns_to_melt:")
    print(columns_to_melt)
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=columns_to_melt)
    print("\n---------- df_cat:")
    print(df_cat)


    # 6
    # Group and reformat the data to split it by 'cardio'.
    # Show counts of each feature.
    # Need to rename one of the cols for catplot to work proprly.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'])['value'].count().reset_index(name='total')
    print("\n---------- df_cat:")
    print(df_cat)


    # 7



    # 8
    fig = None


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
