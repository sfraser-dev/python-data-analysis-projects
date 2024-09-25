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
    # 5
    df_cat = None


    # 6
    df_cat = None
    

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
