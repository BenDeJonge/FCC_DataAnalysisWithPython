import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import calendar
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

#______________________________________________________________________________

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(filepath_or_buffer='Project4/fcc-forum-pageviews.csv',
                 index_col=0)

# Clean data. Remove datapoints outside of the 2.5% and 97.5% percentiles.
df = df[
        df.value.between(df.value.quantile(0.025), df.value.quantile(0.975))
        ]
# Convert the index to datetime for date lookup. Infer format for quick processing.
df.index = pd.to_datetime(df.index, infer_datetime_format='%YYYY-&MM-%DD')

#______________________________________________________________________________

def draw_line_plot(df):
    # Object-oriented Matplotlib interface, separating the figure from the axis.
    fig, ax = plt.subplots()
    # Labelling both axes.
    ax.set_ylabel('Page Views')
    ax.set_xlabel('Date')
    # Formatting a title.
    start, end = [date.strftime('%m/%Y')
                  for date in (df.index[0], df.index[-1])]
    ax.set_title(f'Daily Free Code Camp Forum Page Views {start}-{end}')
    # Plotting the data.
    ax.plot(df, color='r')
    # Save image and return fig (don't change this part)
    fig.set_size_inches((16, 4))
    fig.savefig('Project4/line_plot.png',
                bbox_inches='tight', transparent=True)
    return fig

#______________________________________________________________________________


def draw_bar_plot(df):
    # Object-oriented Matplotlib interface, separating the figure from the axis.
    fig, ax = plt.subplots()
    # Labelling both axes.
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    # Setting up the bar plot ticks and labels.
    years = df.index.year.unique()
    ax.set_xticks(np.arange(len(years)))
    ax.set_xticklabels(years)
    # Defining a bar width to center 12 bars around the tick.
    bar_width = 0.075
    # Looping over all years and months and slicing the DataFrame.
    for x_tick, year in enumerate(years):
        for month in range(12):
            df_bar = df[df.index.year.isin([year]) &
                        df.index.month.isin([month+1])
                        ]
            # Format the bar color and position.
            bar_color = (1 - (month/11), 0, month/11)
            bar_pos = (x_tick - (6 - month) * bar_width) + bar_width/2
            # Plotting a bar.
            ax.bar(bar_pos, np.mean(df_bar.value),
                   width=bar_width,
                   color=bar_color,
                   edgecolor='black',
                   label=(lambda month: calendar.month_abbr[month])(month+1) 
                          if x_tick == 0 else ''
                   )
    # Formatting the legend.
    plt.tight_layout()
    fig.legend(loc='center left',
               bbox_to_anchor=(1,0.5),
               framealpha=0)
    # Save image and return fig (don't change this part)
    fig.savefig('Project4/bar_plot.png',
                bbox_inches='tight', 
                dpi=300,
                transparent=True)
    return fig

#______________________________________________________________________________


def draw_box_plot(df):
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    fig = None
    # Save image and return fig (don't change this part)
    # fig.savefig('Project4/box_plot.png', bbox_inches='tight', transparent=True)
    return fig

#______________________________________________________________________________


draw_line_plot(df)
draw_bar_plot(df)
draw_box_plot(df)