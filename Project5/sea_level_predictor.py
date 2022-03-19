import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file.
    df = pd.read_csv('Project5/epa-sea-level.csv')
    # Object-oriented Matplotlib interface.
    fig, ax = plt.subplots()
    # Discretizing time space.
    tfull_low = df['Year'].min()
    tfull_high = 2050
    time_full = np.arange(tfull_low, tfull_high + 1)
    trecent_low = 2000
    time_recent = np.arange(trecent_low, tfull_high + 1)
    # Create scatter plot.
    ax.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'],
               color=(0.85,0.85,0.85), label='Data')
    # Helper function.
    def linreg_fun(lr, val):
        '''A helper function to extract the mathematical expression from the 
        linear regression object.'''
        return lr.intercept + lr.slope * val
    # Creating the first line of best fit.
    lr1 = linregress(x=df['Year'], 
                     y=df['CSIRO Adjusted Sea Level'])    
    ax.plot(df['Year'],
            np.vectorize( lambda val : linreg_fun(lr1, val) )(df['Year']),
            color = (1,0,0),
            label = f'Linfit full [{time_full.min()}-{time_full.max()}]'
            )
    # Creating the second line of best fit.
    lr2 = linregress(x=df[ df['Year'] >= trecent_low ]['Year'],
                     y=df[ df['Year'] >= trecent_low ]['CSIRO Adjusted Sea Level'])
    ax.plot(time_recent,
            np.vectorize( lambda val : linreg_fun(lr2, val) )(time_recent),
            color = (0,0,1),
            label = f'Linfit recent [{time_recent.min()}-{time_recent.max()}]'
            )
    # Adding labels and title.
    ax.set_xlim(left  = tfull_low- 10,
                right = tfull_high + 10)    
    ax.set_title('Rise in sea level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea level [inches]')
    ax.legend(framealpha=0, loc='upper left')
    # Saving plot and return data for testing.
    fig.savefig('sea_level_plot.png',
                dpi=300, bbox_inches='tight', transparent=True)
    return fig

fig = draw_plot()