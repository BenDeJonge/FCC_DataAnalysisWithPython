import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(filepath_or_buffer='Project4/fcc-forum-pageviews.csv',
                 index_col=0)

# Clean data. Remove datapoints outside of the 2.5% and 97.5% percentiles.
df = df[ 
        df.value.between( df.value.quantile(0.025), df.value.quantile(0.975) )
        ]
df.index = pd.to_datetime(df.index, infer_datetime_format='%YYYY-&MM-%DD')

def draw_line_plot(df):
    # Object-oriented Matplotlib interface, separating the figure from the axis.
    fig, ax = plt.subplots()
    # Labelling both axes.
    ax.set_ylabel('Page Views')
    ax.set_xlabel('Date')
    # Formatting a title.
    start, end = [ date.strftime('%m/%Y') for date in (df.index[0], df.index[-1]) ]
    ax.set_title(f'Daily Free Code Camp Forum Page Views {start}-{end}')
    # Plotting the data.
    ax.plot(df, color='r')
    # Save image and return fig (don't change this part)
    fig.set_size_inches((16, 4))
    fig.savefig('Project4/line_plot.png', bbox_inches='tight', transparent=True)
    return fig

def draw_bar_plot(df):
    # Copy and modify data for monthly bar plot
    df_bar = None
    fig = None
    # Draw bar plot





    # Save image and return fig (don't change this part)
    fig.savefig('Project4/bar_plot.png', bbox_inches='tight', transparent=True)
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)




    fig = None
    # Save image and return fig (don't change this part)
    fig.savefig('Project4/box_plot.png', bbox_inches='tight', transparent=True)
    return fig

draw_line_plot(df)