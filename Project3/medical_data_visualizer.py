import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# ______________________________________________________________________________

# Import data
df = pd.read_csv('Project3/medical_examination.csv')
# Add 'overweight' column
body_mass_index = df['weight'] / (df['height']/100) ** 2
df['overweight'] = np.where(body_mass_index > 25, 1, 0)
# Normalize data by making 0 always good and 1 always bad. If the value of
# 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1,
# make the value 1.
for val in ['cholesterol', 'gluc']:
    df[val] = np.where(df[val] > 1, 1, 0)

# ______________________________________________________________________________

# Draw Categorical Plot


def draw_cat_plot(df):
    # Create DataFrame for cat plot using `pd.melt` using just the values from
    # 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df.melt(
        id_vars='cardio', value_vars='active alco cholesterol gluc overweight smoke'.split(' '))
    cardio1 = df_cat[df_cat['cardio'] == 1]
    cardio0 = df_cat[df_cat['cardio'] == 0]
    dfs = [cardio0, cardio1]
    # Grabbing the values for the x axis.
    x_labels = df_cat.variable.unique()
    x_is = np.arange(len(x_labels))
    bar_width = 0.5
    # Create a (1,2) figure with shared y-axis.
    fig, axes = plt.subplots(1, 2, sharey=True)
    # Looping over both dataframes. Associate each with an axis.
    for i_df, ax in enumerate(axes):
        df = dfs[i_df]
        # Looping over all plotted variables.
        for j, var in enumerate(x_labels):
            bar_col = {0: 'tab:blue', 1: 'tab:orange'}
            # Constructing a bar for both variable values.
            for var_val in [0, 1]:
                # Slice the dataframe for the specific value of that variable.
                y = len(df[(df['variable'] == var) & (df['value'] == var_val)])
                # Placing both half width bars centered around the xtick.
                ax.bar(j + (var_val-0.5)*bar_width/2,
                       y,
                       width=bar_width/2,
                       color=bar_col[var_val],
                       align='center',
                       label=str(var_val) if j == 0 and i_df == 0 else '')
        # Formatting the axes with a label. 
        # Fixing x-axis ticks and associate labels.
        # Removing top and right spines.
        ax.set_ylabel('total' if i_df==0 else '')
        ax.set_xlabel('variable')
        ax.set_xticks(x_is)
        ax.set_xticklabels(x_labels, rotation=45, ha='right')
        for spine in ['top', 'right']:
            ax.spines[spine].set_visible(False)
    # Placing a legend.
    fig.legend(title='value', loc='center right', framealpha=0)
    # Group and reformat the data to split it by 'cardio'. Show the counts of
    # each feature. You will have to rename one of the columns for the catplot
    # to work correctly.
    # df_cat = None
    # Draw the catplot with 'sns.catplot()'

    # Do not modify the next two lines
    fig.savefig('Project3/catplot.png', bbox_inches='tight', transparent=True)
    return fig

# ______________________________________________________________________________

# Draw Heat Map


def draw_heat_map(df):
    # Clean the data. Keep if:
    #- 'ap_hi' >= 'ap_lo'
    # - 2.5% < 'height' < 97.5%
    # - 2.5% < 'weight' < 97.5%
    h, w, lo, hi = df.height, df.weight, df.ap_lo, df.ap_hi
    df_clean = df[h.between(h.quantile(0.025), h.quantile(0.975)) &
                  w.between(w.quantile(0.025), w.quantile(0.975)) &
                  (hi >= lo)]
    # Calculate the correlation matrix
    corr = df_clean.corr()
    # Generate a mask for the upper triangle
    # Fill matrix of identical dimensions as correlation matrix with 1s
    # dtype = bool: fill with True instead of 1
    # Generate an upper triangle matrix: all bottom triangle bools to False
    mask = np.triu(np.ones_like(corr, dtype=bool))
    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 9))
    # Setting up a colormap
    # Use a diverging palette: 2 different colors centered around 0
    cmap = sns.color_palette("icefire", as_cmap=True)
    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(data=corr,
                mask=mask,
                cmap=cmap,
                center=0,
                square=True,
                linewidths=1,
                annot=True,
                fmt='.1f')
    # Do not modify the next two lines
    fig.savefig('Project3/heatmap.png', bbox_inches='tight', transparent=True)
    return fig


draw_cat_plot(df)
draw_heat_map(df)
