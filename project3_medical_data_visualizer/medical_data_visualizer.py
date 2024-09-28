import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
# Import data
df = pd.read_csv('medical_examination.csv')

# 2
# Calc BMI and create overweight column
# Create new temporary column 'height_meters' by dividing 'height' by 100
df['height_meters'] = df['height'] / 100
print("\n---------- df['height_meters]:")
print(df['height_meters'])
# Create new temporary column 'bmi' by dividing 'weight' by 'height_meters' squared
df['bmi'] = df['weight'] / (df['height_meters'] ** 2)
print("\n---------- df['bmi]:")
print(df['bmi'])
# Create new column 'overweight' by setting 'bmi' > 25 to 1 and 0 otherwise
df['overweight'] = (df['bmi'] > 25).astype(int)
print("\n---------- df['overweight]:")
print(df['overweight'])
# Drop the temporary columns used for the overweight calculation
df.drop(['height_meters', 'bmi'], axis=1, inplace=True)

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
print("\n---------- df['cholesterol]:")
print(df['cholesterol'])

# Normalize data by making 0 always good and 1 always bad. If the value of gluc is 1, set the value to 0. If the value is more than 1, set the value to 1.
# Same as for cholesterol, using shorthand
df['gluc'] = (df['gluc'] > 1).astype(int)
print("\n---------- df['gluc]:")
print(df['gluc'])

# 4
# Draw Categorical Plot
def draw_cat_plot():
    """
    Draws a categorical plot showing the relationship between various health factors and cardiovascular disease.

    Args:
      df (pandas.DataFrame): The DataFrame containing the medical data.

    Returns:
      matplotlib.figure.Figure: The matplotlib Figure object containing the catplot.
    """

    #  --------------------------------- Prepare the Data ---------------------------------

    # 5
    # Create new DF 'df_cat' using 'pd.melt'.
    # This will transform the data from wide format to long format, making it suitable for a catplot.
    # Select only the columns 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight' as categories.
    df_cat = pd.melt(df, 
                     id_vars=['cardio'], 
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Reset the index of the DataFrame.
    # This ensures that the 'index' column reflects the row number, which will be used for counting later.
    df_cat = df_cat.reset_index()

    # --------------------------------- Group and Aggregate ---------------------------------

    # 6
    # 7
    # Group the data by 'variable', 'cardio', and 'value' columns.
    # This groups the data by category, cardiovascular disease status, and the value of the category (e.g., 1 for high cholesterol).
    # Then, aggregate the data by counting the occurrences of each combination using 'agg('count')`.
    # This counts how many people fall into each group (e.g., how many people with cardiovascular disease have high cholesterol).
    # Rename the 'index' column to 'total' for clarity. This column now represents the count for each group.
    df_cat = df_cat.groupby(['variable', 'cardio', 'value']) \
                   .agg('count') \
                   .rename({'index': 'total'}, axis=1)
    # Reset the index to make 'variable', 'cardio', 'value', and 'total' regular columns.
    df_cat = df_cat.reset_index()

    # --------------------------------- Create the Catplot ---------------------------------

    # 8
    # Create catplot using Seaborn's `catplot` function.
    # 'x='variable'`: Categories ('cholesterol', 'gluc', etc.) are plotted on the x-axis.
    # 'y='total': Counts are plotted on the y-axis.
    # 'hue='cardio': Data is colored differently based on cardiovascular disease status.
    # 'col='value': Creates separate plots for each value of the categories (e.g., 0 and 1 for cholesterol).
    # 'kind='bar':  Specifies that the plot should be a bar chart.
    # 'height=6': Sets the height of each subplot.
    # 'aspect=1.5': Sets the aspect ratio of each subplot.
    fig = sns.catplot(x='variable', 
                     y='total', 
                     hue='cardio', 
                     col='value', 
                     data=df_cat, 
                     kind='bar', 
                     height=5, 
                     aspect=1.6)

    # --------------------------------- Save and Return ---------------------------------

    # 9
    # Save figure to 'catplot.png'.
    fig.savefig('catplot.png')
    # Extract matplotlib Figure object from FacetGrid object (`fig`).
    fig = fig.figure
    # Return the Figure object.
    return fig


# 10
def draw_heat_map():
    """
    Creates a heatmap visualising the correlation between different medical parameters after cleaning the data.

    Args:
        df (pandas.DataFrame): The DataFrame containing the medical data.

    Returns:
        matplotlib.figure.Figure: The matplotlib Figure object containing the heatmap.
    """

    # --------------------------------- Clean the Data ---------------------------------

    # 11
    # Clean the data by filtering out rows based on conditions given in task
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &  # Ensure 'ap_lo' is less than or equal to 'ap_hi'
        (df['height'] >= df['height'].quantile(0.025)) &  # Remove bottom 2.5% of 'height' values
        (df['height'] <= df['height'].quantile(0.975)) &  # Remove top 2.5% of 'height' values
        (df['weight'] >= df['weight'].quantile(0.025)) &  # Remove bottom 2.5% of 'weight' values
        (df['weight'] <= df['weight'].quantile(0.975))    # Remove top 2.5% of 'weight' values
    ]


    # --------------------------------- Correlation Matrix ---------------------------------

    # 12
    # Calculate the correlation matrix between all pairs of columns in the cleaned data
    corr = df_heat.corr()

    # --------------------------------- Create Mask ---------------------------------

    # 13
    # Generate mask for the upper triangle of the correlation matrix to avoid redundant information
    # Note: 'triu' stands for 'triangle upper'
    mask = np.triu(corr)

    # --------------------------------- Create Heatmap ---------------------------------

    # 14
    # Create a matplotlib figure and axes for plotting
    fig, ax = plt.subplots()
    
    # 15
    # Draw the heatmap using seaborn's heatmap function
    ax = sns.heatmap(
        corr,           # Data to visualize (correlation matrix)
        mask=mask,      # Hide the upper triangle
        annot=True,     # Show correlation values on the heatmap
        fmt='0.1f',     # Format the annotations to one decimal place
        square=True     # Make the heatmap cells square for better visual representation
    )

    # --------------------------------- Save and Return ---------------------------------

    # 16
    fig.savefig('heatmap.png')
    return fig