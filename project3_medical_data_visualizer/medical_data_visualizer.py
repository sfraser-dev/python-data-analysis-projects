import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
# Calc BMI and create overweight column
# Create new column 'height_meters' by dividing 'height' by 100
df['height_meters'] = df['height'] / 100
print("\n---------- df['height_meters]:")
print(df['height_meters'])
# Create new column 'bmi' by dividing 'weight' by 'height_meters' squared
df['bmi'] = df['weight'] / (df['height_meters'] ** 2)
print("\n---------- df['bmi]:")
print(df['bmi'])
# Create new column 'overweight' by setting 'bmi' > 25 to 1 and 0 otherwise
df['overweight'] = (df['bmi'] > 25).astype(int)
print("\n---------- df['overweight]:")
print(df['overweight'])

# 3
# Normalize data by making 0 always good and 1 always bad. If the value of cholesterol is 1, set the value to 0. If the value is more than 1, set the value to 1.
# Access 'cholesterol' column
cholesterol_column = df['cholesterol']
print("\n---------- cholesterol_column:")
print(cholesterol_column)
# Create boolean mask Series for cholesterol levels >1
cholesterol_mask = cholesterol_column > 1
print("\n---------- cholesterol_mask:")
print(cholesterol_mask)
# Convert boolean mask Series to integers (1 for True, 0 for False)
# Note: .astype(int) converts True to 1 and False to 0
cholesterol_int = cholesterol_mask.astype(int)
print("\n---------- cholesterol_int:")
print(cholesterol_int)
# Assign resulting Series back to the 'cholesterol' column in DF
df['cholesterol'] = cholesterol_int
# shorthand: df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
print("\n---------- df['cholesterol]:")
print(df['cholesterol'])

# Normalize data by making 0 always good and 1 always bad. If the value of gluc is 1, set the value to 0. If the value is more than 1, set the value to 1.
# Same as for cholesterol, using shorthand
df['gluc'] = (df['gluc'] > 1).astype(int)
print("\n---------- df['gluc]:")
print(df['gluc'])


# 4
def draw_cat_plot():
    """Draw a categorical plot using seaborn's catplot."""

    # 5
    # Create a DataFrame for the cat plot using pd.melt with values from cholesterol, gluc, smoke, alco, active, and overweight in the df_cat variable.
    # Note: .melt() is used to transform a DF from wide to long format. In a wide format, each variable is in a separate col, while in a long format, all variables are stacked into a single col with another col indicating which variable each value corresponds to.
    columns_to_melt = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    print("\n---------- columns_to_melt:")
    print(columns_to_melt)
    # Melting the DF
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=columns_to_melt)
    print("\n---------- df_cat (melt):")
    print(df_cat)


    # 6
    # Group and reformat the data in df_cat to split it by cardio. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    # Group the DF by 'cardio', 'variable', and 'value' using .groupby()
    # Note: .groupby() identifies all unique combinations of the values in the specified columns. A powerful abstraction for manipulating and summarizing data.
    grouped_df = df_cat.groupby(['cardio', 'variable', 'value'])  # produces a SeriesGroupBy object, cannot print
    # Count the occurrences of each group in the 'value' column
    counted_values = grouped_df['value'].count()
    # Reset index to turn the grouped data back into a DF
    reset_df = counted_values.reset_index(name='total')
    # Assign resultant DF to df_cat
    df_cat = reset_df
    print("\n---------- counted_values:")
    print(counted_values)
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
