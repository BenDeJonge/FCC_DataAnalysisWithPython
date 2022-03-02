import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = None

# Clean data
df = None


def draw_line_plot():
    # Draw line plot
    fig = None




    # Save image and return fig (don't change this part)
    fig.savefig('Project4/line_plot.png', bbox_inches='tight', transparent=True)
    return fig

def draw_bar_plot():
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
